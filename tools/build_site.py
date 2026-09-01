#!/usr/bin/env python3
"""Render the DigitalStemCell documentation site.

One shell (head, LAKA header contract, mega menu, footer) plus one body per
page, so the header/footer can never drift between pages. Output is plain
static HTML written into site/ and served by nginx.

    python3 tools/build_site.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
GRAMMAR = ROOT / "Content" / "LAKA_Volumetric_Grammar"

SITE_URL = "https://digitalstemcell.bowtiekreative.com"
API_URL = "https://api.digitalstemcell.bowtiekreative.com"
BRAND = "https://designsystem.bowtiekreative.com"

# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------

NAV_GROUPS = [
    ("Documentation", [
        ("/", "Overview", "What the grammar is and how to call it"),
        ("/grammar.html", "The Grammar", "Axes, grid, coordinates, operators"),
        ("/reference.html", "API Reference", "Every endpoint, parameter and response"),
        ("/explorer.html", "Explorer", "Run live calls against the API"),
    ]),
    ("Machine readable", [
        (f"{API_URL}/v1/openapi.json", "OpenAPI 3.1", "The full specification"),
        (f"{API_URL}/llms.txt", "llms.txt", "Agent guide"),
        (f"{API_URL}/v1/docs", "Interactive docs", "Try requests in the browser"),
        (f"{API_URL}/v1", "Service index", "Live endpoint listing"),
    ]),
    ("Related", [
        (BRAND, "LAKA Design System", "The design library this site is built from"),
        ("https://bowtiekreative.com", "Bow Tie Kreative", "The studio"),
    ]),
]


def _menu_html() -> str:
    cols = []
    for heading, links in NAV_GROUPS:
        items = "\n".join(
            f'          <li><a href="{href}">{label}<small>{note}</small></a></li>'
            for href, label, note in links
        )
        cols.append(f"      <div>\n        <h2>{heading}</h2>\n        <ul>\n{items}\n        </ul>\n      </div>")
    return "\n".join(cols)


def _footer_html() -> str:
    cols = []
    for heading, links in NAV_GROUPS:
        items = "\n".join(f'          <li><a href="{href}">{label}</a></li>' for href, label, _ in links)
        cols.append(f"      <div>\n        <h2>{heading}</h2>\n        <ul>\n{items}\n        </ul>\n      </div>")
    return "\n".join(cols)


def shell(*, slug: str, title: str, description: str, body: str, cta: tuple[str, str] = ("/reference.html", "API Reference"), jsonld: dict | None = None) -> str:
    canonical = SITE_URL + ("/" if slug == "index" else f"/{slug}.html")
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">\n' + json.dumps(jsonld, separators=(",", ":")) + "\n</script>"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="DigitalStemCell">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BRAND}/brand/btk-seal.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<link rel="icon" sizes="32x32" href="{BRAND}/brand/favicon-32.png">
<link rel="apple-touch-icon" href="{BRAND}/brand/apple-touch-icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="{API_URL}">
<link rel="stylesheet" href="{BRAND}/dist/laka.css">
<link rel="stylesheet" href="/assets/site.css">
{ld}
</head>
<body class="laka">
<a class="skip" href="#main">Skip to content</a>

<div class="site-header">
  <header class="laka-header">
    <div class="laka-header__left">
      <a href="/" aria-label="DigitalStemCell home">
        <img class="laka-header__seal" src="{BRAND}/brand/btk-seal-white.png" alt="Bow Tie Kreative" width="34" height="34">
      </a>
      <a class="laka-header__name" href="/">Digital <span>StemCell</span></a>
    </div>
    <div class="laka-header__right">
      <button type="button" class="laka-btn laka-btn--outline" data-laka-menu="#megamenu" aria-expanded="false" aria-controls="megamenu">Menu</button>
      <a class="laka-btn laka-btn--primary" href="{cta[0]}">{cta[1]}</a>
    </div>
  </header>
  <nav class="megamenu" id="megamenu" hidden aria-label="Main">
    <div class="megamenu__inner">
{_menu_html()}
    </div>
  </nav>
</div>

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__cols">
{_footer_html()}
    </div>
    <div class="legal">
      <span>LAKA Volumetric Grammar v1.0-draft · API v1.0.0</span>
      <span>Powered by <a href="https://bowtiekreative.com">Bow Tie Kreative</a></span>
    </div>
  </div>
</footer>

<script src="{BRAND}/dist/laka.js" defer></script>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def section(inner: str, extra_class: str = "") -> str:
    cls = f"laka-section {extra_class}".strip()
    return f'  <section class="{cls}">\n    <div class="laka-section__inner">\n{inner}\n    </div>\n  </section>\n'


def heading(eyebrow: str, h: str, lede: str = "", level: int = 2) -> str:
    out = ['      <div class="stack stack--tight">', f'        <p class="laka-eyebrow">{eyebrow}</p>', f"        <h{level}>{h}</h{level}>"]
    if lede:
        out.append(f'        <p class="laka-lede">{lede}</p>')
    out.append("      </div>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Endpoint documentation — the source of truth for the reference page.
# Kept in step with app/main.py by tools/check_site.py.
# --------------------------------------------------------------------------

E = lambda **kw: kw  # noqa: E731

ENDPOINT_DOCS = [
    ("Meta", [
        E(method="GET", path="/v1", anchor="get-index",
          summary="Service index: version, counts and the endpoint listing.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1"),
        E(method="GET", path="/v1/health", anchor="get-health",
          summary="Liveness check. Returns the loaded coordinate count.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/health"),
        E(method="GET", path="/llms.txt", anchor="get-llms",
          summary="Plain-text agent guide: what the grammar is, every route, and the typical flow.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/llms.txt"),
    ]),
    ("Grammar", [
        E(method="GET", path="/v1/axes", anchor="get-axes",
          summary="All three axes in one document, with the origin note and the illustrative-state warning.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/axes"),
        E(method="GET", path="/v1/axes/{axis}", anchor="get-axis",
          summary="One axis on its own.",
          params=[("axis", "path", "required", "One of <code>change-levels</code>, <code>internal-variables</code>, <code>meta-variables</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/axes/meta-variables",
          errors=[("404", "The axis name is not one of the three.")]),
        E(method="GET", path="/v1/grid", anchor="get-grid",
          summary="The 50-cell grid pairing each change level with each internal variable, and the intent of that pairing.",
          params=[("change", "query", "optional", "Change level code, e.g. <code>C3</code>."),
                  ("internal", "query", "optional", "Internal variable code, e.g. <code>I07</code>.")],
          example="curl 'https://api.digitalstemcell.bowtiekreative.com/v1/grid?change=C3&internal=I07'"),
        E(method="GET", path="/v1/coordinates/{code}", anchor="get-coordinate",
          summary="Resolve a full coordinate into its three axis definitions, the grid intent and the prompt stem.",
          params=[("code", "path", "required", "A coordinate id of the form <code>LAKA-C3-I07-M08</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/coordinates/LAKA-C3-I07-M08",
          errors=[("422", "The code is malformed. Change is C0–C4, internal is I01–I10, meta is M01–M14.")]),
    ]),
    ("Prompts", [
        E(method="GET", path="/v1/prompts", anchor="get-prompts",
          summary="Search and page the 700 prompt stems. Filters combine with AND.",
          params=[("q", "query", "optional", "Free-text search across the prompt stem and the id."),
                  ("change", "query", "optional", "Change level code, e.g. <code>C2</code>."),
                  ("internal", "query", "optional", "Internal variable code, e.g. <code>I07</code>."),
                  ("meta", "query", "optional", "Meta-variable code, e.g. <code>M08</code>."),
                  ("limit", "query", "optional", "1–700. Defaults to 50."),
                  ("offset", "query", "optional", "Zero-based. Defaults to 0.")],
          example="curl 'https://api.digitalstemcell.bowtiekreative.com/v1/prompts?change=C2&internal=I07&limit=5'"),
        E(method="GET", path="/v1/prompts/{id}", anchor="get-prompt",
          summary="One prompt stem by coordinate id.",
          params=[("id", "path", "required", "Coordinate id, e.g. <code>LAKA-C0-I01-M01</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/prompts/LAKA-C0-I01-M01",
          errors=[("404", "No prompt stem carries that id.")]),
    ]),
    ("Modes and operators", [
        E(method="GET", path="/v1/modes", anchor="get-modes",
          summary="The six operating modes plus the overview table as Markdown.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/modes"),
        E(method="GET", path="/v1/modes/{id}", anchor="get-mode",
          summary="One mode playbook as Markdown.",
          params=[("id", "path", "required", "<code>DECODE</code>, <code>GENERATE</code>, <code>PLAN</code>, <code>POSITION</code>, <code>PREDICT</code> or <code>SOLVE</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/modes/PREDICT",
          errors=[("404", "Unknown mode name.")]),
        E(method="GET", path="/v1/operators", anchor="get-operators",
          summary="The seventeen operators with definition, input, output, guardrail and example.",
          params=[("category", "query", "optional", "Navigation, Transformation, Relationship, Control, Composition, Comparison or Selection.")],
          example="curl 'https://api.digitalstemcell.bowtiekreative.com/v1/operators?category=Transformation'"),
        E(method="GET", path="/v1/operators/{name}", anchor="get-operator",
          summary="One operator. Case-insensitive.",
          params=[("name", "path", "required", "e.g. <code>INVERT</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/operators/INVERT",
          errors=[("404", "Unknown operator name.")]),
    ]),
    ("Reference material", [
        E(method="GET", path="/v1/core", anchor="get-core",
          summary="The seven core framework extracts, listed by id and title.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/core"),
        E(method="GET", path="/v1/core/{id}", anchor="get-core-item",
          summary="One core extract as Markdown.",
          params=[("id", "path", "required", "e.g. <code>formal-grammar</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/core/formal-grammar",
          errors=[("404", "Unknown extract id.")]),
        E(method="GET", path="/v1/templates", anchor="get-templates",
          summary="The five working templates, listed by id and title.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/templates"),
        E(method="GET", path="/v1/templates/{id}", anchor="get-template",
          summary="One template as Markdown.",
          params=[("id", "path", "required", "<code>run-laka</code>, <code>worksheet</code>, <code>concept-card</code>, <code>forecast-ledger</code> or <code>strategy-and-positioning</code>.")],
          example="curl https://api.digitalstemcell.bowtiekreative.com/v1/templates/run-laka",
          errors=[("404", "Unknown template id.")]),
        E(method="GET", path="/v1/schema/run", anchor="get-schema-run",
          summary="The JSON Schema (2020-12) a run document must satisfy.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/schema/run"),
        E(method="GET", path="/v1/schema/blank-run", anchor="get-schema-blank",
          summary="An empty, schema-valid run document to fill in.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/schema/blank-run"),
        E(method="GET", path="/v1/scoring", anchor="get-scoring",
          summary="The seven weighted criteria, the four hard gates, the rating anchors and the formula.",
          params=[], example="curl https://api.digitalstemcell.bowtiekreative.com/v1/scoring"),
    ]),
    ("Compute", [
        E(method="POST", path="/v1/score", anchor="post-score",
          summary="Weight a set of 0–4 ratings into a 0–100 comparison index, with the per-criterion contribution shown.",
          params=[("ratings", "body", "required", "Object mapping every criterion id to an integer 0–4."),
                  ("hard_gates_passed", "body", "optional", "Boolean. Omit or send null when unknown — the result is then held for investigation.")],
          example="""curl -X POST https://api.digitalstemcell.bowtiekreative.com/v1/score \\
  -H 'content-type: application/json' \\
  -d '{
    "ratings": {
      "outcome_contribution": 3, "feasibility": 2, "evidence": 2,
      "adoption": 3, "differentiation": 4, "reversible_learning": 3,
      "robustness": 2
    },
    "hard_gates_passed": true
  }'""",
          errors=[("422", "A criterion is missing, unknown, or a rating falls outside 0–4.")]),
        E(method="POST", path="/v1/validate", anchor="post-validate",
          summary="Validate a run document against the run schema. Returns every error with its JSON path.",
          params=[("(body)", "body", "required", "The run document to validate.")],
          example="""curl -X POST https://api.digitalstemcell.bowtiekreative.com/v1/validate \\
  -H 'content-type: application/json' \\
  -d '{"run_id":"demo","mode":"GENERATE"}'"""),
    ]),
]


