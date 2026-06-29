---
type: Concept
title: Lyhna integration as consumer
description: Keryke uses Lyhna as a witness/integration layer without making Lyhna the room or product owner.
domain: keryke
status: canonical
confidence: high
source_refs: [/_raw/keryke/claude-corpus-2026-06-25/lyhna-integration-as-consumer-evidence.json]
tags: [keryke, claude-corpus, phase-2-mine, explored-rejected, contradiction-flag]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Lyhna integration as consumer

## Verdict

Keryke uses Lyhna as a witness/integration layer without making Lyhna the room or product owner.

## Durability

- Reconciled source count: 321
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:42ef0213-0ca2-4839-a117-128c1fd03a30` (chat, 433 msgs): 5.23 MCP Proxy Adapter — 5.23 MCP Proxy Adapter **Conversation Overview** Adam Holwerda, founder and sole operator of Lyhna, spent a full day (approximately noon to 6pm) in a long-running session building, verifying, and deploying the MCP proxy adapter — the eighth distribution surface for Lyhna's `bind()` gate. Adam works with two Codex agents (one pointed at the `lyhna-mcp-proxy` repo on his Windows desktop, one on the Keryke VPS where the live agent Chione runs) and uses
- `chat:9428c065-a022-4664-a8db-5bc9498348b7` (chat, 365 msgs): Arlo Inc v.0.3 progress update — Arlo Inc v.0.3 progress update **Conversation overview** Adam Holwerda is the founder of Lyhna Inc, a company building execution authority infrastructure for AI systems. The core primitive is `bind()` — a pre-execution gate that returns signed Ed25519 receipts (`LyhnaReceiptV2`) proving actions were evaluated under a specific authority structure before execution. The session was a full-day (~15 hour) engineering sprint completing four major ship
- `chat:bdecb6fd-c59d-4160-b2f4-34093899a7a0` (chat, 306 msgs): Arlo/Lyhna first tenant — Arlo/Lyhna first tenant **Conversation Overview** Adam is building Arlo Inc, an AI-powered venture incubator operating across multiple business divisions. His primary agent is Arlo, running on OpenClaw (an open-source AI orchestration framework) deployed on a VPS at root@5.78.206.130. Arlo's first active division is Frostbite Feeders, a reptile feeder e-commerce
- `chat:e8301f3c-9189-4225-9663-937f2ba5f17b` (chat, 287 msgs): 5.17 Keryke Stand-up — 5.17 Keryke Stand-up **Conversation Overview** Adam Holwerda is the founder of Keryke (an AI agent platform), Dolios (his personal tenant), and co-founder of Lyhna (a pre-execution authority service for autonomous agents). He also operates Creative Coatings (a manufacturing business) and Frostbite Feeders. His working pattern involves approximately 8-10 hours daily with Claude, using parallel agent workflows across multiple chat windows, a Windows desktop running Codex as lead engineer, a VPS...
- `chat:62d01fc5-7264-455a-949f-29719089eea3` (chat, 271 msgs): Arlo Web game called "Frostbite HQ" — Web game called "Frostbite HQ" **Conversation Overview** This was a comprehensive working session with Adam Holwerda, founder of both Frostbite Feeders (a frozen feeder rodent business based in Fort Wayne, Indiana) and Lyhna (an AI governance infrastructure company). Adam is building a social media growth experiment called the "Frostbite AI Employee Program" — deploying a named AI agent called Arlo to grow Frostbite Feeders' social media presence, with the agent's journey serving as the conte...
- `chat:e8eace00-570f-4706-966e-4df3293462c4` (chat, 270 msgs): Arlo inc Layer 1 infrastructure — ng through them sequentially. He also issued a firm scope boundary directive: Claude's scope is Arlo Inc. infrastructure only (OpenClaw, LiteLLM, SOUL.md, skill files, Arlo's Supabase instance), with zero involvement in Lyhna — a separate company where Arlo is a customer, not a co-development partner. The session completed the following: Docker consolidation of LiteLLM and Langfuse into a shared network at /opt/arlo-infra with nine healthy containers; OpenRouter account creation and API key d...
- `chat:d2b90e40-ca89-4feb-9156-9902bd8885a1` (chat, 263 msgs): Keryke.oi Founding Docs — Phone… You don't have to buy the computer to get the phone." This triggered a complete rewrite of the portfolio architecture into seven distinct, independently shippable products: Keryke (desktop cockpit, $29–$109/mo), Lyhna Authority Layer (already shipping at lyhna.com), Cost Observatory (standalone web SaaS), Companion Shell (a vertical product line), Whiteboard (standalone thinking surface), Hermes Plugin Marketplace, and Hermes Hosted (managed runtime). Each product has its own audience,...
- `chat:9ccc13bc-a817-4fad-a8b6-154defcf29ca` (chat, 260 msgs): Receipt capture app for Frostbite accounting integration — M already running at the existing gateway. This is NOT an Arlo platform feature — it's a tenant-scoped app proving the isolation model. **Scope discipline**: This app is strictly Frostbite tenant work. Do not reference Lyhna. Do not touch OpenClaw core. Do not modify the capability registry. Build a standalone app that consumes the existing infrastructure. ### Deliverables Build three components under `/root/tenants/frostbite/`: ``` /root/tenants/frostbite/ ├── api/ Node.js Express API (VPS s...

## Explored / Rejected Signals

- `chat:00b6a117-2402-45e0-9115-eabd83d63ee2`
- `chat:063edfc0-8a20-46c0-9a84-b0190f559290`
- `chat:0757cfd3-8d82-4f2d-83f6-978cdca365db`
- `chat:082835be-006f-43ae-8ac9-31a6757deded`
- `chat:08e609d8-1cee-42ca-9827-e823c676aa21`
- `chat:09ad58de-144d-4a6c-a071-802256642148`
- `chat:0cad6316-f166-422a-8d38-a74fceac2092`
- `chat:0cece6f6-3344-4c96-bc12-ea3ac4ce44c9`
- `chat:11f03bd0-1f6a-4bee-a6c4-b5472488b92d`
- `chat:129bf6f5-df0c-47f2-85f1-87dd902e9aaf`
- `chat:12c867ef-47e8-4223-b9bf-a09c60067103`
- `chat:139aca3c-b465-4b05-9afb-2f586f7b2d6f`

## Contradictions / Open Questions

- Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects.
- Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.

## Source Trail

- Redacted evidence bundle: [/_raw/keryke/claude-corpus-2026-06-25/lyhna-integration-as-consumer-evidence.json](/_raw/keryke/claude-corpus-2026-06-25/lyhna-integration-as-consumer-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
