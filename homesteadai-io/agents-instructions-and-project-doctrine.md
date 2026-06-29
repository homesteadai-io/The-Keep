---
type: Concept
title: Agents instructions and project doctrine
description: AGENTS instructions and project doctrine are load-bearing handoff surfaces for future agents.
domain: homesteadai-io
status: canonical
confidence: high
source_refs: [/_raw/homesteadai-io/claude-corpus-2026-06-25/agents-instructions-and-project-doctrine-evidence.json]
tags: [homesteadai-io, claude-corpus, phase-2-mine, explored-rejected, contradiction-flag]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Agents instructions and project doctrine

## Verdict

AGENTS instructions and project doctrine are load-bearing handoff surfaces for future agents.

## Durability

- Reconciled source count: 98
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:44bc4bee-effa-4fa3-b828-e97c7e47133b` (chat, 178 msgs): Phase 10 Onboarding — to-approved, and never surfacing for human review. **The diagnostic question is:** does Arlo's `before_tool_call` hook query the `authority_rules` table to resolve the canonical tier for the action_type, or does Arlo's prompt/reasoning determine the tier value it passes to `bind()`? If it's the latter — and given that the tenant agent audit protocol explicitly states "Arlo does NOT build tier/authority/escalation logic — only calls `bind()`" — then the hook is violating the protocol. Arlo sho...
- `chat:5e8e5c32-1de6-4661-80c7-759bfc9bfd22` (chat, 172 msgs): Claude Design to Shopify publishing pipeline — with an explicitly anti-discount, anti-sale positioning modeled after YETI and Liquid Death. Adam prefers executive tone, systems thinking, continuity across sessions (no re-litigating settled decisions), and copy-boxed prompts for Claude Chrome. He delegates execution to Claude Chrome and Claude Code rather than doing UI work himself, and he expects full-scope prompts that close entire tasks rather than partial ones that create future chores. The session addressed cart abandonment as a real-...
- `chat:2addba91-278d-4b3e-ab9b-c9f8bb0d5ad2` (chat, 158 msgs): sdk add ons — surface. He expressed a strong desire to eliminate himself as the manual copy-paste bridge between strategic planning conversations with Claude and execution in Claude Code. The Arlo loop test ran 9 cycles of a 15-task prompt through OpenClaw with the lyhna-gate plugin loaded at priority 1000. The test produced 624 binding events, all verified with correct receipt structure including `receipt_id`, `action_type`, `tier`, `tier_source`, `outcome`, `bound_at`, and `canonical_hash`. A key finding...
- `chat:f3ddfffb-b7bb-4a2c-a7e0-fe93a470bd3e` (chat, 117 msgs): Build A.1-3 , 5.7 — without calling completeTask or blockTask, failure_limit=1) is a required A.4 build component, not optional. Judge model placement was locked: active on subagent Ralph loop iterations, selective on high-stakes subagent handoffs, present in lead agent dream state (L11), and explicitly absent from lead agent conversational turns. Fan-out limits were established as three layers: per-agent iteration budget (default 90 parent / 50 subagent), concurrent subagent fan-out (default 3–5, governor-autho...
- `chat:7d6a3365-ff37-4066-a0b3-966cfca8fb2c` (chat, 106 msgs): Project progress update and next build steps — on the Arlo Inc. multi-model agent platform, operated by Adam (the governor). The session opened with Adam asking Claude to orient from project files and pick up where the previous session ended. Claude read the session handoff documents and surfaced the two available work tracks: Cognition Refresh (Arlo's cognition layer was stale, operating on doctrine from approximately one month prior) and CAP-OBS-006b Provider Drift Monitor. Adam chose to do both in sequence, then expanded scope by notin...
- `chat:94b4df04-26f8-408b-a0c8-4ab8f741e21b` (chat, 86 msgs): Homesteadai.io foundation setup — matter, 30_CANONICAL→domain folders directly, 40_MAPS→`index.md` TOCs, 50_CONTEXT_PACKS→`/context-packs`, 60_RECEIPTS→`/write-logs`, 90_ARCHIVE→`/attic`). Two items are parked on Adam's timeline and must not be raised unprompted: an OpenRouter key file that is untracked but loose in the working tree, and the local clone sitting inside an OneDrive Desktop folder rather than the previously hardened `C:\dev\The-Keep` location. Adam confirmed the home is GitHub regardless of local clone placement...
- `chat:efaad0e3-8cea-4616-8dea-10dac015f8b6` (chat, 83 msgs): TEMPLATE-SPINE v2 write — produced signal to evaluate. Key working patterns: Adam corrected Claude's understanding of how Claude Code operates (it runs as a VPS CLI, has no access to Anthropic project knowledge, requires all context inlined in prompts), corrected present-tense tenant language mid-session, corrected an over-sized Phase 2 deployment prompt (927 lines reduced to 125 lines by removing the inlined spec), and confirmed that all Claude Code deployment prompts must be self-contained copy-paste artifacts rathe...
- `chat:16f56fdf-d3f6-412e-bf40-cb42b6f460be` (chat, 73 msgs): Phase 2a closure and 2b handoff strategy — Phase 2a closure and 2b handoff strategy **Conversation Overview** Adam Holwerda is the sole founder of Lyhna, Inc., building what he describes as "the layer directly below human judgment" — an attestation infrastructure (`bind()`) that produces signed, append-only, offline-verifiable receipts for autonomous agent actions before execution. He operates a three-lane build model: Ada

## Explored / Rejected Signals

- `chat:007a20bc-660b-4eef-95b3-b746222a8d0d`
- `chat:01319aee-30ce-4348-a669-6bb064722609`
- `chat:0e0e04e1-4bb6-4487-9708-a05a5078785a`
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

- Redacted evidence bundle: [/_raw/homesteadai-io/claude-corpus-2026-06-25/agents-instructions-and-project-doctrine-evidence.json](/_raw/homesteadai-io/claude-corpus-2026-06-25/agents-instructions-and-project-doctrine-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
