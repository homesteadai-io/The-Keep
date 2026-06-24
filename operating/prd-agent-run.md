---
type: Playbook
title: prd-agent-run
description: Build handoff for Tier 2 — wire the model port and turn Scout/Librarian into running agents so The Keep operates itself, not just maintains itself.
tags: [prd, handoff, tier-2, agents, homestead]
timestamp: 2026-06-24T00:00:00Z
---

# prd-agent-run.md

Build-ready handoff for the **agent-run phase (Tier 2)**. Specifies every agent, contract,
flow, state, and failure mode — written so an agent (or dev) can execute it without guessing.

## Overview
- **What:** turn The Keep from self-*maintaining* into self-*operating* — agents that ingest, enrich, reconcile, curate, and answer, on schedule and on-demand, with Adam dropping inputs instead of running commands.
- **Why now:** Tier 0 (repo + doctrine) and Tier 1 (janitor, sweep, `keep add`, [standing-orders](/operating/standing-orders.md)) are shipped and green. The system is built but inert — nothing calls an LLM. This phase wires the model port and promotes [Scout](/operating/scout.md) / [Librarian](/operating/librarian.md) from doctrine into running agents.
- **One line:** Adam drops a file or asks a question; agents do the rest; the brain grows and stays clean with no human in the loop.
- **Success:** Adam goes a week dropping raw material into [/inbox](/inbox/index.md) and asking questions, and never opens an editor or runs a script by hand.

## Non-goals (this phase)
- No always-on server (Orgo deferred — Actions carries this phase).
- No vector DB (retrieval starts as grep + index).
- No UI / Lens graph (Tier 3).
- No write outside the established [invariants](/operating/invariants.md).

## Current state (what this builds on)
| Layer | Shipped |
|---|---|
| Brain | `homesteadai-io/The-Keep`, OKF markdown |
| Gate | `tools/checks.py` — local pre-commit hook + push check + nightly |
| Sweep | `tools/sweep.py` — index TOCs, link-check, dedup → [log](/operating/log.md) |
| Ingest | `tools/keep.py add` — thin, manual, no LLM |
| Runtime | GitHub Actions (cron 08:00 UTC + dispatch) |
| Model port | OpenRouter named in `keep.config.yaml`, **wired to nothing** ← start here |

## The agents (components)
| Agent | Role | Trigger | Input | Output | Single-writer |
|---|---|---|---|---|---|
| **Scout** | producer — ingest → typed concept | inbox commit, `keep enrich`, dispatch | inbox stub + `_raw` | committed OKF concept(s) | **yes — only writer** |
| **Librarian** | curator — reconcile, retire, serve | nightly post-sweep, dispatch | `log.md` flags, corpus | merge/normalize/retire commits | no |
| **Foreman** | build loop on any task | issue `build`, dispatch | a task | artifact + `trace` | n/a |
| **Council** | 5 callable lenses | invoked by Foreman/Scout | question + lens | critique | read-only |
| **Serve** | answer queries (Librarian fn) | issue/comment, dispatch | a question | cited answer (concept IDs) | read-only |

