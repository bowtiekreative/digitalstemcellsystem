#!/usr/bin/env python3
"""Verify the built site against the LAKA blocking rules and the live route table.

Checks, in order:
  1. Every page is well-formed HTML.
  2. LAKA header contract (rule nav.four, nav.no-inline, nav.name-case, brand.seal-asset).
  3. Exactly one h1 per page (LAKA seo system).
  4. Footer attribution (rule attr.footer).
  5. Every endpoint documented in build_site.py actually exists in app/main.py,
     and every route in app/main.py is documented.

Exits non-zero on any failure.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "tools"))

failures: list[str] = []
checks = 0


def check(ok: bool, label: str) -> None:
    global checks
    checks += 1
    if not ok:
        failures.append(label)


class Wellformed(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}>")
        elif self.stack[-1] != tag:
            self.errors.append(f"</{tag}> closes <{self.stack[-1]}>")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


PAGES = sorted(SITE.glob("*.html"))

print("Checking", len(PAGES), "pages\n")

for page in PAGES:
    text = page.read_text(encoding="utf-8")
    name = page.name

    p = Wellformed()
    p.feed(text)
    check(not p.errors and not p.stack,
          f"{name}: malformed HTML — {p.errors[:3]} unclosed={p.stack[:3]}")

    # --- header contract -------------------------------------------------
    header = re.search(r'<header class="laka-header">(.*?)</header>', text, re.S)
    if not header:
        check(False, f"{name}: no .laka-header")
        continue
    h = header.group(1)

    seal = len(re.findall(r'class="laka-header__seal"', h))
    site_name = len(re.findall(r'class="laka-header__name"', h))
    menu = len(re.findall(r"data-laka-menu=", h))
    cta = len(re.findall(r'class="laka-btn laka-btn--primary"', h))
    check(seal == 1, f"{name}: nav.four — expected 1 seal, found {seal}")
    check(site_name == 1, f"{name}: nav.four — expected 1 site name, found {site_name}")
    check(menu == 1, f"{name}: nav.four — expected 1 MENU button, found {menu}")
    check(cta == 1, f"{name}: nav.four — expected exactly 1 primary CTA, found {cta}")

    # nothing else in the bar: count anchors/buttons, seal link + name + menu + cta = 4
    controls = len(re.findall(r"<a |<button ", h))
    check(controls == 4, f"{name}: nav.no-inline — {controls} interactive elements in the bar, expected 4")

    check("btk-seal-white.png" in h, f"{name}: brand.seal-asset — canonical seal not used")
    check("Digital <span>StemCell</span>" in h,
          f"{name}: nav.name-case — site name must be two-tone (second word in accent)")

    # --- one h1 ----------------------------------------------------------
    h1s = len(re.findall(r"<h1[ >]", text))
    check(h1s == 1, f"{name}: seo — expected exactly 1 <h1>, found {h1s}")

    # --- attribution -----------------------------------------------------
    check("Powered by <a href=\"https://bowtiekreative.com\">Bow Tie Kreative</a>" in text,
          f"{name}: attr.footer — attribution line missing from the legal row")

    # --- metadata --------------------------------------------------------
    check('rel="canonical"' in text, f"{name}: seo — no canonical URL")
    check('name="description"' in text, f"{name}: seo — no meta description")

print(f"  header contract, HTML, SEO: {checks} checks")

# --------------------------------------------------------------------------
# Docs vs. actual routes
# --------------------------------------------------------------------------

import build_site  # noqa: E402

documented = set()
for _, entries in build_site.ENDPOINT_DOCS:
    for e in entries:
        documented.add((e["method"], e["path"]))

main_py = (ROOT / "api" / "app" / "main.py").read_text(encoding="utf-8")
actual = set()
for m in re.finditer(r'@app\.(get|post)\("([^"]+)"(.*?)\)', main_py, re.S):
    verb, path, rest = m.group(1).upper(), m.group(2), m.group(3)
    if "include_in_schema=False" in rest and path != "/llms.txt":
        continue
    if path == "/":
        continue
    actual.add((verb, path))

# normalise FastAPI's {param} names to the documented ones
ALIAS = {
    "/v1/prompts/{prompt_id}": "/v1/prompts/{id}",
    "/v1/modes/{mode_id}": "/v1/modes/{id}",
    "/v1/core/{core_id}": "/v1/core/{id}",
    "/v1/templates/{template_id}": "/v1/templates/{id}",
}
actual = {(v, ALIAS.get(p, p)) for v, p in actual}

undocumented = actual - documented
phantom = documented - actual

check(not undocumented, f"routes in main.py with no docs: {sorted(undocumented)}")
check(not phantom, f"documented endpoints that do not exist: {sorted(phantom)}")

print(f"  route coverage: {len(actual)} live routes, {len(documented)} documented\n")

if failures:
    print(f"FAILED — {len(failures)} of {checks} checks\n")
    for f in failures:
        print("  ✗", f)
    sys.exit(1)

print(f"PASSED — {checks} checks\n")
