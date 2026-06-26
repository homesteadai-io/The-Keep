---
type: Concept
title: Model choice and cost control
description: Model choice interfaces, API costs, and operational cost reduction recur in Keryke builds.
domain: keryke
status: canonical
confidence: high
source_refs: [/_raw/keryke/claude-corpus-2026-06-25/model-choice-and-cost-control-evidence.json]
tags: [keryke, claude-corpus, phase-2-mine, explored-rejected, contradiction-flag]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Model choice and cost control

## Verdict

Model choice interfaces, API costs, and operational cost reduction recur in Keryke builds.

## Durability

- Reconciled source count: 20
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:e8301f3c-9189-4225-9663-937f2ba5f17b` (chat, 287 msgs): 5.17 Keryke Stand-up — alue migrates to packaging, not capacity.** What you sell is design quality: pack coherence, installer reliability, cockpit polish, the agent-pack catalog curation. Compute is the buyer's problem. Anthropic/OpenAI/local-model choice is the buyer's problem. 4. **Margin doesn't compress with usage.** Hosted agent companies get crushed when a power user runs them 16 hours a day on a $39/mo plan. Downloadable artifacts have no usage variance. Price is price. 5. **Distribution scales without infra...
- `chat:62d01fc5-7264-455a-949f-29719089eea3` (chat, 271 msgs): Arlo Web game called "Frostbite HQ" — assistant: Adam is pointing out that the cost table needs to include real platform costs that a social media operation actually incurs - subscription fees for social media management tools, paid ad spend, and any other operational costs beyond just API and hosting.Right. The cost table was only counting Arlo's infrastructure costs. A real social media operation has platform costs too. Here's the complete cost picture: **Platform Subscription Costs** TikTok Business Account is free. But TikTok...
- `chat:00b6a117-2402-45e0-9115-eabd83d63ee2` (chat, 231 msgs): 5.16 Arlo Inc. project onboarding — built. Looking at the patterns, the priority chain maps cleanly across the four packs with no overlap—Memory handles early reads, Cognition builds the prompt, Execution manages tool calls, and Smart Router resolves the model choice. The five sidecars I mentioned earlier all nest into either Cognition or Memory & Retrieval, so each could potentially become its own product rung on the ladder.Mapped it. Kept your wording verbatim on each item. Four packs hold everything; nothing falls outside. #...
- `chat:ec589f76-07d6-4c62-b9ef-8f8527125ed3` (chat, 208 msgs): 4.23 CAP-CON-001 Phase — CLOSED — **Retrieval ranking and relevance scoring.** That is SUB-004 Knowledge Index territory. Projection Discipline says retrieval results must carry atom-IDs; it says nothing about *which* atoms rank higher. 2. **Embedding model choice, vector dimensionality, chunking strategy.** Implementation details of specific capabilities, not doctrine. 3. **Access control and per-tenant scoping.** Already covered by RLS and tenant_id conventions across the platform. Projection Discipline is orthogonal. Proje...
- `chat:bc35cab6-9243-4110-958f-5a5ea5248fea` (chat, 180 msgs): Claw3D visualization layer for Arlo content production — ple talk about things.... i just never needed them assistant: Yes. There are a few levers, and they're worth configuring now before Arlo starts running image generation, cron jobs, and content production — that's when token costs compound. ``` This block is not supported on your current device yet. ``` There are three levers that matter for Arlo, and they should all go into tomorrow's Claude Code session alongside the image skills binder. ## 1. Prompt Caching (Biggest Win) Anthropic's prompt...
- `chat:93aa0ba3-37f5-40a9-a9c3-aedad554214f` (chat, 96 msgs): ChatGPT and Arlo intelligence memory stack — t LIVE. The Claude Code workflow runs by SSHing into VPS root@5.78.206.130, then launching claude from /root/.openclaw on the VPS itself (not running Claude Code locally with remote SSH commands). The person noted that token costs have increased 2-3x recently and attributed it to pre-release throttling ahead of Opus 4.7. The person also noted Claude's hallucination rate has reportedly increased. Key colleagues referenced: ChatGPT as a peer architectural reviewer, Tim Spear as an investor/stak...
- `chat:6c4c7448-230f-4b1c-bb18-fc5f81f7d354` (chat, 52 msgs): Keeping Arlo running autonomously for extended decision-making — ystem prompt that instructs him to autonomously execute a sequence of varied actions—pulling from the registry of available actions and hitting different tiers and types throughout the hour-long run. I'm thinking about token costs too: since each bind() call is just a lightweight API call to Lyhna and not to Claude, the main expense is only when OpenClaw calls Claude. So running an hour of varied prompts should be manageable if Adam's token usage is fixed. The prompt itself should be self-con...
- `chat:561ef607-acec-4124-bba6-b91b7815c1f7` (chat, 28 msgs): Reducing Arlo's operational costs — Reducing Arlo's operational costs **Conversation Overview** This conversation focused on diagnosing and resolving a severe cost overrun with Arlo, an autonomous AI agent running on the OpenClaw platform on a VPS (IP: 5.78.206.130). The person is building a multi-agent AI operation and wants to scale to 2-3 agents ("hires") for Arlo soon, with a second agent

## Explored / Rejected Signals

- `chat:00b6a117-2402-45e0-9115-eabd83d63ee2`
- `chat:561ef607-acec-4124-bba6-b91b7815c1f7`
- `chat:56758d10-8205-4f06-9f3c-8e26e30a4adf`
- `chat:62d01fc5-7264-455a-949f-29719089eea3`
- `chat:6c4c7448-230f-4b1c-bb18-fc5f81f7d354`
- `chat:93aa0ba3-37f5-40a9-a9c3-aedad554214f`
- `chat:9e2efa80-d95f-4213-873c-0181a6484fce`
- `chat:a7cd6a1f-9f66-4d9c-8d28-16c46396e5d6`
- `chat:bc35cab6-9243-4110-958f-5a5ea5248fea`
- `chat:cea3efa9-f926-4ca6-bfd1-2e3744bf9e87`
- `chat:d7314918-5ba8-43d2-81cb-3019c96c1968`
- `chat:db191d79-4029-4868-a9f2-72697bc84916`

## Contradictions / Open Questions

- Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects.
- Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.

## Source Trail

- Redacted evidence bundle: [/_raw/keryke/claude-corpus-2026-06-25/model-choice-and-cost-control-evidence.json](/_raw/keryke/claude-corpus-2026-06-25/model-choice-and-cost-control-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
