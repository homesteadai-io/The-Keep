---
type: Concept
title: Onboarding and stranger proof
description: Fresh-workspace onboarding and customer-style proof reports recur as Lyhna product evidence.
domain: lyhna
status: canonical
confidence: high
source_refs: [/_raw/lyhna/claude-corpus-2026-06-25/onboarding-and-stranger-proof-evidence.json]
tags: [lyhna, claude-corpus, phase-2-mine, explored-rejected]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Onboarding and stranger proof

## Verdict

Fresh-workspace onboarding and customer-style proof reports recur as Lyhna product evidence.

## Durability

- Reconciled source count: 74
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:6c682278-c07f-4e4e-a2ea-8ceab3a3af74` (chat, 433 msgs): Lyhna Build 3.29 — re the tool runs, the gate failed." Key people: Tim (senior authority for Arlo Inc, needs Telegram setup), Zach (senior authority for Frostbite, needs Telegram setup), Pranger (target enterprise customer for Phase 9-10 onboarding proof). Key product decisions locked this session: "Authorize All" replaces "dangerously allow" as the button label for permissive tier configuration, with subtext "Gate remains active. All actions auto-approve with signed receipts." When Authorize All is active, tie...
- `chat:59bc7fd7-dabf-48b6-a5b5-f84fd2d7e803` (chat, 208 msgs): 4.4 Lyhna Build Phase 9 — policies govern outcomes. Receipts carry `effective_policy`. The entire system built tonight is now running in production. Accept, then paste Step 10 — the Pranger Preflight. This is the integration test that proves a stranger could do this without you in the room. human: im pasted all that i have highlighted assistant: Good. That's the right content — all 12 sub-steps of the Pranger Preflight. But this one says "No code to paste — this is validation." It's a manual walkthrough, not a Claude...
- `chat:4d131bfe-4a19-43b1-878c-88cd2aad4700` (chat, 184 msgs): Project update and bug fix — had hardcoded notification logic in the server code, while the new `tenant_f14b937edc14` tenant had no notification routing. The correct fix was building a `tenant_notification_config` table in Supabase with RLS, wiring onboarding to collect the notification destination (a gap where the UI collected channel type but not destination), and updating the escalation handler to query this table per tenant. After that was deployed and seeded, a second bug was found: the `checkResolutionChain` functi...
- `chat:c75ff313-11b5-489a-bafd-31157121c5b5` (chat, 164 msgs): 5.11 Lyhna Agent Install — may ESCALATE, and that still proves install/enforcement is working Surfaces to inspect: 1. public/docs.html 2. public/sdks.html 3. public/signup.html 4. public/pricing.html 5. public/index.html 6. public/dashboard.html onboarding text 7. README.md 8. lyhna-bind/README.md 9. cli/README.md 10. express-middleware/README.md 11. fastapi-middleware/README.md 12. go-sdk/README.md 13. python-sdk/README.md 14. any @lyhna/setup directory/README/package metadata if present 15. package.json files for pac...
- `chat:85513e36-a8cf-4c82-8ff5-4cd51877b2b0` (chat, 160 msgs): Plugin gate capsule build update — paste-ready blocks, Claude Code as builder, and Codex as adversarial PR reviewer. Adam pastes blocks and makes merge calls but never authors code or commands directly. This session focused on completing Product Gate 1 (stranger-proof install plus self-proving landing page), specifically Checkpoints 6 and 7A: the agent-stranger test loop. A key strategic reframe was settled: the stranger is an agent, not a human, because agents are the actual install persona in the current market. Adam's frami...
- `chat:34a3bf6b-b69d-48f4-89fa-f73b91f9ff19` (chat, 152 msgs): 51826 Lyhna Authority Tier Mapping — y patches, SSL cert issuance **Agent_control tier_1 → tier_2 (7 rows)** — agent/subagent spawning, delegation, memory deletion, skill mutations **tier_2 → tier_3 promotions (6 rows)** — vendor invoice approval, vendor onboarding, refunds, credit memos, package publishing, agent tool access revocation, external invoice send **tier_0 → tier_1 promotions (5 rows)** — code commits, nonprod restart, resume screening, interview scheduling, employee event logging **Additional audit pass (5 rows)** —...
- `chat:5f879ae6-8864-4433-861a-38ce0bcf09dd` (chat, 147 msgs): 4.26 Stage 3 Closed — mapping). Tier source column is correctly populating (`Default (Lyhna)`, `Overridden (Tenant)`, `Unclassified`). Integrity column verifies. This is the post-Phase 10 server-fix surface working correctly. **Images 2–4 — Onboarding Wizard, Step 2 (Authority Posture):** The "Review your authority posture" wizard step is rendering the canonical action registry across `deployment`, `internal_mutation`, and `read_retrieval` domains with the correct default tiers. Tier overrides via dropdown work. E...
- `chat:f9269843-7534-4c5d-be52-d25a94358e22` (chat, 146 msgs): Lyhna Build 3.24 — That is the correct Phase 6 shape. A few parts are especially well-chosen. The scope boundary is disciplined. It keeps Phase 6 to a thin Railway-hosted API plus proof harness, and explicitly excludes dashboard, portal, onboarding, billing, and policy UI. That protects the phase from drifting into “build the company all at once.” The auth model is right. API key resolves tenant and environment server-side, and tenant identity is never caller-asserted. That is exactly the kind of hard boundary...

## Explored / Rejected Signals

- `chat:0376db08-2d30-45c6-982d-e3a23fc24973`
- `chat:0c1c09a9-127c-4936-8f28-ebf1ff606188`
- `chat:147f24e3-ea3d-4953-a08f-aa84806f72b4`
- `chat:246b1b62-02a1-487d-aad9-0a51df2dda3f`
- `chat:27d73bd8-9440-4e10-ad71-68917083891c`
- `chat:34a3bf6b-b69d-48f4-89fa-f73b91f9ff19`
- `chat:35285b24-4da6-48ee-a3c4-6af6cf150ca4`
- `chat:38c2b034-4eaa-4b11-8b6d-47c10111be43`
- `chat:3c669c5d-9a98-4f6b-9bc6-90b3c078499e`
- `chat:3d094fcf-6a68-436e-96ec-989a61cfc0c8`
- `chat:41c74a55-1442-4a59-b5c4-9553fcfd0640`
- `chat:4371864c-cbba-4de2-b3d5-4d8b81d8e731`

## Contradictions / Open Questions

- None flagged in this pass.

## Source Trail

- Redacted evidence bundle: [/_raw/lyhna/claude-corpus-2026-06-25/onboarding-and-stranger-proof-evidence.json](/_raw/lyhna/claude-corpus-2026-06-25/onboarding-and-stranger-proof-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
