# DigitalStemCell

The **LAKA Volumetric Grammar** as a public REST API, plus its documentation site.

| Surface | URL | Served by |
|---|---|---|
| Documentation | https://digitalstemcell.bowtiekreative.com | `web` (nginx, static) |
| API | https://api.digitalstemcell.bowtiekreative.com | `api` (FastAPI, uvicorn) |
| OpenAPI 3.1 | `/v1/openapi.json` | `api` |
| Agent guide | `/llms.txt` | `api` |

Every GET endpoint is public — no key, no signup.

## What the grammar is

Five change levels (`C0` Baseline → `C4` Paradigm) × ten internal variables
(`I01` Object … `I10` Failure mode) × fourteen meta-variables (`M01` Magnitude …
`M14` Accumulation) = **700 base coordinates**.

A coordinate id such as `LAKA-C3-I07-M08` reads as *Structural Change × Feedback ×
Acceleration*. It is a question slot — an analysis prompt — **not** a guaranteed
distinct, feasible, novel or valuable innovation.

## Layout

```
Content/LAKA_Volumetric_Grammar/   the corpus — source of truth, not generated
api/                              FastAPI service
  app/loader.py                   reads the corpus into memory at startup
  app/main.py                     the 22 routes
site/                             generated static docs (committed)
tools/build_site.py               renders every page from one shell
tools/check_site.py               LAKA rule + route-drift checks
docker-compose.dokploy.yml        the deployed stack
```

The corpus under `Content/` is hand-authored and is the single source of truth.
The API reads it; it never writes to it.

## Working on the site

The site is generated — **edit `tools/build_site.py`, never `site/*.html`.**

```bash
python3 tools/build_site.py    # regenerate site/
python3 tools/check_site.py    # verify before committing
```

`check_site.py` enforces the LAKA blocking rules (`nav.four`, `nav.no-inline`,
`nav.name-case`, `brand.seal-asset`, `attr.footer`), one `<h1>` per page, HTML
well-formedness, and that the documented endpoints exactly match the routes in
`api/app/main.py`. It exits non-zero on any failure.

## Running locally

```bash
docker compose -f docker-compose.dokploy.yml build
docker run --rm -p 8000:8000 decisionmaking-api:latest
docker run --rm -p 8080:80   decisionmaking-web:latest
```

Or run the API straight from the source tree:

```bash
pip install -r api/requirements.txt
cd api && GRAMMAR_DIR=../Content/LAKA_Volumetric_Grammar \
  uvicorn app.main:app --reload
```

## Design

The docs site is built from the [LAKA Design System](https://designsystem.bowtiekreative.com)
— `laka.css` and `laka.js` are linked from the CDN, and all colour, spacing,
radius and focus tokens come from there. No design tokens are redefined locally;
`site/assets/site.css` adds layout only.

## Status and limits

This is a specification and working toolkit, not a deployed decision engine, a
proven universal grammar, or an empirically validated forecasting system.

- State ladders are illustrative vocabularies, not calibrated numerical scales.
- An unfilled coordinate does not establish novelty or demand.
- `/v1/score` returns an analyst-defined comparison index from 0 to 100 — not a
  success probability.
- A DECODE result is not proof of intent or wrongdoing.