def render_reference_body() -> str:
    toc = ['      <nav class="toc" aria-label="On this page">']
    ops = []
    for group, entries in ENDPOINT_DOCS:
        toc.append(f"        <strong>{group}</strong>")
        for e in entries:
            toc.append(f'        <a href="#{e["anchor"]}">{html.escape(e["path"])}</a>')
            ops.append(_render_op(e))
    toc.append("      </nav>")

    inner = (
        heading("Reference", "API reference",
                level=1,
                lede=f'Base URL <code>{API_URL}</code>. Every endpoint is public — no key, no signup. '
                f'Responses are JSON and carry <code>Cache-Control: public, max-age=3600</code>. '
                f'The authoritative machine-readable contract is the <a href="{API_URL}/v1/openapi.json">OpenAPI 3.1 document</a>.')
        + '\n      <div class="ref">\n'
        + "\n".join(toc)
        + '\n      <div>\n'
        + "\n".join(ops)
        + "\n      </div>\n      </div>"
    )
    return section(inner)


def _render_op(e: dict) -> str:
    out = [f'        <article class="op" id="{e["anchor"]}">',
           '          <div class="op__head">',
           f'            <span class="endpoint__method" data-m="{e["method"]}">{e["method"]}</span>',
           f'            <h2 class="mono">{html.escape(e["path"])}</h2>',
           "          </div>",
           f'          <p>{e["summary"]}</p>']
    if e.get("params"):
        out += ['          <div class="table-wrap">', "          <table>",
                f'            <caption class="laka-visually-hidden">Parameters for {e["method"]} {html.escape(e["path"])}</caption>',
                "            <thead><tr><th>Name</th><th>In</th><th>Required</th><th>Description</th></tr></thead>",
                "            <tbody>"]
        for name, loc, req, desc in e["params"]:
            out.append(f"              <tr><td><code>{name}</code></td><td>{loc}</td><td>{req}</td><td>{desc}</td></tr>")
        out += ["            </tbody>", "          </table>", "          </div>"]
    out.append(f"<pre><code>{html.escape(e['example'])}</code></pre>")
    if e.get("errors"):
        out += ['          <div class="table-wrap">', "          <table>",
                f'            <caption class="laka-visually-hidden">Error responses for {e["method"]} {html.escape(e["path"])}</caption>',
                "            <thead><tr><th>Status</th><th>When</th></tr></thead>", "            <tbody>"]
        for code, when in e["errors"]:
            out.append(f"              <tr><td><code>{code}</code></td><td>{when}</td></tr>")
        out += ["            </tbody>", "          </table>", "          </div>"]
    out.append("        </article>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

def _load(rel: str):
    return json.loads((GRAMMAR / rel).read_text(encoding="utf-8"))


def render_index_body() -> str:
    hero = section(
        '      <p class="laka-eyebrow">Public REST API</p>\n'
        '      <h1 class="laka-display">A grammar for structured decisions.</h1>\n'
        '      <p class="laka-lede">The LAKA Volumetric Grammar treats any system as a sentence you can navigate:\n'
        '        five change levels &times; ten internal variables &times; fourteen meta-variables — 700 base\n'
        '        coordinates, each one a specific question about the system in front of you. This API serves all of it as JSON.</p>\n'
        '      <div class="hero__meta">\n'
        '        <span class="laka-chip">700 coordinates</span>\n'
        '        <span class="laka-chip">6 operating modes</span>\n'
        '        <span class="laka-chip">17 operators</span>\n'
        '        <span class="laka-chip">50-cell grid</span>\n'
        '        <span class="laka-chip">No API key</span>\n'
        "      </div>\n"
        '      <div class="hero__actions">\n'
        '        <a class="laka-btn laka-btn--primary" href="/reference.html">Read the reference</a>\n'
        '        <a class="laka-btn laka-btn--outline" href="/explorer.html">Open the explorer</a>\n'
        "      </div>",
        "hero",
    ).replace('<div class="laka-section__inner hero">', "")
    # inject the decorative lattice inside the hero section
    hero = hero.replace(
        '<div class="laka-section__inner">',
        '<div class="lattice" aria-hidden="true"></div>\n    <div class="laka-section__inner hero__inner">',
        1,
    )

    quickstart = section(
        heading("Quickstart", "One call, no key, no signup.",
                "Every GET endpoint is public. Resolve a coordinate to see the shape of the data.")
        + "\n<pre><code><span class=\"tok-c\"># Structural Change x Feedback x Acceleration</span>\n"
        f"curl <span class=\"tok-s\">{API_URL}/v1/coordinates/LAKA-C3-I07-M08</span></code></pre>\n"
        "<pre><code>{\n"
        '  <span class="tok-k">"id"</span>: <span class="tok-s">"LAKA-C3-I07-M08"</span>,\n'
        '  <span class="tok-k">"change_level"</span>:      { <span class="tok-k">"code"</span>: <span class="tok-s">"C3"</span>, <span class="tok-k">"label"</span>: <span class="tok-s">"Structural Change"</span>, ... },\n'
        '  <span class="tok-k">"internal_variable"</span>: { <span class="tok-k">"code"</span>: <span class="tok-s">"I07"</span>, <span class="tok-k">"label"</span>: <span class="tok-s">"Feedback"</span>, ... },\n'
        '  <span class="tok-k">"meta_variable"</span>:     { <span class="tok-k">"code"</span>: <span class="tok-s">"M08"</span>, <span class="tok-k">"label"</span>: <span class="tok-s">"Acceleration"</span>, ... },\n'
        '  <span class="tok-k">"grid_intent"</span>: <span class="tok-s">"Multiple adaptive loops across the system"</span>,\n'
        '  <span class="tok-k">"prompt"</span>: <span class="tok-s">"For [ACTOR] in [SCENARIO], ..."</span>\n'
        "}</code></pre>"
    )

    axes = _load("05_machine_readable/axes.json")
    cards = "\n".join([
        '        <article class="laka-card">\n'
        '          <h3 class="laka-card-title">5 change levels</h3>\n'
        "          <p>How far you are willing to move: "
        + ", ".join(f'<code>{c["code"]}</code> {c["label"]}' for c in axes["change_levels"])
        + ".</p>\n"
        '          <p class="laka-micro">GET /v1/axes/change-levels</p>\n        </article>',
        '        <article class="laka-card">\n'
        '          <h3 class="laka-card-title">10 internal variables</h3>\n'
        "          <p>The clauses of the system sentence: "
        + ", ".join(v["label"] for v in axes["internal_variables"])
        + ".</p>\n"
        '          <p class="laka-micro">GET /v1/axes/internal-variables</p>\n        </article>',
        '        <article class="laka-card">\n'
        '          <h3 class="laka-card-title">14 meta-variables</h3>\n'
        "          <p>How a clause can vary: "
        + ", ".join(v["label"] for v in axes["meta_variables"])
        + ".</p>\n"
        '          <p class="laka-micro">GET /v1/axes/meta-variables</p>\n        </article>',
    ])
    volume = section(
        heading("The volume", "Three axes multiply into one coordinate space.")
        + f'\n      <div class="laka-grid">\n{cards}\n      </div>\n'
        '      <div class="laka-panel">\n'
        "        <h3>5 &times; 10 &times; 14 = 700</h3>\n"
        "        <p>A coordinate such as <code>LAKA-C3-I07-M08</code> reads as <strong>Structural Change &times; Feedback &times; Acceleration</strong>. "
        "It is a question slot — an analysis prompt — not a guaranteed distinct, feasible, novel or valuable innovation.</p>\n"
        "      </div>"
    )

    rows = []
    for _, entries in ENDPOINT_DOCS:
        for e in entries:
            rows.append(
                f'        <div class="endpoint"><span class="endpoint__method" data-m="{e["method"]}">{e["method"]}</span>'
                f'<span class="endpoint__path mono">{html.escape(e["path"])}</span>'
                f'<span class="endpoint__summary">{e["summary"]}</span></div>'
            )
    count = len(rows)
    endpoints = section(
        heading("Endpoints", f"{count} routes across six groups.",
                'Full parameters and response shapes are in the <a href="/reference.html">API reference</a>.')
        + f'\n      <div class="endpoints">\n' + "\n".join(rows) + "\n      </div>"
    )

    honesty = section(
        heading("Honesty", "What this is not.")
        + '\n      <div class="laka-banner laka-banner--warning" role="note">\n'
        "        <p><strong>A specification and working toolkit — not a validated forecasting system.</strong></p>\n"
        "      </div>\n"
        '      <div class="laka-grid">\n'
        '        <article class="laka-card"><h3 class="laka-card-title">Coordinates are questions</h3>'
        "<p>An unfilled cell does not establish novelty or demand. Filling one produces an observation, assumption, "
        "hypothesis or documented not-applicable result — nothing stronger.</p></article>\n"
        '        <article class="laka-card"><h3 class="laka-card-title">State ladders are vocabularies</h3>'
        "<p>The illustrative states are not calibrated ordinal scales and do not map onto change levels.</p></article>\n"
        '        <article class="laka-card"><h3 class="laka-card-title">The score is an index</h3>'
        "<p><code>/v1/score</code> returns an analyst-defined comparison number from 0 to 100. It is not a success probability.</p></article>\n"
        '        <article class="laka-card"><h3 class="laka-card-title">DECODE is not proof</h3>'
        "<p>A decoded explanation of a system is not proof of intent or wrongdoing.</p></article>\n"
        "      </div>"
    )

    return hero + quickstart + volume + endpoints + honesty


def render_grammar_body() -> str:
    axes = _load("05_machine_readable/axes.json")
    grid = _load("05_machine_readable/internal_grid.json")
    ops = _load("05_machine_readable/operators.json")["operators"]

    intro = section(
        '      <p class="laka-eyebrow">The grammar</p>\n'
        "      <h1>How the volume is built.</h1>\n"
        '      <p class="laka-lede">Every endpoint in this API is a view onto one structure: a system described as a '
        "sentence, and a coordinate space of ways that sentence can change. This page is the vocabulary; the "
        '<a href="/reference.html">reference</a> is the calling convention.</p>'
    )

    def table(rows, headers, caption):
        h = "".join(f"<th>{x}</th>" for x in headers)
        body = "\n".join("            <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
        return ('      <div class="table-wrap">\n        <table>\n'
                f'          <caption class="laka-visually-hidden">{caption}</caption>\n'
                f"          <thead><tr>{h}</tr></thead>\n          <tbody>\n{body}\n          </tbody>\n"
                "        </table>\n      </div>")

    changes = section(
        heading("Axis one", "Five change levels",
                "How far the transformation is allowed to reach. C0 is not a change — it is the baseline you must "
                "establish before proposing any of the others.")
        + "\n" + table(
            [(f'<code>{c["code"]}</code>', f'<strong>{c["label"]}</strong>', c["definition"], f'<em>{c["operator_examples"]}</em>')
             for c in axes["change_levels"]],
            ["Code", "Level", "Definition", "Typical operators"], "The five change levels")
    )

    internals = section(
        heading("Axis two", "Ten internal variables",
                "The clauses of the system sentence. Together they say who does what to which object, under what "
                "conditions, with what, producing what, and how it breaks.")
        + "\n" + table(
            [(f'<code>{v["code"]}</code>', f'<strong>{v["label"]}</strong>', v["question"], v["grammar_role"])
             for v in axes["internal_variables"]],
            ["Code", "Variable", "Question it answers", "Grammar role"], "The ten internal variables")
    )

    metas = section(
        heading("Axis three", "Fourteen meta-variables",
                "How any one clause can vary. The illustrative states are vocabularies for describing a direction of "
                "travel — they are not calibrated scales.")
        + "\n" + table(
            [(f'<code>{v["code"]}</code>', f'<strong>{v["label"]}</strong>', v["question"])
             for v in axes["meta_variables"]],
            ["Code", "Meta-variable", "Question it answers"], "The fourteen meta-variables")
    )

    coord = section(
        heading("Reading a coordinate", "LAKA-C3-I07-M08")
        + '\n      <div class="laka-panel">\n'
        "        <p><code>C3</code> Structural Change &times; <code>I07</code> Feedback &times; <code>M08</code> Acceleration — "
        "<em>“how might the rate of change of the system's feedback loops be restructured?”</em></p>\n"
        "      </div>\n"
        "      <p>The 50-cell grid pairs each change level with each internal variable and names the intent of that "
        "pairing. The meta-variable then selects which property of the clause is in play. "
        f'Fetch any single coordinate from <code>GET /v1/coordinates/{{code}}</code>.</p>\n'
        + table(
            [(f'<code>{g["change_code"]}</code> {g["change_level"]}', f'<code>{g["internal_code"]}</code> {g["internal_variable"]}', g["intent"])
             for g in grid if g["change_code"] in ("C0", "C4")],
            ["Change level", "Internal variable", "Intent"], "Grid intents for the C0 and C4 rows")
        + '\n      <p class="laka-micro">Showing the C0 and C4 rows. All 50 cells: GET /v1/grid</p>'
    )

    by_cat: dict[str, list] = {}
    for o in ops:
        by_cat.setdefault(o["category"], []).append(o)
    op_cards = "\n".join(
        '        <article class="laka-card">\n'
        f'          <h3 class="laka-card-title">{cat}</h3>\n'
        "          <p>" + ", ".join(f"<code>{o['name']}</code>" for o in items) + "</p>\n"
        "          <p>" + items[0]["definition"] + "</p>\n"
        "        </article>"
        for cat, items in by_cat.items()
    )
    operators = section(
        heading("Operators", f"{len(ops)} moves through the volume",
                "Operators are how you get from one coordinate to another. Each one carries a guardrail — the "
                "condition under which applying it would be invalid.")
        + f'\n      <div class="laka-grid">\n{op_cards}\n      </div>\n'
        '      <p class="laka-micro">Full definitions, inputs, outputs and guardrails: GET /v1/operators</p>'
    )

    modes = section(
        heading("Modes", "Six ways to read the same volume",
                "The coordinate space does not change; the question you bring to it does.")
        + "\n" + table([
            ("<code>GENERATE</code>", "Produce candidate transformations from unfilled coordinates."),
            ("<code>SOLVE</code>", "Move a specific failing clause to an acceptable state."),
            ("<code>DECODE</code>", "Explain an existing system by locating it in the volume."),
            ("<code>PREDICT</code>", "Project how meta-variables carry a clause forward."),
            ("<code>PLAN</code>", "Sequence transformations into a feasible order."),
            ("<code>POSITION</code>", "Compare your system sentence against alternatives."),
        ], ["Mode", "How it reads the volume"], "The six operating modes")
        + '\n      <p class="laka-micro">Each mode ships a full playbook: GET /v1/modes/{id}</p>'
    )

    return intro + changes + internals + metas + coord + operators + modes


def render_explorer_body() -> str:
    presets = "\n".join(
        f'            <option value="{k}">{v}</option>'
        for k, v in [
            ("coordinate", "Resolve a coordinate"),
            ("prompts", "Search prompt stems"),
            ("axes", "List the meta-variables"),
            ("grid", "Grid rows for C4"),
            ("modes", "The PREDICT playbook"),
            ("operators", "Transformation operators"),
            ("templates", "The RUN LAKA template"),
            ("scoring", "The scoring rubric"),
            ("score", "Score a concept (POST)"),
            ("validate", "Validate a run (POST)"),
        ]
    )
    body = (
        '      <p class="laka-eyebrow">Explorer</p>\n'
        "      <h1>Call the API from here.</h1>\n"
        '      <p class="laka-lede">Requests go straight from your browser to '
        f'<code>{API_URL}</code>. Nothing is proxied and nothing is stored.</p>\n'
        '      <div class="explorer">\n'
        '        <form id="explorer-form" class="laka-card">\n'
        '          <div class="laka-field">\n'
        '            <label class="laka-label" for="explorer-preset">Preset</label>\n'
        '            <select class="laka-select" id="explorer-preset" name="preset">\n'
        f"{presets}\n"
        "            </select>\n"
        "          </div>\n"
        '          <div class="laka-field">\n'
        '            <label class="laka-label" for="explorer-method">Method</label>\n'
        '            <select class="laka-select" id="explorer-method" name="method">\n'
        '              <option value="GET">GET</option>\n'
        '              <option value="POST">POST</option>\n'
        "            </select>\n"
        "          </div>\n"
        '          <div class="laka-field">\n'
        '            <label class="laka-label" for="explorer-path">Path</label>\n'
        '            <input class="laka-input" id="explorer-path" name="path" type="text" value="/v1/coordinates/LAKA-C3-I07-M08" spellcheck="false" autocapitalize="off" autocomplete="off">\n'
        '            <p class="laka-hint">Begins with a slash, e.g. <code>/v1/prompts?change=C2</code></p>\n'
        "          </div>\n"
        '          <div class="laka-field" id="explorer-body-field" hidden>\n'
        '            <label class="laka-label" for="explorer-body">Request body (JSON)</label>\n'
        '            <textarea class="laka-textarea" id="explorer-body" name="body" rows="10" spellcheck="false"></textarea>\n'
        "          </div>\n"
        '          <button class="laka-btn laka-btn--primary" type="submit">Send request</button>\n'
        "        </form>\n"
        '        <div class="stack">\n'
        '          <p class="mono laka-micro" id="explorer-url">GET</p>\n'
        '          <p id="explorer-status" class="laka-hint" role="status" aria-live="polite">Ready.</p>\n'
        '          <div class="result"><pre><code id="explorer-output"></code></pre></div>\n'
        "        </div>\n"
        "      </div>"
    )
    return section(body)


def render_404_body() -> str:
    return section(
        '      <p class="laka-eyebrow">404</p>\n'
        "      <h1>That page is not in the volume.</h1>\n"
        '      <p class="laka-lede">The link may be out of date. Start from the overview, or go straight to the reference.</p>\n'
        '      <div class="hero__actions">\n'
        '        <a class="laka-btn laka-btn--primary" href="/">Overview</a>\n'
        '        <a class="laka-btn laka-btn--outline" href="/reference.html">API reference</a>\n'
        "      </div>"
    )


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

PAGES = [
    dict(slug="index", file="index.html",
         title="DigitalStemCell API — the LAKA Volumetric Grammar",
         description="A public REST API over the LAKA Volumetric Grammar: 700 base coordinates, six operating modes, seventeen operators, run schema and scoring rubric.",
         render=render_index_body, priority="1.0",
         jsonld={"@context": "https://schema.org", "@type": "WebAPI", "name": "DigitalStemCell API",
                 "description": "The LAKA Volumetric Grammar as a REST service: 700 base coordinates, six operating modes, seventeen operators, run schema and scoring rubric.",
                 "documentation": f"{SITE_URL}/reference.html",
                 "provider": {"@type": "Organization", "name": "Bow Tie Kreative", "url": "https://bowtiekreative.com"}}),
    dict(slug="grammar", file="grammar.html",
         title="The Grammar — DigitalStemCell API",
         description="The three axes of the LAKA Volumetric Grammar: five change levels, ten internal variables, fourteen meta-variables, the 50-cell grid, seventeen operators and six modes.",
         render=render_grammar_body, priority="0.8",
         jsonld={"@context": "https://schema.org", "@type": "TechArticle",
                 "headline": "The LAKA Volumetric Grammar",
                 "description": "The three axes of the LAKA Volumetric Grammar, the 50-cell grid, seventeen operators and six operating modes.",
                 "url": f"{SITE_URL}/grammar.html",
                 "publisher": {"@type": "Organization", "name": "Bow Tie Kreative", "url": "https://bowtiekreative.com"}}),
    dict(slug="reference", file="reference.html",
         title="API Reference — DigitalStemCell API",
         description="Every DigitalStemCell endpoint with parameters, examples and error codes. Public, no API key required.",
         render=render_reference_body, priority="0.9",
         jsonld={"@context": "https://schema.org", "@type": "APIReference",
                 "name": "DigitalStemCell API reference",
                 "description": "Every DigitalStemCell endpoint with parameters, examples and error codes.",
                 "url": f"{SITE_URL}/reference.html",
                 "programmingModel": "REST",
                 "publisher": {"@type": "Organization", "name": "Bow Tie Kreative", "url": "https://bowtiekreative.com"}}),
    dict(slug="explorer", file="explorer.html",
         title="Explorer — DigitalStemCell API",
         description="Run live requests against the DigitalStemCell API from the browser.",
         render=render_explorer_body, priority="0.7",
         jsonld={"@context": "https://schema.org", "@type": "WebApplication",
                 "name": "DigitalStemCell API explorer",
                 "description": "Run live requests against the DigitalStemCell API from the browser.",
                 "url": f"{SITE_URL}/explorer.html",
                 "applicationCategory": "DeveloperApplication",
                 "browserRequirements": "Requires JavaScript",
                 "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                 "publisher": {"@type": "Organization", "name": "Bow Tie Kreative", "url": "https://bowtiekreative.com"}}),
    dict(slug="404", file="404.html",
         title="Page not found — DigitalStemCell API",
         description="That page is not in the volume.",
         render=render_404_body, priority=None),
]


def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)

    for page in PAGES:
        cta = ("/explorer.html", "Explorer") if page["slug"] == "reference" else ("/reference.html", "API Reference")
        out = shell(
            slug=page["slug"], title=page["title"], description=page["description"],
            body=page["render"](), cta=cta, jsonld=page.get("jsonld"),
        )
        (SITE / page["file"]).write_text(out, encoding="utf-8")
        print(f"  wrote site/{page['file']:16} {len(out):>7,} bytes")

    urls = "\n".join(
        f"  <url><loc>{SITE_URL}{'/' if p['slug'] == 'index' else '/' + p['file']}</loc>"
        f"<priority>{p['priority']}</priority></url>"
        for p in PAGES if p["priority"]
    )
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n", encoding="utf-8")

    (SITE / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")

    print("  wrote site/sitemap.xml, site/robots.txt")


if __name__ == "__main__":
    main()
