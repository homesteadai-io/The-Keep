---
type: Concept
title: Cold-amnesia proof
description: The Keep is not done until it can answer useful questions from files alone.
domain: homesteadai-io
status: canonical
confidence: high
source_refs: [/_raw/homesteadai-io/claude-corpus-2026-06-25/cold-amnesia-proof-evidence.json]
tags: [homesteadai-io, claude-corpus, phase-2-mine, explored-rejected, contradiction-flag]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Cold-amnesia proof

## Verdict

The Keep is not done until it can answer useful questions from files alone.

## Durability

- Reconciled source count: 103
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:44bc4bee-effa-4fa3-b828-e97c7e47133b` (chat, 178 msgs): Phase 10 Onboarding — thority tiers because agents were self-classifying rather than resolving against a registry, (2) 99.7% of production receipts carrying empty action hashes (SHA-256 of `{}`), and (3) zero governance epochs declared. Four server-side fixes were deployed across three commits (8eed392, 05b795e, 1484480) and a canonical registry resolution update (ae4fd4e): server-side tier resolution from `authority_rules`, real action payload hashing, lowercase normalization, caller tier ignored, `tier_source` a...
- `chat:5e8e5c32-1de6-4661-80c7-759bfc9bfd22` (chat, 172 msgs): Claude Design to Shopify publishing pipeline — ion about ball pythons' diet, so I need to push back where the analysis is actually off-base. The misspelling is a straightforward fix, but I'm running into a constraint with the Shopify MCP tools available to me—I can query data but I'm not sure if I have write access to the theme files where that typo lives. On the price-drop signaling, there's a real tension here. I previously advised against permanent strikethrough for FTC and brand reasons, and I want to stick with that guidance unless s...
- `chat:2addba91-278d-4b3e-ab9b-c9f8bb0d5ad2` (chat, 158 msgs): sdk add ons — orrectness** — Spot-check: `action_type`, `authority_tier`, `outcome`, and `tier_source` should all resolve correctly. `tier_source` should show `authority_rules`, not caller-supplied. 3. **Intent field** — The pending server fix (reject null/non-string/empty/numeric intent) is still undeployed. Watch for any receipt where `intent` looks malformed. Arlo's loop prompt is plain text, so the agent-submitted intent may be verbose or synthetic — flag anything numeric or null. --- **After Loop Comp...
- `chat:f3ddfffb-b7bb-4a2c-a7e0-fe93a470bd3e` (chat, 117 msgs): Build A.1-3 , 5.7 — -knowledge skill and live web checks on Codex (May 2026 changelog) and Claude Code subagents (May 2026 docs). ### 2. JWT / RLS / Supabase — Confirmed Locked Reality I have the canonical pattern committed. Restating to prove it landed and to avoid the recurring agent drift on this surface: - **Three different tenant-context settings live in production. Do not assume cross-table:** - `cost_events` → `request.jwt.claims` (PostgREST-set from JWT) - `cognitive_events` → `app.tenant_id` (app-set) -...
- `chat:7d6a3365-ff37-4066-a0b3-966cfca8fb2c` (chat, 106 msgs): Project progress update and next build steps — with Arlo's tenant isolation posture), and Hermes Checkpoints v2 (risk of two checkpoint paths). A key architectural decision emerged from ChatGPT review and Adam's direction: Arlo stays OpenClaw-carried and identity-preserved with Hermes informing principles only, while Charlie (female voice, operating-chief posture) is built Hermes-native from the start. SOUL.md framing was corrected — Arlo should not narrate substrate updates; the correct framing is "Arlo's identity remains stable while hi...
- `chat:94b4df04-26f8-408b-a0c8-4ab8f741e21b` (chat, 86 msgs): Homesteadai.io foundation setup — `), keeper agent merge (`86462ba`), one-folder schema reconciliation (`b11be85`), and Keeper critical path wiring (`2c7f31b`). The Keeper pipeline is wired in `keep.config.yaml` as `scout_capture → librarian_reconcile → serve_by_files`. All verification passed: OKF validation, stale-schema scan (no old `spine/projects`, no 6-tool MCP contract, no `Lyhna-ai/The-Keep`), and secret-scan clean. The runtime decision locked on Codex-as-agent (β) — Codex IS Scout/Librarian, runs locally where `_raw`...
- `chat:efaad0e3-8cea-4616-8dea-10dac015f8b6` (chat, 83 msgs): TEMPLATE-SPINE v2 write — eployment prompts must be self-contained copy-paste artifacts rather than relying on any external file reads. human: Right. [COGNITION.md]([URL] v1.4 is live on disk. [SOUL.md]([URL] v1.3 was preserved (mtime confirmed). Both identity files now match what we authored today. Here's where we stand and what's next. Status Artifact Status [SOUL.md]([URL] v1.3 ✅ Live on disk, injecting Core Identity per turn [COGNITION.md]([URL] v1.4 ✅ Live on disk, durable reference [TEMPLATE-SPINE.md]([URL] v1.2...
- `chat:16f56fdf-d3f6-412e-bf40-cb42b6f460be` (chat, 73 msgs): Phase 2a closure and 2b handoff strategy — every `bind()` inside a loop without touching the frozen four-field contract? The caller can't add a fifth field. So the loop association either rides inside the payload (and thus the `action_hash`) or happens through a server-side loop session — and which one it is has to be discovered, not assumed. That makes 2b Step 0 real discovery work, plus a build, plus a likely Codex review cycle, plus a live fire, plus a Supabase confirm. That's the same weight as the full 2a arc I just ran. The fail...

## Explored / Rejected Signals

- `chat:007a20bc-660b-4eef-95b3-b746222a8d0d`
- `chat:01319aee-30ce-4348-a669-6bb064722609`
- `chat:05e34f2c-3b55-4fd2-a586-ecc85092e38e`
- `chat:0fd33c67-81da-4e02-9cfd-bed1d32e15c2`
- `chat:13b9f98d-7dd8-4b76-84cc-c1ea64bd8cc6`
- `chat:16f56fdf-d3f6-412e-bf40-cb42b6f460be`
- `chat:1ce0016c-48c0-4dbf-b9af-1f75bb3f6cc5`
- `chat:1cebcce5-5e64-40c0-a3ea-19407741ce9d`
- `chat:1e0adbf2-98c1-4f85-b98e-3affd2e6cf32`
- `chat:1ff3ce3e-f636-404f-8ed2-6e526399b0b7`
- `chat:20259a7e-d8a7-40a5-8dd0-d07337ef7e26`
- `chat:2034cbd1-19fa-432f-8b31-9b82a3e29d92`

## Contradictions / Open Questions

- Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.

## Source Trail

- Redacted evidence bundle: [/_raw/homesteadai-io/claude-corpus-2026-06-25/cold-amnesia-proof-evidence.json](/_raw/homesteadai-io/claude-corpus-2026-06-25/cold-amnesia-proof-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
