"""DigitalStemCell API — the LAKA Volumetric Grammar as a REST service.

Read-only over a versioned corpus, plus two computed endpoints (/v1/score,
/v1/validate). Every GET is public; the shape mirrors the LAKA design-system
API so agents can treat both services the same way.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from jsonschema import Draft202012Validator

from . import loader

SERVICE = "digitalstemcell-api"
VERSION = "1.0.0"
DOCS_URL = "https://digitalstemcell.bowtiekreative.com"
API_URL = "https://api.digitalstemcell.bowtiekreative.com"

app = FastAPI(
    title="DigitalStemCell API",
    version=VERSION,
    description=(
        "The LAKA Volumetric Grammar as a REST service: five change levels x ten "
        "internal variables x fourteen meta-variables = 700 base coordinates, six "
        "operating modes, seventeen operators, templates, run schema and scoring."
    ),
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url=None,
)

class HeadRequestMiddleware:
    """Serve HEAD as GET with the body discarded.

    FastAPI's ``.get()`` decorator registers GET only, so HEAD returns 405 —
    which link checkers, uptime monitors and the LAKA release gate all read as
    a broken link. Per RFC 9110 a HEAD response keeps the GET headers
    (Content-Length included) and carries no body.
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") != "http" or scope.get("method") != "HEAD":
            return await self.app(scope, receive, send)

        sent_body = False

        async def send_wrapper(message):
            nonlocal sent_body
            if message["type"] != "http.response.body":
                await send(message)
                return
            if sent_body:
                return
            sent_body = True
            await send({"type": "http.response.body", "body": b"", "more_body": False})

        await self.app(dict(scope, method="GET"), receive, send_wrapper)


