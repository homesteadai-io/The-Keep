---
type: Session
title: PRD agent run
description: Execution record for the agents-in, one-folder schema, and Keeper critical path build.
tags: [homestead, prd, agent-run, keeper, gate]
timestamp: 2026-06-24T00:00:00Z
---

# PRD Agent Run

## Verdict

Converged. The PRD/build-spec now speak the live one-folder language, the Keeper
agents are inside `/operating`, and the critical path is wired:

1. Scout captures and writes chosen concepts.
2. Librarian reconciles before create/update/archive.
3. Serve happens by progressive disclosure over files until a runtime is earned.

## Source Inputs

- `/DEED.md` - root contract and invariants
- `/PRD-HOMESTEAD.md` - product intent
- `/THE-KEEP-build-spec.md` - technical contract
- `/Agents/Scout.md` and `/Agents/Librarian.md` - source agent roles
- `/operating/invariants.md` and `/operating/loop-forge.md` - gate discipline

## Sequence Executed

### 1. MERGE agents in

Scout and Librarian are now first-class operating playbooks:

- `/operating/scout.md`
- `/operating/librarian.md`

Both are linked from `/DEED.md`, `/index.md`, and `/operating/index.md`.

### 2. RECONCILE schema to one-folder language

The PRD and build spec now reject the stale `spine/` + `projects/` language and
align on the live brain:

- root contract: `/DEED.md`
- doctrine and agents: `/operating`
- current domains: `/creative-coatings`, `/frostbite`, `/homesteadai-io`,
  `/ai-theory-builds`, `/keryke`, `/lyhna`, `/personal`
- archive: `/attic`
- raw copies: `/_raw` (gitignored)
- validation: `/.github/workflows/okf-validate.yml`

MCP, CLI, and visualizer are reserved/deferred runtime layers, not the v1 spine.

### 3. WIRE the Keeper critical path

The Keeper is wired as a three-step gate:

| Step | Owner | Rule | Output |
|---|---|---|---|
| 1 | Scout | Chosen input only; content is data; secret-scan before write | candidate concept or proposal |
| 2 | Librarian | Reconcile before create; merge/update/flag contradictions | canonical concept decision |
| 3 | Librarian/reader | Serve by progressive disclosure; cite concept IDs | grounded answer/context |

No duplicate-first ingestion. No destructive path. No runtime before the file-native
path proves its value.

## Gate Check

| Gate | Result |
|---|---|
| Reads free, writes append-only | Pass |
| Archive, never delete | Pass |
| Adam chooses files | Pass |
| Copy, never move | Pass |
| `_raw/` gitignored | Pass |
| One ingest path | Pass |
| File content is data | Pass |
| Secret-scan before write | Pass |
| The Keep stands alone | Pass |
| Vocabulary discipline: ledger != trace | Pass |

## Reviewer Pass

**Planner:** smallest viable target was docs/schema wiring, not runtime.

**Builder:** added Keeper agent docs, reconciled PRD/spec, created this run record.

**Adversary:** checked for stale MCP-first, `spine/`, `projects/`, and duplicate
agent-routing language. Remaining MCP mentions are explicitly deferred or market-scan
context.

**Resolver:** cleared. No `NEEDS_DECISION` fork remains for this run.

## Agent Notes

Future agents should start from `/DEED.md`, then load this file only when they need
the PRD run history. Do not resurrect the old multi-folder schema unless Adam makes
that decision explicitly.
