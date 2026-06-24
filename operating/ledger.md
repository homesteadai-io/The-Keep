---
type: Session
title: ledger
description: Append-only record of Adam's decisions. Newest first. Homestead's word — not a trace, not a receipt.
tags: [doctrine, ledger, decisions, homestead]
timestamp: 2026-06-23T00:00:00Z
---

# ledger.md

The append-only record of **Adam's decisions**. Newest first. This is the *ledger*
(Homestead's word). Loop telemetry is a *trace* (Loop Forge); witnessed proof is a
*receipt* (Lyhna). Never cross them.

---

## 2026-06-24 — Tier 1: self-maintenance live
- **Keepers wired.** `scout.md` (the only writer) + `librarian.md` (curator/server) added to `/operating` and listed in the indexes.
- **Inbox opened.** `/inbox` drop-zone documents the Drop → Scout → Librarian → raw-stays-out flow.
- **Nightly sweep live.** `.github/workflows/nightly-sweep.yml` — pure Python (`tools/sweep.py`), no LLM, no new secrets, `GITHUB_TOKEN` only. Cron 08:00 UTC + manual dispatch. Rebuilds index TOCs (managed `AUTO-INDEX` blocks), link-checks + dedup-flags (warn-only, never auto-merges), re-runs the gate, commits as `github-actions[bot]`. Proven on the runner: run 28076084178 green; bot commit `4aff825` self-healed a deliberately-staled index (idempotent + push path confirmed).
- **Gate unified.** `tools/checks.py` is the single OKF-validate + secret-scan source for both the on-push check and the sweep.
- **Invariant #13 added** (Adam-approved): no-delete protects vault concepts, not local scratch.
- **main protection — NEEDS_DECISION (deferred).** A required-status-check on a *private* repo needs GitHub Team (org `homesteadai-io` is free plan); going public is barred by invariants #5/#10. The janitor still runs green on every push — it just isn't *enforced* as a push gate yet. Awaiting Adam's plan call.

---

## 2026-06-24 — Tier 0 shipped
- **The Keep is live.** homesteadai-io/The-Keep pushed to main, private. Janitor green (run 28074719043).
- **Lyhna confirmed out.** No lyhna/ and no _raw/ in the pushed tree — matches the corrected Deed.
- **Loop ran clean.** Adversary raised a CRLF risk; Resolver verified ground truth (run passed) and killed the false alarm — no noise commit.
- **Decisions:** clone moved out of OneDrive; stale Desktop scaffold retired; commit author = Adam for now, Scout gets a homestead-owned bot identity at Tier 1; Node-20 action bump deferred to Tier 1; main stays direct-push, required janitor-check protection added when Scout lands.

---

## 2026-06-23 — G0: Contract locked

- **Estate named.** Org = `homesteadai-io` (the land). Repo = `The-Keep` (the brain). Visibility: **private**.
- **Where it runs:** GitHub holds the brain (zero-server v1) · OpenRouter is the model port · GitHub Actions is the janitor. No always-on box of our own.
- **Deferred, bookmarked:** Orgo (always-on agent home), MCP query server, pgvector read-accelerator — Tier 2/3, not built.
- **Old stack retired:** Keryke, Chione, Hermes, LiteLLM, Supabase/pgvector dropped from this build.
- **Lyhna excluded:** separate product, not a domain here. Nothing of Lyhna lives in this repo. `receipt` stays its reserved word.
- **Three vocabularies sealed:** `ledger` (Homestead) · `trace` (Loop Forge) · `receipt` (Lyhna).
- **Tool lanes:** Claude Code = infra · Codex = builder/adversary · Cursor = surgical · Adam = merge authority.
- **The Deed ratified** as `/DEED.md` — every agent boots from it.
- **Build order frozen:** Tier 0 (kill amnesia) → 1 (keep alive) → 2 (make sharp) → 3 (see it). Engine before dashboard.

---