app.add_middleware(HeadRequestMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

C = loader.load()


def _cache(payload: Any, seconds: int = 3600) -> JSONResponse:
    return JSONResponse(payload, headers={"Cache-Control": f"public, max-age={seconds}"})


# --------------------------------------------------------------------------
# Index / health
# --------------------------------------------------------------------------

ENDPOINTS = [
    {"method": "GET", "path": "/v1/axes", "summary": "The three axes and their vocabularies"},
    {"method": "GET", "path": "/v1/axes/{axis}", "summary": "One axis: change-levels, internal-variables or meta-variables"},
    {"method": "GET", "path": "/v1/grid", "summary": "The 50-cell change x internal intent grid"},
    {"method": "GET", "path": "/v1/coordinates/{code}", "summary": "Resolve a coordinate such as LAKA-C3-I07-M08"},
    {"method": "GET", "path": "/v1/prompts", "summary": "Search and page the 700 prompt stems"},
    {"method": "GET", "path": "/v1/prompts/{id}", "summary": "One prompt stem by coordinate id"},
    {"method": "GET", "path": "/v1/modes", "summary": "The six operating modes"},
    {"method": "GET", "path": "/v1/modes/{id}", "summary": "One mode playbook"},
    {"method": "GET", "path": "/v1/operators", "summary": "The seventeen navigation and transformation operators"},
    {"method": "GET", "path": "/v1/operators/{name}", "summary": "One operator with guardrail and example"},
    {"method": "GET", "path": "/v1/core", "summary": "The seven core framework extracts"},
    {"method": "GET", "path": "/v1/core/{id}", "summary": "One core extract as Markdown"},
    {"method": "GET", "path": "/v1/templates", "summary": "Run, worksheet, concept card, forecast ledger, positioning"},
    {"method": "GET", "path": "/v1/templates/{id}", "summary": "One template as Markdown"},
    {"method": "GET", "path": "/v1/schema/run", "summary": "JSON Schema for a LAKA run"},
    {"method": "GET", "path": "/v1/schema/blank-run", "summary": "An empty run document to fill in"},
    {"method": "GET", "path": "/v1/scoring", "summary": "The proposed scoring rubric and hard gates"},
    {"method": "POST", "path": "/v1/score", "summary": "Compute the comparison index from ratings"},
    {"method": "POST", "path": "/v1/validate", "summary": "Validate a run document against the schema"},
    {"method": "GET", "path": "/v1/health", "summary": "Service health"},
]


@app.get("/v1", tags=["meta"])
@app.get("/", include_in_schema=False)
def index() -> JSONResponse:
    return _cache(
        {
            "service": SERVICE,
            "version": VERSION,
            "corpus_version": C.version,
            "documentation": DOCS_URL,
            "agent_guide": f"{API_URL}/llms.txt",
            "openapi": f"{API_URL}/v1/openapi.json",
            "interactive_docs": f"{API_URL}/v1/docs",
            "counts": {
                "change_levels": len(C.change_by_code),
                "internal_variables": len(C.internal_by_code),
                "meta_variables": len(C.meta_by_code),
                "coordinates": len(C.prompts),
                "grid_cells": len(C.grid),
                "operators": len(C.operator_by_name),
                "modes": len(C.modes),
                "templates": len(C.templates),
            },
            "endpoints": ENDPOINTS,
            "status_note": (
                "A coordinate is a question slot, not a validated innovation. "
                "The scoring index is an analyst-defined comparison number, not a probability."
            ),
        }
    )


@app.get("/v1/health", tags=["meta"])
def health() -> Dict[str, Any]:
    return {"status": "ok", "service": SERVICE, "version": VERSION, "coordinates": len(C.prompts)}


# --------------------------------------------------------------------------
# Axes and grid
# --------------------------------------------------------------------------

AXIS_KEYS = {
    "change-levels": "change_levels",
    "internal-variables": "internal_variables",
    "meta-variables": "meta_variables",
}


@app.get("/v1/axes", tags=["grammar"])
def axes() -> JSONResponse:
    return _cache(C.axes)


@app.get("/v1/axes/{axis}", tags=["grammar"])
def axis(axis: str) -> JSONResponse:
    key = AXIS_KEYS.get(axis)
    if not key:
        raise HTTPException(404, f"Unknown axis '{axis}'. Expected one of: {', '.join(AXIS_KEYS)}")
    return _cache({"axis": axis, "count": len(C.axes[key]), "items": C.axes[key]})


@app.get("/v1/grid", tags=["grammar"])
def grid(
    change: Optional[str] = Query(None, description="Change level code, e.g. C3"),
    internal: Optional[str] = Query(None, description="Internal variable code, e.g. I07"),
) -> JSONResponse:
    items = C.grid
    if change:
        items = [g for g in items if g["change_code"] == change.upper()]
    if internal:
        items = [g for g in items if g["internal_code"] == internal.upper()]
    return _cache({"count": len(items), "cells": items})


@app.get("/v1/coordinates/{code}", tags=["grammar"])
def coordinate(code: str) -> JSONResponse:
    parts = loader.parse_coordinate(code)
    if not parts:
        raise HTTPException(422, "Malformed coordinate. Expected the form LAKA-C3-I07-M08.")
    ch, iv, mv = parts
    prompt = C.prompts_by_id.get(f"LAKA-{ch}-{iv}-{mv}")
    cell = C.grid_by_pair.get((ch, iv))
    return _cache(
        {
            "id": f"LAKA-{ch}-{iv}-{mv}",
            "change_level": C.change_by_code.get(ch),
            "internal_variable": C.internal_by_code.get(iv),
            "meta_variable": C.meta_by_code.get(mv),
            "grid_intent": cell.get("intent") if cell else None,
            "prompt": prompt.get("prompt") if prompt else None,
        }
    )


# --------------------------------------------------------------------------
# Prompt library
# --------------------------------------------------------------------------


@app.get("/v1/prompts", tags=["prompts"])
def prompts(
    q: Optional[str] = Query(None, description="Free-text search across the prompt stem"),
    change: Optional[str] = Query(None, description="Change level code, e.g. C2"),
    internal: Optional[str] = Query(None, description="Internal variable code, e.g. I07"),
    meta: Optional[str] = Query(None, description="Meta-variable code, e.g. M08"),
    limit: int = Query(50, ge=1, le=700),
    offset: int = Query(0, ge=0),
) -> JSONResponse:
    items: List[dict] = C.prompts
    if change:
        items = [p for p in items if p["coordinate"]["change_code"] == change.upper()]
    if internal:
        items = [p for p in items if p["coordinate"]["internal_code"] == internal.upper()]
    if meta:
        items = [p for p in items if p["coordinate"]["meta_code"] == meta.upper()]
    if q:
        needle = q.lower()
        items = [p for p in items if needle in p["prompt"].lower() or needle in p["id"].lower()]
    return _cache(
        {
            "count": len(items),
            "limit": limit,
            "offset": offset,
            "prompts": items[offset : offset + limit],
        }
    )


@app.get("/v1/prompts/{prompt_id}", tags=["prompts"])
def prompt(prompt_id: str) -> JSONResponse:
    item = C.prompts_by_id.get(prompt_id.strip().upper())
    if not item:
        raise HTTPException(404, f"No prompt stem with id '{prompt_id}'.")
    return _cache(item)


# --------------------------------------------------------------------------
# Modes, operators, core, templates
# --------------------------------------------------------------------------


@app.get("/v1/modes", tags=["modes"])
def modes() -> JSONResponse:
    return _cache(
        {
            "count": len(C.modes),
            "overview_markdown": C.modes_overview,
            "modes": [{"id": m["id"], "title": m["title"]} for m in C.modes.values()],
        }
    )


@app.get("/v1/modes/{mode_id}", tags=["modes"])
def mode(mode_id: str) -> JSONResponse:
    item = C.modes.get(mode_id.strip().upper())
    if not item:
        raise HTTPException(404, f"Unknown mode '{mode_id}'. Expected one of: {', '.join(C.modes)}")
    return _cache(item)


@app.get("/v1/operators", tags=["operators"])
def operators(category: Optional[str] = Query(None)) -> JSONResponse:
    items = C.operators.get("operators", [])
    if category:
        items = [o for o in items if o["category"].lower() == category.lower()]
    return _cache({"count": len(items), "operators": items})


@app.get("/v1/operators/{name}", tags=["operators"])
def operator(name: str) -> JSONResponse:
    item = C.operator_by_name.get(name.strip().upper())
    if not item:
        raise HTTPException(404, f"Unknown operator '{name}'.")
    return _cache(item)


@app.get("/v1/core", tags=["reference"])
def core() -> JSONResponse:
    return _cache(
        {"count": len(C.core), "extracts": [{"id": x["id"], "title": x["title"], "file": x["file"]} for x in C.core.values()]}
    )


@app.get("/v1/core/{core_id}", tags=["reference"])
def core_item(core_id: str) -> JSONResponse:
    item = C.core.get(core_id.strip().lower())
    if not item:
        raise HTTPException(404, f"Unknown core extract '{core_id}'.")
    return _cache(item)


@app.get("/v1/templates", tags=["reference"])
def templates() -> JSONResponse:
    return _cache(
        {"count": len(C.templates), "templates": [{"id": x["id"], "title": x["title"], "file": x["file"]} for x in C.templates.values()]}
    )


@app.get("/v1/templates/{template_id}", tags=["reference"])
def template(template_id: str) -> JSONResponse:
    item = C.templates.get(template_id.strip().lower())
    if not item:
        raise HTTPException(404, f"Unknown template '{template_id}'.")
    return _cache(item)


@app.get("/v1/schema/run", tags=["schema"])
def run_schema() -> JSONResponse:
    return _cache(C.run_schema)


@app.get("/v1/schema/blank-run", tags=["schema"])
def blank_run() -> JSONResponse:
    return _cache(C.blank_run)


@app.get("/v1/scoring", tags=["schema"])
def scoring() -> JSONResponse:
    return _cache(C.scoring)


# --------------------------------------------------------------------------
# Computed endpoints
# --------------------------------------------------------------------------


class ScoreRequest(BaseModel):
    ratings: Dict[str, int] = Field(
        ...,
        description="Criterion id -> integer rating 0..4. Every rubric criterion must be present.",
    )
    hard_gates_passed: Optional[bool] = Field(
        None,
        description="Whether all four hard gates are satisfied. Omit or null when unknown.",
    )


@app.post("/v1/score", tags=["compute"])
def score(body: ScoreRequest) -> Dict[str, Any]:
    criteria = C.scoring["criteria"]
    lo, hi = C.scoring["rating_range"]

    missing = [c["id"] for c in criteria if c["id"] not in body.ratings]
    if missing:
        raise HTTPException(422, f"Missing ratings for: {', '.join(missing)}")
    unknown = [k for k in body.ratings if k not in {c['id'] for c in criteria}]
    if unknown:
        raise HTTPException(422, f"Unknown criteria: {', '.join(unknown)}")
    out_of_range = [k for k, v in body.ratings.items() if not (lo <= v <= hi)]
    if out_of_range:
        raise HTTPException(422, f"Ratings must be {lo}..{hi}. Out of range: {', '.join(out_of_range)}")

    contributions = []
    total = 0.0
    for c in criteria:
        r = body.ratings[c["id"]]
        share = c["weight"] * r / hi
        total += share
        contributions.append(
            {
                "id": c["id"],
                "question": c["question"],
                "weight": c["weight"],
                "rating": r,
                "anchor": C.scoring["anchors"][str(r)],
                "points": round(100 * share, 2),
            }
        )

    if body.hard_gates_passed is None:
        gate_status = "hold-for-investigation"
    elif body.hard_gates_passed:
        gate_status = "passed"
    else:
        gate_status = "blocked"

    return {
        "index": round(100 * total, 2),
        "gate_status": gate_status,
        "hard_gates": C.scoring["hard_gates"],
        "unknown_policy": C.scoring["unknown_policy"],
        "formula": C.scoring["formula"],
        "interpretation": C.scoring["interpretation"],
        "contributions": contributions,
        "caveat": (
            "This index is an analyst-defined comparison number from 0 to 100. "
            "It is not a success probability and does not establish novelty, feasibility or demand."
        ),
    }


@app.post("/v1/validate", tags=["compute"])
def validate(run: Dict[str, Any]) -> Dict[str, Any]:
    validator = Draft202012Validator(C.run_schema)
    errors = sorted(validator.iter_errors(run), key=lambda e: list(e.path))
    return {
        "valid": not errors,
        "error_count": len(errors),
        "errors": [
            {
                "path": "/".join(str(p) for p in e.path) or "(root)",
                "message": e.message,
                "validator": e.validator,
            }
            for e in errors
        ],
    }


# --------------------------------------------------------------------------
# Agent guide
# --------------------------------------------------------------------------


@app.get("/llms.txt", response_class=PlainTextResponse, include_in_schema=False)
def llms_txt(request: Request) -> str:
    lines = [
        "# DigitalStemCell API",
        "",
        "The LAKA Volumetric Grammar as a REST service. Every GET below is public and needs no key.",
        "",
        f"Corpus version: {C.version}",
        f"OpenAPI: {API_URL}/v1/openapi.json",
        f"Documentation: {DOCS_URL}",
        "",
        "## What the grammar is",
        "",
        "Five change levels (C0 Baseline -> C4 Paradigm) x ten internal variables",
        "(I01 Object .. I10 Failure mode) x fourteen meta-variables (M01 Magnitude ..",
        "M14 Accumulation) = 700 base coordinates. A coordinate is a question slot,",
        "not a guaranteed distinct, feasible, novel or valuable innovation.",
        "",
        "A coordinate id looks like LAKA-C3-I07-M08 = Structural Change x Feedback x Acceleration.",
        "",
        "## Endpoints",
        "",
    ]
    for e in ENDPOINTS:
        lines.append(f"{e['method']:4} {e['path']:34} {e['summary']}")
    lines += [
        "",
        "## Typical agent flow",
        "",
        "1. GET /v1/modes and pick a mode (GENERATE, SOLVE, DECODE, PREDICT, PLAN, POSITION).",
        "2. GET /v1/templates/run-laka for the master run template.",
        "3. Establish the baseline before proposing any change.",
        "4. GET /v1/prompts?change=C2&internal=I07 to pull a focused coordinate subset.",
        "5. Record answers as observation, assumption, hypothesis, transformation or not-applicable.",
        "6. POST /v1/validate with the run document to check it against the schema.",
        "7. POST /v1/score to produce a comparison index across concepts.",
        "",
        "## Limits",
        "",
        "This is a specification and working toolkit, not a validated forecasting system.",
        "State ladders are illustrative vocabularies, not calibrated numerical scales.",
        "An unfilled cell does not establish novelty or demand.",
        "A decoded explanation is not proof of intent or wrongdoing.",
    ]
    return "\n".join(lines)
