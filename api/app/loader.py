"""Load the LAKA Volumetric Grammar corpus into memory once at startup.

The corpus is a directory of JSON (machine-readable axes, operators, grid,
schema, rubric) and Markdown (core extracts, mode playbooks, templates).
Everything is read eagerly and kept in a single Corpus instance -- the data
is small (~500KB) and entirely read-only, so there is no cache to invalidate.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

GRAMMAR_DIR = Path(os.environ.get("GRAMMAR_DIR", "/app/grammar"))

MODE_IDS = ["DECODE", "GENERATE", "PLAN", "POSITION", "PREDICT", "SOLVE"]

TEMPLATE_FILES = {
    "run-laka": "RUN_LAKA.md",
    "worksheet": "WORKSHEET.md",
    "concept-card": "CONCEPT_CARD.md",
    "forecast-ledger": "FORECAST_LEDGER.md",
    "strategy-and-positioning": "STRATEGY_AND_POSITIONING.md",
}

CORE_FILES = {
    "volume-and-context": "01_volume_and_context.md",
    "system-sentence-and-state-transitions": "02_system_sentence_and_state_transitions.md",
    "change-levels-and-internal-grid": "03_change_levels_and_internal_grid.md",
    "meta-variables-and-state-ladders": "04_meta_variables_and_state_ladders.md",
    "formal-grammar": "05_formal_grammar.md",
    "navigation-and-operators": "06_navigation_and_operators.md",
    "run-laka-and-validation-rules": "07_run_laka_and_validation_rules.md",
}

COORDINATE_RE = re.compile(r"^LAKA-(C[0-4])-(I0[1-9]|I10)-(M0[1-9]|M1[0-4])$")


def _read_json(rel: str):
    return json.loads((GRAMMAR_DIR / rel).read_text(encoding="utf-8"))


def _read_text(rel: str) -> str:
    return (GRAMMAR_DIR / rel).read_text(encoding="utf-8")


def _title_of(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


@dataclass
class Corpus:
    version: str = ""
    axes: dict = field(default_factory=dict)
    operators: dict = field(default_factory=dict)
    grid: list = field(default_factory=list)
    scoring: dict = field(default_factory=dict)
    run_schema: dict = field(default_factory=dict)
    blank_run: dict = field(default_factory=dict)
    prompts: list = field(default_factory=list)
    prompts_by_id: dict = field(default_factory=dict)
    modes: dict = field(default_factory=dict)
    modes_overview: str = ""
    templates: dict = field(default_factory=dict)
    core: dict = field(default_factory=dict)
    master_grammar: str = ""

    # ---- derived lookups -------------------------------------------------
    change_by_code: dict = field(default_factory=dict)
    internal_by_code: dict = field(default_factory=dict)
    meta_by_code: dict = field(default_factory=dict)
    grid_by_pair: dict = field(default_factory=dict)
    operator_by_name: dict = field(default_factory=dict)


def load() -> Corpus:
    c = Corpus()

    c.axes = _read_json("05_machine_readable/axes.json")
    c.operators = _read_json("05_machine_readable/operators.json")
    c.grid = _read_json("05_machine_readable/internal_grid.json")
    c.scoring = _read_json("05_machine_readable/scoring_rubric.json")
    c.run_schema = _read_json("05_machine_readable/laka_run.schema.json")
    c.blank_run = _read_json("05_machine_readable/blank_run.json")

    prompt_doc = _read_json("03_prompt_library/700_prompt_stems.json")
    c.prompts = prompt_doc.get("prompts", [])
    c.prompts_by_id = {p["id"]: p for p in c.prompts}

    c.version = c.axes.get("version", "1.0-draft")

    c.change_by_code = {x["code"]: x for x in c.axes.get("change_levels", [])}
    c.internal_by_code = {x["code"]: x for x in c.axes.get("internal_variables", [])}
    c.meta_by_code = {x["code"]: x for x in c.axes.get("meta_variables", [])}
    c.grid_by_pair = {(g["change_code"], g["internal_code"]): g for g in c.grid}
    c.operator_by_name = {o["name"].upper(): o for o in c.operators.get("operators", [])}

    c.modes_overview = _read_text("02_operating_modes/00_modes_overview.md")
    for mode in MODE_IDS:
        body = _read_text(f"02_operating_modes/{mode}.md")
        c.modes[mode] = {
            "id": mode,
            "title": _title_of(body, mode),
            "markdown": body,
        }

    for tid, fname in TEMPLATE_FILES.items():
        body = _read_text(f"04_templates/{fname}")
        c.templates[tid] = {
            "id": tid,
            "title": _title_of(body, tid),
            "file": fname,
            "markdown": body,
        }

    for cid, fname in CORE_FILES.items():
        body = _read_text(f"01_core/{fname}")
        c.core[cid] = {
            "id": cid,
            "title": _title_of(body, cid),
            "file": fname,
            "markdown": body,
        }

    c.master_grammar = _read_text("LAKA_MASTER_GRAMMAR.md")
    return c


def parse_coordinate(code: str):
    """Return (change_code, internal_code, meta_code) or None if malformed."""
    m = COORDINATE_RE.match(code.strip().upper())
    return m.groups() if m else None
