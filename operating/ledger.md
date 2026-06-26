---
type: Session
title: ledger
description: Append-only record of Adam's decisions. Newest first. Homestead's word, not a trace.
tags: [doctrine, ledger, decisions, homestead]
timestamp: 2026-06-23T00:00:00Z
---

# ledger.md

The append-only record of **Adam's decisions**. Newest first. This is the *ledger*
(Homestead's word). Loop telemetry is a *trace* (Loop Forge). Source-specific terms
inside a domain stay source content, not Keep doctrine.

---

## 2026-06-25 - Deed reflects parking-lot reality

- **[homestead]** Rewrote `/DEED.md` so The Keep is described as Adam's shared
  OKF shelf for cross-tool context, not a secret-guarding vault or permission
  authority. why: Adam clarified the Keep collects content that already exists
  across Anthropic, OpenAI, and disk; each platform owns its own permissions.
  ref: `/DEED.md`, `/attic/DEED-2026-06-25-fortress-framing.md`

---

## 2026-06-25 - Lyhna and Keeper role correction

- **[homestead]** Lyhna is a separate, active venture with its own codebase,
  sites, and product. Homestead is the OS/context shelf work boots from; The Keep
  holds context about Lyhna as an active project, not as Homestead architecture.
  ref: `/DEED.md`, `/lyhna/lyhna-domain-call.md`
- **[homestead]** Replaced the stale single-writer rule with one ingest path:
  Scout writes new concepts; Librarian reconciles and curates. why: the
  Librarian already merges, normalizes, indexes, and retires, so the honest rule
  is two Keeper roles with different jobs. ref: `/operating/invariants.md`,
  `/operating/scout.md`, `/operating/librarian.md`
- **[homestead]** Retired active "vault" vocabulary in favor of The Brain /
  The Keep. why: Homestead is a readable OS/context brain, not a sealed vault.
  ref: `/THE-KEEP-build-spec.md`

---

## 2026-06-25 - Keryke domain clarification

- **[homestead]** Keryke is its own small-business AI company/library domain in
  The Keep. why: Adam clarified that Keryke is not retired stack residue or a
  sub-bucket under AI theory; it needs its own library path for the Claude corpus
  ingest. ref: `/keryke/index.md`, `/keep.config.yaml`

---

## 2026-06-25 - Step 1: Recon and reconcile

- **[homestead]** Chose the one-folder schema: `/inbox`, `/_raw`, `/write-logs`,
  `/attic`, and six domain folders. why: the actual repo already lives as one OKF
  vault; the numbered folder schema only existed inside built-agent source docs.
  ref: `/operating/recon-2026-06-25.md`
- **[homestead]** Lyhna is an ordinary domain in The Keep. why: Adam explicitly
  ruled it in; the old boundary doctrine would trip booting agents.
  ref: `/DEED.md`
- **[homestead]** Rewired rich Scout/Librarian specs to the one-folder addresses
  without changing their core behavior. why: wire the built agents; do not rebuild
  them as thin stubs. ref: `/operating/scout.md`, `/operating/librarian.md`

---

## 2026-06-25 - Step 2: Skeleton

- **[homestead]** Built the six-domain skeleton: `/creative-coatings`, `/frostbite`,
  `/homesteadai-io`, `/ai-theory-builds`, `/lyhna`, `/personal`. why: Adam ruled
  these are the only active domains for this run. ref: root `/index.md`
- **[homestead]** Created local-only `/inbox` and `/_raw` folders via `.gitignore`.
  why: intake and copied source material must not enter Git by accident.
  ref: `/.gitignore`
- **[homestead]** Archived `/people` to `/attic/people`. why: archive-never-delete
  while removing it from the active domain set. ref: `/attic/people/index.md`

---

## 2026-06-25 - Step 3: Wire Scout

- **[homestead]** Added `python tools/keep.py scout <file>` as the runnable Scout
  intake path. why: Scout must be executable, not just vibes in markdown.
  ref: `/tools/keep.py`
- **[homestead]** Scout now secret-scans before writing, copies raw source into
  ignored `/_raw/<domain>`, hash-verifies the copy, and writes one candidate OKF
  concept to the inferred domain. why: preserve copy-never-move and file-content-is-data.
  ref: `/operating/scout.md`

---

## 2026-06-25 - Step 4: Wire Librarian

- **[homestead]** Added `python tools/keep.py librarian` as the runnable reconciler.
  why: Librarian must rebuild indexes, flag duplicates, archive explicit retirements,
  and write `/write-logs` without becoming an ingester. ref: `/tools/keep.py`
- **[homestead]** Source-deletion retirement is explicit-status-only in v1. why:
  `/_raw` is intentionally local-only, so treating missing raw files as dead sources
  would falsely archive valid concepts in clean clones. ref: `/operating/librarian.md`

---

## 2026-06-25 - Step 5: The Loop

- **[homestead]** Added `python tools/keep.py loop` to sweep `/inbox` through
  Scout, Librarian, inbox clear, and Git commit. why: the Keeper needs a single
  operator entrypoint, not two hand-run half-rituals. ref: `/tools/keep.py`
- **[homestead]** Loop clears `/inbox` only after Scout and Librarian both succeed.
  why: fail-closed beats pretending a dropped file was safely captured.
  ref: `/tools/keep.py`

---

## 2026-06-25 - Step 6: Serve

- **[homestead]** Added `python tools/keep.py serve <query>` as the minimal file-native
  query routine. why: v1 serves by progressive disclosure before MCP or graph earns
  its keep. ref: `/tools/keep.py`
- **[homestead]** Serve loads root/domain indexes first and opens only matching
  concepts. why: never slurp the vault. ref: `/operating/librarian.md`

---

## 2026-06-25 - Step 7: Prove it

- **[homestead]** Ran three real source notes through `/inbox` -> Scout -> Librarian
  -> commit -> serve. why: prove the Keeper path end to end, not just by docs.
  ref: `/operating/proof-2026-06-25.md`
- **[homestead]** Cold-amnesia query answered from vault concepts alone with cited
  concept IDs. why: this is the actual value test. ref: `/tools/keep.py`
- **[homestead]** Fixed two proof bugs: Lyhna domain inference priority and stale
  inbox source references. why: proof should change the system when it catches a
  real break. ref: `/tools/keep.py`, `/lyhna/lyhna-domain-call.md`

---

## 2026-06-23 — G0: Contract locked

- **Estate named.** Org = `homesteadai-io` (the land). Repo = `The-Keep` (the brain). Visibility: **private**.
- **Where it runs:** GitHub holds the brain (zero-server v1) · OpenRouter is the model port · GitHub Actions is the janitor. No always-on box of our own.
- **Deferred, bookmarked:** Orgo (always-on agent home), MCP query server, pgvector read-accelerator — Tier 2/3, not built.
- **Old stack retired:** Keryke, Chione, Hermes, LiteLLM, Supabase/pgvector dropped from this build.
- **Historical note:** Lyhna was previously treated as sealed memory only; this was
  superseded on 2026-06-25 when Adam ruled Lyhna is an ordinary domain.
- **Historical note:** earlier vocabulary seal included `receipt`; current Keep
  doctrine treats source-specific receipt language as data, not architecture.
- **Tool lanes:** Claude Code = infra · Codex = builder/adversary · Cursor = surgical · Adam = merge authority.
- **The Deed ratified** as `/DEED.md` — every agent boots from it.
- **Build order frozen:** Tier 0 (kill amnesia) → 1 (keep alive) → 2 (make sharp) → 3 (see it). Engine before dashboard.

---
