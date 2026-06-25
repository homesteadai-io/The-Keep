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

## 2026-06-24 — One-folder language set in the briefs
- **Numbered folders retired.** `scout.md` / `librarian.md` now speak the repo's one-folder language only — no `10_INBOX`/`30_CANONICAL`/etc. survive in the tree or the briefs. Map: `10_INBOX`→`/inbox` · `30_CANONICAL`→domain folders directly (no `canonical/` wrapper) · `40_MAPS`→`index.md` TOCs (sweep-built) · `50_CONTEXT_PACKS`→`/context-packs` · `60_RECEIPTS`→`/write-logs` · `90_ARCHIVE`→`/attic`.
- **`20_SOURCES` folded into `_raw` provenance** (decide-and-log): the concept's `resource:` + `sha256` over gitignored `_raw/` is the source record — no separate `/sources` folder (avoids two source stores).
- `/context-packs` and `/write-logs` are canonical paths that materialize on first use (unwritten path = TODO, invariant #12). No empty dirs pre-created, no tooling changed.

---

## 2026-06-24 — Runtime decision: Codex-as-agent (β)
- **Runtime = Codex-as-agent (β), not α.** Codex *is* Scout + Librarian — reads their briefs, works with native file + git on Adam's subscription. No `tools/llm.py`, no OpenRouter, no repo secret in v1; α (OpenRouter) is the deferred portability fallback only.
- **Agents merged into the Keep.** Uploaded agent files (`AGENTS.md`, `soul.md`, `subagents.md`, `Scout.md`, `Librarian.md`) move into `/operating` (UTF-16→UTF-8); OneDrive `Homestead AI.io\Agents` retires to instruction-base-only (no `_raw` leak / git-corruption risk). One brain = `C:\dev\The-Keep`.
- **Schema upgraded, one folder language.** Reconcile concepts to the richer schema (`status`/`confidence`/`contradiction-notes`/`provenance`) in place — migrate old→new, no numbered folders alongside `operating/`/`people/`.
- **`receipt` → `write-log`.** Renamed in the agent files; `receipt` stays sealed for Lyhna. Sealed three hold: ledger · trace · receipt.
- **`_raw` runtime fix.** Scout enrich runs LOCAL (where gitignored `_raw` lives); Actions = mechanical sweep/janitor only; the "commit→Scout-enrich-on-Actions" trigger is deleted. Spec: [prd-agent-run](/operating/prd-agent-run.md).

---

## 2026-06-24 — Tier 1 rulings: Deed slug, escalation tightened
- **Deed org slug corrected (Adam-approved).** [The Deed](/DEED.md) now labels the GitHub org `homesteadai-io` (hyphen) in all three org spans; `homesteadai.io` kept as the brand/domain in prose. First naming carries the line: "GitHub org: `homesteadai-io` · brand: homesteadai.io". Confirmed against the repo-create screen.
- **[standing-orders](/operating/standing-orders.md) tightened.** Optional/reversible **feature** choices → decide and log to this ledger, not escalate. Escalation now reserved for exactly three triggers: (a) spends money · (b) new credential/key/auth dependency · (c) edits the Deed, invariants, or spine.
- **`keep enrich` (LLM concept bodies) — DEFERRED.** Bookmarked in `keep.config.yaml`; not built. Ingestion stays thin/manual (zero new keys) until Adam says otherwise.
- **Findings board — KEEP current-findings style** (overwritten each sweep; history in git). No change, by decision.

---

## 2026-06-24 — Tier 1 closed: autonomy, ingestion, self-report (handoff)
- **Standing Orders ratified.** [standing-orders](/operating/standing-orders.md) — the autonomy mandate: act, run the loop, batch questions, escalate only true forks. The meta-fix against reverting to babysitting.
- **Free gate enforced locally.** `.githooks/pre-commit` runs `tools/checks.py` before every commit (enable: `git config core.hooksPath .githooks`). Branch protection stays **advisory** (free plan) — no upgrade, by decision.
- **Actions off Node 20** (`checkout@v5`, `setup-python@v6`). `keep.config.yaml` documents the enforcement model; nightly cron kept at 08:00 UTC.
- **Sweep reports, not just heals.** Broken-link + dedup flags now land in [log](/operating/log.md) (a current-findings board), surfaced for the Librarian instead of silently swallowed.
- **Ingestion shipped.** `python tools/keep.py add <file>` → secret-scanned, raw copied to `_raw/`, typed OKF stub, reconciled (refuses duplicate title / overwrite). Drop → concept. See [howto-ingest](/operating/howto-ingest.md).
- **Doctrine cross-linked** (Scout Pass B — links only, zero new facts). The brain reads as one fabric.
- **Landing copy grounded.** [homestead](/homestead.md) states only what the Deed supports, in plain language.
- **Reviewed throughout.** Subagent code-review + doctrine-coherence passes ran during the build; all blocking findings fixed (CRLF normalization + `.gitattributes`, `keep add` write-order, skip-dir alignment).
- **Open fork for Adam:** `DEED.md` writes the org as `homesteadai.io` (dotted) in three spots vs the real GitHub org `homesteadai-io`. Left untouched — it's the spine, Adam's to correct.
- **State: idle-and-ready.** No agent running. Drop a file in `/inbox` and run `keep add` to grow the brain.

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
