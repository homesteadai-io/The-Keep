---
type: Session
title: PR register - Keep corpus ingest and doctrine correction
description: Draft pull-request register for the current Homestead Keep state after Claude corpus ingest, reconciliation, and Lyhna/Keeper role corrections.
tags: [homestead, keep, pr-register, claude-corpus, doctrine]
timestamp: 2026-06-26T00:00:00Z
---

# Draft PR: Register Keep Corpus Ingest and Doctrine Correction

## PR Title

`[codex] Register Keep corpus ingest and doctrine correction`

## Status

Draft register only. This checkout has no Git remote configured, so no GitHub PR was opened from this machine.

Current branch: `main`

## Summary

This registers the current Keep state after the Claude corpus import loop, domain routing cleanup, full mining/reconciliation pass, and the follow-up doctrine correction around Lyhna and Keeper write roles.

The important correction: Homestead is not Lyhna. Lyhna is a separate, active venture with its own codebase, sites, and product. The Keep holds context about Lyhna as a tenant/project lane; it is not built out of Lyhna architecture.

The second correction: Scout is not the only writer in reality. Scout is the single ingest path for new concepts. Librarian reconciles, curates, indexes, and retires. Two Keeper roles; different jobs.

## What Changed

- Added Keryke as its own domain/library lane for small-business AI context.
- Preserved Lyhna as its own active project context lane, not Homestead architecture.
- Routed and mined the Claude export into seven domains:
  - `creative-coatings`
  - `frostbite`
  - `homesteadai-io`
  - `ai-theory-builds`
  - `keryke`
  - `lyhna`
  - `personal`
- Reduced the needs-decision pile before mining by strengthening routing signals.
- Mined and reconciled concepts across the tightened manifest.
- Rebuilt indexes and write logs.
- Updated doctrine from "single writer" to "one ingest path."
- Retired active "vault" vocabulary in favor of The Brain / The Keep where it governed current behavior.
- Updated proof/recon/miner language so old Lyhna framing does not keep resurfacing as live doctrine.

## Key Files

- `/DEED.md` - current boot contract and Lyhna boundary correction.
- `/THE-KEEP-build-spec.md` - technical contract, domain list, Safety Spine, and Brain wording.
- `/operating/invariants.md` - one ingest path and Lyhna separate-project invariant.
- `/operating/scout.md` - Scout as ingest writer for new concepts.
- `/operating/librarian.md` - Librarian as reconciler/curator/server.
- `/operating/ledger.md` - decision record for Keryke and Lyhna/Keeper role correction.
- `/operating/claude-corpus-phase2-3-report-2026-06-25.md` - mining and reconciliation report.
- `/operating/claude-corpus-routing-manifest-2026-06-25.md` - tightened routing manifest.
- `/tools/claude_export_phase1_route.py` - corpus router.
- `/tools/claude_export_mine_reconcile.py` - corpus miner/reconciler.
- Domain concept files under `/creative-coatings`, `/frostbite`, `/homesteadai-io`, `/ai-theory-builds`, `/keryke`, `/lyhna`, and `/personal`.

## Results To Preserve

Phase 1.5 tightened manifest:

| Domain | Chats | Concepts/docs |
|---|---:|---:|
| creative-coatings | 68 | 14 |
| frostbite | 101 | 21 |
| homesteadai-io | 113 | 9 |
| ai-theory-builds | 84 | 1 |
| keryke | 256 | 139 |
| lyhna | 158 | 138 |
| personal | 36 | 0 |
| needs-decision | 25 | n/a |
| skip-noise | 120 | n/a |

Phase 2/3/4:

- Concepts mined in Phase 2/3: 73.
- Total concepts after reconcile: 76.
- Skip-noise checked: 120.
- Skip-noise rescued: 1.
- Cold-amnesia test: pass.
- Keryke question: pass.
- Frostbite question: pass.
- Lyhna question: pass.

## Validation

Latest checks run:

```powershell
python tools\keep.py librarian
python -m py_compile tools\keep.py tools\claude_export_mine_reconcile.py tools\claude_export_phase1_route.py
rg -n "ordinary domain|ordinary raw|old lyhna boundary|not special plumbing|only writer|single writer|Scout only writer|whole vault|the vault|THE VAULT|Answer from vault|Reconciled Vault|producer and only writer" DEED.md THE-KEEP-build-spec.md index.md keep.config.yaml tools operating lyhna -g "*.md" -g "*.py" -g "*.yaml" -g "*.json"
```

Results:

- Librarian rebuild passed: no duplicates or explicit archive markers.
- Python compile passed.
- Stale phrase sweep returns only historical ledger receipts and the miner's contradiction detector for old source phrasing.

## Known Non-PR State

- No Git remote is configured, so this is not yet a real GitHub pull request.
- The working tree is intentionally mixed: tracked doctrine/tool/index changes plus many untracked mined concept files and local artifacts.
- Do not blindly `git add -A`; the PR scope needs explicit staging when a remote is added.
- Historical ledger entries still mention older Lyhna/vault language as receipts. The newer correction entry supersedes them rather than rewriting history.

## Suggested Commit Message

```txt
Register Keep corpus ingest and doctrine correction
```

## Suggested PR Body

```md
## Summary

Registers the Keep after the Claude corpus ingest, domain routing cleanup, mining/reconciliation pass, and doctrine correction.

Key corrections:
- Lyhna is a separate active venture, not Homestead architecture.
- Keryke is its own small-business AI domain/library lane.
- Scout is the single ingest path for new concepts; Librarian reconciles and curates.
- Current doctrine uses The Brain / The Keep language instead of active vault framing.

## Validation

- `python tools\keep.py librarian`
- `python -m py_compile tools\keep.py tools\claude_export_mine_reconcile.py tools\claude_export_phase1_route.py`
- Stale phrase sweep verified current doctrine is clean; remaining matches are historical ledger receipts or contradiction detection for old source phrasing.

## Notes

This PR should stage only the intended Keep corpus/doctrine files. The checkout currently contains unrelated/local artifacts, so avoid blanket staging.
```