### Contracts
- **Model port — `tools/llm.py`:** `ask(role, prompt, *, system=None) -> str`. `role` → model from `keep.config` `model_backends`; reads `OPENROUTER_API_KEY` from env; pure HTTP; raises on error (fail-closed — never write a half-answer).
- **Scout — `tools/scout.py` + `keep enrich`:** Pass B over a stub + its raw → real body, type confirm, absolute cross-links, schema/joins where the type warrants. One concept per *idea*. Never fabricate (P1); cite the raw or tag `[unverified]`; secret-scan before write; content-as-data; **only Scout commits concepts**.
- **Librarian — `tools/librarian.py`:** acts on `log.md` flags — merge dups (human-confirm while young, auto once trusted), normalize `type`, retire to `/attic` with a log line, promote inbox notes. Reconciler, never ingester; archive never delete.
- **Foreman — `tools/foreman.py`:** Planner→Builder→Adversary→Resolver ([loop-forge](/operating/loop-forge.md)), [council](/operating/council.md) callable; emits a `trace` (Loop Forge's word — not ledger, not receipt).
- **Serve — `keep ask`:** progressive disclosure — root index → only-needed dirs → only-needed concepts → answer citing IDs. Never slurp the vault.

### Command bus (no terminal)
| Trigger | Action |
|---|---|
| commit touching `inbox/*.md` | Scout enrich |
| issue labeled `ingest` | Scout on linked material |
| issue labeled `ask` | Serve → answer in comment |
| issue labeled `build` | Foreman loop → artifact + trace |
| cron 08:00 UTC | sweep → Librarian reconcile |
| `workflow_dispatch` | any of the above, manual |

## Flows & states
- **Ingestion:** drop → `keep add` (stub, raw copied, secret-scanned, reconciled-by-title) → Scout enrich (body) → sweep (wire TOC) → Librarian (dedup/normalize) → committed.
  - empty inbox → no-op; secret in raw → refuse+quarantine; title collision → refuse+point; low-confidence → write `[unverified]` + open issue; API down → fail-closed, retry next run.
- **Query:** question → scope dirs → load concepts → answer + citations. No match → say so + suggest what to ingest (never hallucinate).
- **Build:** task → 4 hats → ship or `NEEDS_DECISION`.

## Edge cases & failure modes
- CRLF — solved (`.gitattributes` + LF normalization); new tools inherit it.
- Write race — impossible: only Scout commits; Librarian curates serially post-sweep.
- Runaway cost — per-run token budget + hard ceiling; spend logged to trace.
- Prompt injection via raw — content-as-data absolute; raw is never an instruction.
- Partial write — write concept before copying raw (as `keep add` already does).
- Idempotency — re-run on unchanged input = no-op.

## Acceptance criteria
| # | Milestone | Done when |
|---|---|---|
| 1 | Model port | `ask('scout','ping')` returns text; key is a repo secret; gate green |
| 2 | Scout enrich | a dropped file → real cross-linked typed concept, zero manual edits; no fabrication |
| 3 | Librarian | seeded dup detected → merge-proposed → merged; a dead concept lands in `/attic` |
| 4 | Trigger surface | an `ingest` issue produces a committed concept, no terminal |
| 5 | Runtime | all green on Actions, idempotent, within budget |
| 6 | Serve | `keep ask "X"` answers citing real concept IDs; "no data" path works |
| 7 | Continuity | each run writes a `trace`; soul-loop/council invokable by agents |
| 8 | Foreman | a `build` issue runs the 4-hat loop, emits artifact + trace |
| 9 | Corpus | ≥50 real concepts ingested; cold-session amnesia test passes |
| 10 | Lens + obs | graph renders; per-run cost + diff visible |

## Build order
`1 → 2 → 3` is the critical path (model port → Scout → Librarian = a brain that feeds and cleans itself). `4–5` make it driveable, `6–8` sharp, `9` yours, `10` visible. Nothing in 2–10 starts before 1.

## Risks & open decisions (forks)
1. **OpenRouter key + spend** — the one genuine escalation (new credential + cost; standing-orders §6a/§6b). Blocks everything. Adam's move.
2. **Default model per role** — config points scout/librarian at `claude-sonnet-4.6`. Confirm before Scout ships.
3. **Librarian merge mode** — human-confirm until ~50 concepts, then auto. Reversible.

## File manifest (created this phase)
`tools/llm.py` · `tools/scout.py` · `tools/librarian.py` · `tools/foreman.py` · `.github/workflows/{scout,librarian,agent-bus}.yml` · `operating/trace.md`

---

Related: [scout](/operating/scout.md) · [librarian](/operating/librarian.md) · [loop-forge](/operating/loop-forge.md) · [council](/operating/council.md) · [standing-orders](/operating/standing-orders.md) · [howto-ingest](/operating/howto-ingest.md) · [the deed](/DEED.md)
