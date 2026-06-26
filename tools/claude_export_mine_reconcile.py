#!/usr/bin/env python3
"""Phase 2/3 miner for Adam's Claude export.

This is a Scout-shaped batch path: it reads every routed chat/doc full text,
clusters repeated signals into durable concepts, writes concept files, writes
redacted local evidence bundles under /_raw, and leaves reconciliation/reporting
artifacts for the Librarian.
"""

from __future__ import annotations

import collections
import datetime as dt
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

import claude_export_phase1_route as router


ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "Anthropic Claude Chat Corpus .zip"
MANIFEST = ROOT / "operating" / "claude-corpus-routing-manifest-2026-06-25.json"
REPORT = ROOT / "operating" / "claude-corpus-phase2-3-report-2026-06-25.md"
RAW_ROOT = ROOT / "_raw"
NOW = "2026-06-25T00:00:00Z"

SECRET_PATTERNS = router.SECRET_PATTERNS
URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)


THEMES = [
    # Creative Coatings
    ("creative-coatings", "masked-parts-production-sheets", "Masked parts production sheets", "Daily masked-parts worksheets need consistent formatting, summary rows, and usable production views.", ["masked parts", "part #", "paint color", "tool used", "pax", "spring", "worksheets", "sheet formatting"]),
    ("creative-coatings", "powder-line-inventory-and-ordering", "Powder line inventory and ordering", "Powder-coat inventory, mapping, ordering, and daily tracking are a recurring operating system need.", ["powder line", "powder coat inventory", "daily powder", "inventory and mapping", "ordering"]),
    ("creative-coatings", "photo-to-sheet-data-extraction", "Photo-to-sheet data extraction", "Photos need to become structured sheet rows with customer, part, paint color, quantity, and tool fields.", ["photos data", "google sheets", "customer", "paint color", "quantity", "tool used"]),
    ("creative-coatings", "quote-and-part-audit", "Quote and part audit trail", "Quote and part-audit work needs retrievable source context instead of scattered one-off asks.", ["quote part audit", "quote", "audit", "part audit"]),
    ("creative-coatings", "rework-log-visual-document", "Rework log visual document", "The rework log should become a workable visual document rather than a raw file pile.", ["rework log", "visual document", "workable visual"]),
    ("creative-coatings", "creative-metrics-review", "Creative metrics review", "Creative Coatings metrics and monthly numbers recur as digest/review material.", ["creative metrics", "creative feb", "creative numbers", "february 2026 creative"]),
    ("creative-coatings", "drive-folder-operating-setup", "Drive folder operating setup", "Google Drive/project folders are part of the Creative Coatings operating workflow.", ["google drive project", "project/folder setup", "project folders", "knowledge and creative core"]),
    ("creative-coatings", "daily-raw-to-finished-document-flow", "Daily raw-to-finished document flow", "Daily raw inputs need a repeatable conversion into finished operational documents.", ["raw form", "finished form", "daily drop", "daily file conversion"]),
    ("creative-coatings", "state-column-and-sheet-cleanup", "State column and sheet cleanup", "Spreadsheet cleanup work includes filling state initials and standardizing operational sheets.", ["state with the initials", "fill in the column", "spreadsheet", "sheets"]),
    ("creative-coatings", "labor-cap-complexity", "Labor cap complexity", "The labor-cap idea grew beyond a simple cap into a multi-step implementation problem.", ["labor cap", "cap l1", "cap l1-4", "longer time than the cap"]),

    # Frostbite
    ("frostbite", "company-status-and-financial-model", "Company status and financial model", "Frostbite planning repeatedly turns on company status, gross profit, sales targets, and capacity economics.", ["company status", "financial overview", "gross profit", "financial plan", "sales targets", "full capacity", "wholesale operation financial"]),
    ("frostbite", "inventory-freezer-and-sku-control", "Inventory, freezer, and SKU control", "Freezer inventory, SKU counts, sizes, and dropdown consistency are central Frostbite operating memory.", ["freezer inventory", "inventory organization", "sku", "product counts", "dropdown", "show inventory", "inventory status"]),
    ("frostbite", "rat-breeding-production-capacity", "Rat breeding production capacity", "Breeding capacity, litter survivability, bins, growout, and rack layouts drive Frostbite supply planning.", ["rat breeding", "litter", "bins", "growout", "super rack", "production capacity", "rats weekly"]),
    ("frostbite", "packout-processing-and-equipment", "Packout processing and equipment", "Packout lines, flow wrappers, weighing/sorting, chillers, dry ice, and equipment choices recur as operational constraints.", ["packout", "flowwrapper", "flow wrapper", "weight sorter", "weighing", "plate chiller", "dry ice", "processing equipment"]),
    ("frostbite", "cold-chain-and-shipping-model", "Cold chain and shipping model", "Cold chain reporting, free shipping theory, containers, and box sizing are recurring Frostbite logistics decisions.", ["cold chain", "shipping model", "free shipping", "box size", "custom colored shipping boxes", "gaylord", "shipping large orders"]),
    ("frostbite", "website-shopify-and-catalog", "Website, Shopify, and catalog", "Frostbite website, Shopify, catalog, checkout, product listings, and landing pages are recurring build surfaces.", ["frostbite website", "shopify", "checkout", "landing page", "product catalog", "product listings", "website build"]),
    ("frostbite", "klaviyo-marketing-and-dtc", "Klaviyo, marketing, and DTC", "Klaviyo, social media, DTC positioning, geo-targeting, and Gen Z reptile culture recur as growth levers.", ["klaviyo", "marketing", "dtc", "social media", "geo-targeting", "gen z reptile", "cold email"]),
    ("frostbite", "pricing-and-size-architecture", "Pricing and size architecture", "Pricing, gram-weight sizing, SKU sizes, and customer/order analysis are durable Frostbite pricing concerns.", ["pricing", "gram weight", "sizing", "price breakdown", "rat pricing", "mice", "pinkies"]),
    ("frostbite", "show-and-booth-operations", "Show and booth operations", "Show inventory, booth photography, show sales breakdowns, and event loops recur as Frostbite field operations.", ["show booth", "show inventory", "show sales", "sales event", "booth photography"]),
    ("frostbite", "facility-buildout-and-winterspine", "Facility buildout and Winterspine", "Temporary buildings, Winterspine, growout buildings, HVAC, and facility buildout are repeated capacity themes.", ["winterspine", "temporary building", "buildout", "hvac", "building plans", "facility"]),
    ("frostbite", "breeder-feeder-management-app", "Breeder and feeder management app", "Frostbite spawned app ideas for breeder/feeder calculators, rodent management, and operating workflows.", ["breeder", "feeder calc", "rodent and snake breeder", "frostbite app", "frostbite flow"]),
    ("frostbite", "competitor-and-market-research", "Competitor and market research", "Competitor websites, prize breakdowns, feeder-market summaries, and research-animal pricing recur as market intelligence.", ["competitor", "market", "layne labs", "research animals", "frozen rodent feeder market"]),

    # Homestead
    ("homesteadai-io", "keep-deed-and-domain-spine", "The Keep deed and domain spine", "Homestead uses The Deed, domain folders, and OKF files as the shared memory substrate.", ["the keep", "deed", "domain", "okf", "homestead", "one-folder"]),
    ("homesteadai-io", "scout-librarian-keeper-loop", "Scout, Librarian, and Keeper loop", "Scout and Librarian roles define how chosen source material becomes reconciled Keep memory.", ["scout", "librarian", "keeper", "write-log", "inbox", "raw copies"]),
    ("homesteadai-io", "claude-corpus-ingest", "Claude corpus ingest", "The Claude export becomes the 80 percent memory recovery job feeding the Keep.", ["claude export", "claude corpus", "conversations.json", "phase 1", "phase 2", "ingest"]),
    ("homesteadai-io", "local-codex-agent-operations", "Local Codex agent operations", "Running multiple local Codex agents, cost, setup, and project-window handoffs recur as Homestead operating concerns.", ["codex agents", "local codex", "running local codex", "project window", "codex guide"]),
    ("homesteadai-io", "agents-instructions-and-project-doctrine", "Agents instructions and project doctrine", "AGENTS instructions and project doctrine are load-bearing handoff surfaces for future agents.", ["agents.md", "agent instructions", "instructions", "handoff", "prompt"]),
    ("homesteadai-io", "soul-loop-and-council-reasoning", "Soul Loop and Council reasoning", "Soul Loop and Council doctrine preserve reasoning quality across agents.", ["soul loop", "council", "bengio", "hopfield", "pearl", "hassabis"]),
    ("homesteadai-io", "openrouter-model-port", "OpenRouter model port", "OpenRouter is the model-port abstraction for swapping models without moving the brain.", ["openrouter", "model port", "model choice", "claude opus", "gpt-5"]),
    ("homesteadai-io", "cold-amnesia-proof", "Cold-amnesia proof", "The Keep is not done until it can answer useful questions from files alone.", ["cold-amnesia", "prove it", "serve", "proof", "query"]),
    ("homesteadai-io", "zero-server-git-native-architecture", "Zero-server git-native architecture", "Homestead favors files, Git, and no unnecessary runtime until the file-native path earns trust.", ["zero-server", "git", "github actions", "no server", "file-native"]),
    ("homesteadai-io", "prompt-and-handoff-artifacts", "Prompt and handoff artifacts", "Prompt-ready operational handoffs are a recurring Homestead artifact style.", ["prompt", "handoff", "paste-ready", "operator", "restart prompt"]),

    # AI Theory Builds
    ("ai-theory-builds", "frontier-model-and-keynote-intelligence", "Frontier model and keynote intelligence", "Keynotes, frontier model launches, and competitive AI model analysis form a repeated market-intelligence lane.", ["nvidia keynote", "keynote speech", "gpt-5", "claude opus", "competitive analysis", "ai arms race"]),
    ("ai-theory-builds", "observability-and-evaluation-science", "Observability and evaluation science", "Agent observability, model evaluation, and evaluation science recur as durable theory/build topics.", ["observability", "evaluation science", "model eval", "agent evaluation", "eval"]),
    ("ai-theory-builds", "agentic-workflow-automation", "Agentic workflow automation", "Workflow automation, long-horizon tasks, and agentic systems are recurring build-theory material.", ["workflow automation", "long-horizon", "agentic", "agents", "task completion"]),
    ("ai-theory-builds", "ai-business-idea-fusion", "AI business idea fusion", "AI business ideas are explored, combined, ranked, and sometimes rejected as product directions.", ["unicorn idea", "idea fusion", "business ideas", "product ideas", "which ones you would actually do"]),
    ("ai-theory-builds", "naming-and-positioning-lab", "Naming and positioning lab", "Distinctive one-word names and positioning experiments recur as product-formation work.", ["distinctive single-word", "product name", "made-up word", "easy to pronounce", "naming"]),
    ("ai-theory-builds", "smart-home-and-computer-products", "Smart home and computer products", "SmartHome, Home Assistant, and computer-product explorations are routed into AI theory builds unless tied to Keryke.", ["smart home", "smarthome", "home assistant", "computer products"]),
    ("ai-theory-builds", "ai-university-video-archive", "AI University video archive", "AI video transcripts and research archives are recurring learning and archive assets.", ["ai university", "youtube video", "video transcript", "video concepts", "research archive"]),
    ("ai-theory-builds", "managed-agents-and-platform-apis", "Managed agents and platform APIs", "OpenAI/Anthropic managed agents and platform APIs recur as reference architectures.", ["managed agents", "openai agents", "anthropic managed agents", "agents sdk"]),
    ("ai-theory-builds", "research-transcript-digestion", "Research transcript digestion", "Transcript digestion, synthesis, and presentation work recur as a general AI research workflow.", ["transcript", "digest", "presentation", "research", "summarize"]),
    ("ai-theory-builds", "neural-prediction-and-world-models", "Neural prediction and world models", "Neural prediction, world models, and Meta TRIBE-style concepts are recurring theory signals.", ["neural prediction", "tribe v2", "meta's tribe", "world model"]),

    # Keryke
    ("keryke", "keryke-company-lineage", "Keryke company lineage", "Keryke is the small-business AI company/library domain that absorbed the former Arlo lineage.", ["keryke", "arlo inc", "company name alternatives", "founding docs", "small business ai"]),
    ("keryke", "arlo-architecture-and-buildout", "Arlo architecture and buildout", "Arlo architecture, onboarding, infrastructure layers, and build phases are the dominant Keryke source lineage.", ["arlo architecture", "arlo inc", "arlo build", "layer 1 infrastructure", "onboarding", "phase"]),
    ("keryke", "talaria-browser-os", "Talaria browser OS", "Talaria and browser/super-app surfaces form a Keryke product/library lane.", ["talaria", "browser os", "browser super app", "desktop cockpit"]),
    ("keryke", "tabula-and-chione-lineage", "Tabula and Chione lineage", "Tabula and Chione appear as Keryke lineage/product infrastructure rather than active Homestead stack.", ["tabula", "chione", "chione hermes", "tabula testing"]),
    ("keryke", "crimson-desert-companion", "Crimson Desert companion", "Crimson Desert companion work is a Keryke product lane tied to corpus, guide, marketplace, and agent builds.", ["crimson desert", "game guide", "companion", "marketplace"]),
    ("keryke", "room-spine-and-repurposing-room", "Room spine and Repurposing Room", "Room spine, room-door, and Repurposing Room work are durable Keryke workflow architecture.", ["room spine", "room-door", "repurposing room", "1st room", "rooms"]),
    ("keryke", "small-business-ai-operator-substrate", "Small-business AI operator substrate", "Keryke repeatedly frames an operator substrate for small-business AI products and workflows.", ["small business ai", "operator-substrate", "operator substrate", "company infrastructure"]),
    ("keryke", "agent-observability-and-runaway-prevention", "Agent observability and runaway prevention", "Keryke work repeatedly needs observability, runaway prevention, and agent control surfaces.", ["agent observability", "runaway prevention", "approval workflow", "agent stack"]),
    ("keryke", "memory-second-brain-and-obsidian", "Memory, second brain, and Obsidian", "Keryke carries second-brain, Obsidian, and memory-system experiments as product infrastructure.", ["second brain", "obsidian", "memory architecture", "persistent memory"]),
    ("keryke", "voice-avatar-and-interface-identity", "Voice, avatar, and interface identity", "Arlo/Keryke interface identity includes voice, animated avatar, visual village, and agent presence.", ["arlo voice", "animated avatar", "visual village", "silver fox", "voice match"]),
    ("keryke", "model-choice-and-cost-control", "Model choice and cost control", "Model choice interfaces, API costs, and operational cost reduction recur in Keryke builds.", ["model choice", "token costs", "operational costs", "reducing arlo's operational costs"]),
    ("keryke", "vps-and-local-infrastructure", "VPS and local infrastructure", "VPS, old laptop, Supabase-era infrastructure, and local setup recur as Keryke deployment concerns.", ["vps", "old laptop", "supabase", "infrastructure updates", "running autonomously"]),
    ("keryke", "lyhna-integration-as-consumer", "Lyhna integration as consumer", "Keryke uses Lyhna as a witness/integration layer without making Lyhna the room or product owner.", ["lyhna", "bind", "first tenant", "lyhna reinstallation", "pocket lyhna"]),
    ("keryke", "frostbite-hq-bleed-boundary", "Frostbite HQ bleed boundary", "Some Arlo/Keryke game or build chats mention Frostbite, but title and architecture point to Keryke.", ["frostbite hq", "arlo web game", "persistent memory setup for arlo build"]),

    # Lyhna
    ("lyhna", "axlio-origin-and-value", "Axlio origin and value", "Axlio belongs with Lyhna and appears in naming, value, system-design, and professor-discussion threads.", ["axlio", "insigel", "taking axlio", "monetary value"]),
    ("lyhna", "witness-and-proof-layer", "Witness and proof layer", "Lyhna is repeatedly framed around witness, proof, claimed-vs-actual, and evidence-bound continuation.", ["witness", "proof", "claimed-vs-actual", "evidence", "proof packet"]),
    ("lyhna", "bind-and-mcp-surface", "Bind and MCP surface", "Lyhna bind/MCP appears as the operational interface for proof and governed continuation.", ["bind", "@lyhna", "lyhna mcp", "mcp proxy"]),
    ("lyhna", "tenant-authority-and-core-rules", "Tenant authority and core rules", "Tenant authority rules, canonical registries, and tier/protection logic recur in Lyhna core work.", ["tenant authority", "canonical", "tier", "protect", "dolios"]),
    ("lyhna", "tas-sync-brief-and-proof-projects", "TAS, sync brief, and proof projects", "Sync briefs, TAS specs, and proof-layer project docs are core Lyhna material.", ["tas", "sync brief", "proof-layer", "proof layer"]),
    ("lyhna", "loop-forge-governed-loop", "Loop Forge governed loop", "Loop Forge material ties to Lyhna through governed-loop proof, oscillation termination, and witness discipline.", ["loop-forge", "oscillation", "governed loop", "termination"]),
    ("lyhna", "handoff-and-continuation", "Handoff and continuation", "Lyhna value clusters around evidence-bound handoff, continuation, and witnessed task memory.", ["handoff", "continuation", "session handoff", "customer report"]),
    ("lyhna", "memory-provenance-not-generic-second-brain", "Memory provenance, not generic second brain", "Lyhna should stay on provenance/witness truth rather than drifting into a generic second brain.", ["provenance", "not generic", "second brain", "witness data"]),
    ("lyhna", "onboarding-and-stranger-proof", "Onboarding and stranger proof", "Fresh-workspace onboarding and customer-style proof reports recur as Lyhna product evidence.", ["onboarding", "stranger", "customer report", "fresh workspace"]),
    ("lyhna", "lyhna-project-context-lane", "Lyhna project context lane", "Lyhna is a separate active venture; The Keep holds context about it without becoming Lyhna architecture.", ["lyhna", "separate active venture", "context lane", "homestead is not lyhna", "lyhna project"]),
    ("lyhna", "agent-cost-and-binding-economics", "Agent cost and binding economics", "Lyhna-related cost analysis frames what binding decisions save for solo users, teams, and companies.", ["cost per token", "binding decision", "save", "agent cost"]),
    ("lyhna", "next-lyhna-builds", "Next Lyhna builds", "Chat analysis often asks how frontier memory/task-completion ideas relate to next Lyhna builds.", ["next lyhna builds", "relate to next lyhna", "memory systems"]),

    # Personal
    ("personal", "adam-communication-style", "Adam communication style", "Adam prefers sharp, useful, operator-grade help with warmth and low ceremony.", ["communication style", "preference", "witty", "operator", "adam"]),
    ("personal", "voice-dictation-and-wispr", "Voice, dictation, and Wispr", "Voice input, Wispr, dictation, and conversational triggering recur as personal workflow concerns.", ["voice", "wispr", "dictation", "conversation"]),
    ("personal", "portfolio-performance-summary", "Portfolio performance summary", "Personal finance/portfolio summaries need investment, current value, gain/loss, and percentage views.", ["portfolio", "invested overall", "value today", "gain or loss", "amount made"]),
    ("personal", "calendar-reminders-and-meetings", "Calendar, reminders, and meetings", "Reminders, meetings, and scheduling notes recur as personal operating material.", ["remind me", "meeting scheduled", "meeting for the", "calendar"]),
    ("personal", "family-audio-sharing", "Family audio sharing", "Adam sometimes wants written material converted into audio for family sharing.", ["audio file", "email my brother", "iphone", "listen"]),
    ("personal", "rare-names-and-personal-creative-asks", "Rare names and personal creative asks", "Short personal creative asks like rare Dutch/Frisian names are routed to personal memory.", ["rare dutch", "frisian", "friezan", "names"]),
    ("personal", "desktop-and-app-workflow-reminders", "Desktop and app workflow reminders", "Personal reminders about using Claude/Codex across apps belong in the personal operating lane.", ["excel", "powerpoint", "desktop", "apps and websites"]),
]


class Theme:
    def __init__(self, domain: str, slug: str, title: str, description: str, keywords: list[str]):
        self.domain = domain
        self.slug = slug
        self.title = title
        self.description = description
        self.keywords = [keyword.lower() for keyword in keywords]


THEME_OBJECTS = [Theme(*item) for item in THEMES]
THEMES_BY_DOMAIN = collections.defaultdict(list)
for theme in THEME_OBJECTS:
    THEMES_BY_DOMAIN[theme.domain].append(theme)


def rel(path: Path) -> str:
    return "/" + path.resolve().relative_to(ROOT).as_posix()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def redact(text: str) -> str:
    text = text or ""
    for pattern in SECRET_PATTERNS:
        text = pattern.sub("[REDACTED_SECRET]", text)
    return text


def secret_scan(text: str, label: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise SystemExit(f"secret scan failed for {label}: {pattern.pattern}")


def text_from_content(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return "\n".join(parts)
    if isinstance(value, dict):
        return str(value.get("text") or value.get("content") or "")
    return ""


def chat_text(conversation: dict) -> str:
    messages = conversation.get("chat_messages") or []
    parts = [
        conversation.get("name") or "",
        conversation.get("summary") or "",
    ]
    for message in messages:
        sender = message.get("sender") or ""
        body = message.get("text") or text_from_content(message.get("content"))
        parts.append(f"{sender}: {body}")
    return "\n".join(parts)


def first_human_line(conversation: dict) -> str:
    for message in conversation.get("chat_messages") or []:
        if (message.get("sender") or "").lower() in {"human", "user"}:
            return clean_excerpt(message.get("text") or text_from_content(message.get("content")), 220)
    return ""


def clean_excerpt(text: str, limit: int = 500) -> str:
    text = redact(URL_RE.sub("[URL]", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        return text[: limit - 3].rstrip() + "..."
    return text


def excerpt_for(text: str, keywords: list[str]) -> str:
    lowered = text.lower()
    best = -1
    for keyword in keywords:
        idx = lowered.find(keyword)
        if idx != -1 and (best == -1 or idx < best):
            best = idx
    if best == -1:
        return clean_excerpt(text, 500)
    start = max(0, best - 220)
    end = min(len(text), best + 360)
    return clean_excerpt(text[start:end], 500)


def matches_theme(text: str, theme: Theme) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in theme.keywords)


def durable_skip_noise(conversation: dict) -> tuple[bool, str]:
    title = conversation.get("name") or ""
    text = chat_text(conversation)
    first = first_human_line(conversation)
    words = re.findall(r"[A-Za-z0-9]{3,}", f"{title} {first}")
    if title.strip() and title.strip() != "[blank]" and len(words) >= 5:
        return True, "nonblank-title-with-substance"
    scores, hits = router.score_text(router.norm(text[:5000]))
    top_domain, top_score = max(scores.items(), key=lambda item: item[1])
    if top_score >= 6 and len(words) >= 4:
        return True, f"strong-domain-signal:{top_domain}"
    if len(words) >= 18 and not router.looks_like_link_only(first):
        return True, "short-but-substantive-human-line"
    return False, "blank/link/tiny-no-durable-signal"


def route_rescued(conversation: dict) -> tuple[str, str]:
    text = router.norm(chat_text(conversation)[:12000])
    scores, hits = router.score_text(text)
    title = router.clean_cell(conversation.get("name") or conversation.get("title") or "[blank]")
    title_domain = router.explicit_title_domain(title) if title != "[blank]" else None
    domain, reason = router.choose_domain(scores, hits, title_domain=title_domain)
    return domain, reason


def load_inputs() -> tuple[dict, dict[str, dict], list[dict]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    with zipfile.ZipFile(EXPORT) as archive:
        conversations = json.load(archive.open("conversations.json"))
        docs = []
        for name in sorted(path for path in archive.namelist() if path.startswith("projects/") and path.endswith(".json")):
            project = json.load(archive.open(name))
            project_name = (project.get("name") or "").strip()
            for doc in project.get("docs") or []:
                docs.append(
                    {
                        "project": project_name,
                        "filename": doc.get("filename") or "[untitled]",
                        "content": doc.get("content") or "",
                        "created_at": doc.get("created_at"),
                    }
                )
    return manifest, {item.get("uuid"): item for item in conversations}, docs


def build_sources(manifest: dict, conversations: dict[str, dict], docs: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    route_by_uuid = {item["uuid"]: item for item in manifest["chat_routes"]}
    rescued = []
    skip_checked = []
    sources = []

    for uuid, route in route_by_uuid.items():
        conversation = conversations.get(uuid)
        if not conversation:
            continue
        if route["domain"] == "NEEDS_DECISION":
            continue
        if route["domain"] == "skip-noise":
            durable, why = durable_skip_noise(conversation)
            skip_checked.append({"uuid": uuid, "title": route["title"], "durable": durable, "why": why})
            if not durable:
                continue
            domain, reason = route_rescued(conversation)
            if domain not in router.DOMAINS:
                continue
            route = {**route, "domain": domain, "reason": f"rescued-skip-noise:{reason}"}
            rescued.append({"uuid": uuid, "title": route["title"], "domain": domain, "why": why})

        text = chat_text(conversation)
        sources.append(
            {
                "id": f"chat:{uuid}",
                "kind": "chat",
                "domain": route["domain"],
                "title": route["title"],
                "updated_at": route.get("updated_at"),
                "messages": route.get("messages", 0),
                "text": text,
                "first_human": first_human_line(conversation),
                "route_reason": route.get("reason", ""),
            }
        )

    doc_routes = collections.defaultdict(list)
    for item in manifest["doc_routes"]:
        doc_routes[(item["project"], item["filename"])].append(item)
    for doc in docs:
        route_items = doc_routes.get((doc["project"], doc["filename"]), [])
        if not route_items:
            continue
        route = route_items[0]
        domain = route["domain"]
        if domain not in router.DOMAINS:
            continue
        sources.append(
            {
                "id": f"doc:{doc['project']}:{doc['filename']}",
                "kind": "project-doc",
                "domain": domain,
                "title": f"{doc['project']} / {doc['filename']}",
                "updated_at": doc.get("created_at"),
                "messages": 0,
                "text": f"{doc['project']}\n{doc['filename']}\n{doc['content']}",
                "first_human": "",
                "route_reason": route.get("reason", ""),
            }
        )
    return sources, skip_checked, rescued


def mine(sources: list[dict]) -> dict[str, dict]:
    concepts: dict[str, dict] = {}
    for source in sources:
        for theme in THEMES_BY_DOMAIN[source["domain"]]:
            if not matches_theme(source["text"], theme):
                continue
            key = f"{theme.domain}/{theme.slug}"
            concept = concepts.setdefault(
                key,
                {
                    "theme": theme,
                    "sources": [],
                    "rejected": [],
                    "contradictions": set(),
                },
            )
            concept["sources"].append(
                {
                    "id": source["id"],
                    "kind": source["kind"],
                    "title": source["title"],
                    "updated_at": source["updated_at"],
                    "messages": source["messages"],
                    "route_reason": source["route_reason"],
                    "excerpt": excerpt_for(source["text"], theme.keywords),
                }
            )
            lowered = source["text"].lower()
            if any(word in lowered for word in ["rejected", "too close", "doesn't need", "do not", "retired", "wrong", "not special", "lost his mind"]):
                concept["rejected"].append(source["id"])
            if theme.domain == "keryke" and "frostbite" in lowered and "arlo" in lowered:
                concept["contradictions"].add("Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects.")
            if theme.domain == "lyhna" and "ordinary domain" in lowered and "boundary" in lowered:
                concept["contradictions"].add("Old boundary and ordinary-domain framing appear; current Keep doctrine treats Lyhna as a separate active venture whose context is held here.")
            if "supabase" in lowered and source["domain"] in {"keryke", "homesteadai-io"}:
                concept["contradictions"].add("Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.")
    return concepts


def write_raw_bundle(domain: str, slug: str, payload: dict) -> Path:
    raw_dir = RAW_ROOT / domain / "claude-corpus-2026-06-25"
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / f"{slug}-evidence.json"
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    secret_scan(text, str(path))
    path.write_text(text, encoding="utf-8")
    return path


def concept_frontmatter(theme: Theme, raw_path: Path, support_count: int, confidence: str, tags: list[str]) -> str:
    tag_text = ", ".join(tags)
    return f"""---
type: Concept
title: {theme.title}
description: {theme.description}
domain: {theme.domain}
status: canonical
confidence: {confidence}
source_refs: [{rel(raw_path)}]
tags: [{tag_text}]
created: {NOW}
updated: {NOW}
---

"""


def write_concept(concept: dict) -> tuple[Path | None, bool]:
    theme: Theme = concept["theme"]
    sources = sorted(concept["sources"], key=lambda item: (-(item.get("messages") or 0), item.get("title") or ""))
    unique_sources = {item["id"] for item in sources}
    confidence = "high" if len(unique_sources) >= 5 else "medium"
    tags = [theme.domain, "claude-corpus", "phase-2-mine"]
    if concept["rejected"]:
        tags.append("explored-rejected")
    if concept["contradictions"]:
        tags.append("contradiction-flag")

    payload = {
        "theme": theme.slug,
        "title": theme.title,
        "domain": theme.domain,
        "source_export": str(EXPORT),
        "source_count": len(unique_sources),
        "sources": sources,
        "rejected_source_ids": sorted(set(concept["rejected"])),
        "contradictions": sorted(concept["contradictions"]),
    }
    raw_path = write_raw_bundle(theme.domain, theme.slug, payload)
    concept_path = ROOT / theme.domain / f"{theme.slug}.md"
    if concept_path.exists():
        return concept_path, False

    evidence_lines = []
    for item in sources[:8]:
        evidence_lines.append(f"- `{item['id']}` ({item['kind']}, {item.get('messages') or 0} msgs): {item['title']} — {item['excerpt']}")
    contradiction_lines = [f"- {item}" for item in sorted(concept["contradictions"])] or ["- None flagged in this pass."]
    rejected_lines = [f"- `{item}`" for item in sorted(set(concept["rejected"]))[:12]] or ["- None flagged in this pass."]

    body = f"""# {theme.title}

## Verdict

{theme.description}

## Durability

- Reconciled source count: {len(unique_sources)}
- Confidence: {confidence}
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

{chr(10).join(evidence_lines)}

## Explored / Rejected Signals

{chr(10).join(rejected_lines)}

## Contradictions / Open Questions

{chr(10).join(contradiction_lines)}

## Source Trail

- Redacted evidence bundle: [{rel(raw_path)}]({rel(raw_path)})
- Source export: `Anthropic Claude Chat Corpus .zip`
"""
    text = concept_frontmatter(theme, raw_path, len(unique_sources), confidence, tags) + body
    secret_scan(text, str(concept_path))
    concept_path.write_text(text, encoding="utf-8")
    return concept_path, True


def frontier_sanity(sources: list[dict]) -> list[dict]:
    rows = []
    for source in sources:
        if source["kind"] != "chat" or source["domain"] != "keryke":
            continue
        lowered = source["text"].lower()
        frostbite_hits = [kw for kw in router.KEYWORDS["frostbite"] if kw in lowered]
        keryke_hits = [kw for kw in router.KEYWORDS["keryke"] if kw in lowered]
        if frostbite_hits and keryke_hits:
            rows.append(
                {
                    "title": source["title"],
                    "messages": source["messages"],
                    "keryke_hits": ", ".join(keryke_hits[:5]),
                    "frostbite_hits": ", ".join(frostbite_hits[:5]),
                    "route_reason": source["route_reason"],
                }
            )
    rows.sort(key=lambda item: item["messages"], reverse=True)
    return rows[:5]


def report_markdown(
    concepts: dict[str, dict],
    created: list[Path],
    merged_existing: list[Path],
    skip_checked: list[dict],
    rescued: list[dict],
    sanity: list[dict],
) -> str:
    per_domain = collections.Counter(concept["theme"].domain for concept in concepts.values())
    created_per_domain = collections.Counter(path.parent.name for path in created)
    contradiction_count = sum(1 for concept in concepts.values() if concept["contradictions"])
    rejected_count = sum(1 for concept in concepts.values() if concept["rejected"])
    source_matches = sum(len(concept["sources"]) for concept in concepts.values())
    cluster_merges = max(0, source_matches - len(concepts))

    lines = [
        "---",
        "type: Session",
        "title: Claude Corpus Phase 2/3 Mine and Reconcile Report",
        "description: Full-text concept mining and reconciliation report for Adam's Claude export.",
        "tags: [homestead, claude-export, mining, reconciliation]",
        f"timestamp: {NOW}",
        "---",
        "",
        "# Claude Corpus Phase 2/3 Mine and Reconcile Report",
        "",
        "## Verdict",
        "",
        "Phase 2/3 mined the tightened manifest without mining `NEEDS_DECISION` chats. Full chat/doc text was scanned against explicit concept patterns, repeated signals were collapsed into one concept per idea, and redacted evidence bundles were written under ignored `/_raw`.",
        "",
        "## Counts",
        "",
        f"- Concepts in this mine: {len(concepts)}",
        f"- Concept files created: {len(created)}",
        f"- Existing concept path merges/skips: {len(merged_existing)}",
        f"- Source-to-concept cluster merges: {cluster_merges}",
        f"- Concepts with contradiction flags: {contradiction_count}",
        f"- Concepts with explored/rejected signals: {rejected_count}",
        "",
        "## Per-Domain Concept Counts",
        "",
        "| Domain | Concepts mined | New files created |",
        "|---|---:|---:|",
    ]
    for domain in router.DOMAINS:
        lines.append(f"| `{domain}` | {per_domain[domain]} | {created_per_domain[domain]} |")

    lines.extend(
        [
            "",
            "## Skip-Noise Check",
            "",
            f"- Skip-noise chats checked: {len(skip_checked)}",
            f"- Short-but-real chats rescued: {len(rescued)}",
        ]
    )
    if rescued:
        lines.extend(["", "| Title | Routed domain | Why rescued |", "|---|---|---|"])
        for item in rescued[:20]:
            lines.append(f"| {item['title']} | `{item['domain']}` | {item['why']} |")
    else:
        lines.append("- No skip-noise chats carried enough durable signal to rescue.")

    lines.extend(
        [
            "",
            "## Frontier Sanity: Frostbite -> Keryke Bleed",
            "",
            "These are the five largest Keryke-routed chats that still contain Frostbite vocabulary. They are shown so Adam can confirm the Frostbite drop was real bleed, not stolen signal.",
            "",
            "| Chat | Messages | Keryke hits | Frostbite hits | Route reason |",
            "|---|---:|---|---|---|",
        ]
    )
    for item in sanity:
        lines.append(f"| {item['title']} | {item['messages']} | {item['keryke_hits']} | {item['frostbite_hits']} | {item['route_reason']} |")

    lines.extend(
        [
            "",
            "## Contradiction Flags",
            "",
        ]
    )
    any_contradiction = False
    for key, concept in sorted(concepts.items()):
        if not concept["contradictions"]:
            continue
        any_contradiction = True
        lines.append(f"- `{key}`: " + " / ".join(sorted(concept["contradictions"])))
    if not any_contradiction:
        lines.append("- None flagged.")

    lines.extend(
        [
            "",
            "## Phase 4 Placeholder",
            "",
            "Cold-amnesia test is appended after Librarian rebuilds the indexes.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_report(text: str) -> None:
    secret_scan(text, str(REPORT))
    REPORT.write_text(text, encoding="utf-8")


def write_log(message: str) -> None:
    now = dt.datetime.now(dt.timezone.utc)
    path = ROOT / "write-logs" / f"{now:%Y-%m}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n- {now:%Y-%m-%dT%H:%M:%SZ} - {message}\n")


def main() -> int:
    manifest, conversations, docs = load_inputs()
    sources, skip_checked, rescued = build_sources(manifest, conversations, docs)
    concepts = mine(sources)
    created: list[Path] = []
    merged_existing: list[Path] = []
    for key, concept in sorted(concepts.items()):
        path, was_created = write_concept(concept)
        if was_created:
            created.append(path)
        elif path:
            merged_existing.append(path)

    sanity = frontier_sanity(sources)
    report = report_markdown(concepts, created, merged_existing, skip_checked, rescued, sanity)
    write_report(report)
    write_log(
        "Claude corpus Phase 2/3: "
        f"concepts={len(concepts)}, created={len(created)}, "
        f"skip_checked={len(skip_checked)}, rescued={len(rescued)}, "
        f"contradiction_concepts={sum(1 for concept in concepts.values() if concept['contradictions'])}, "
        "phase4=pending"
    )
    print(f"concepts mined: {len(concepts)}")
    print(f"concept files created: {len(created)}")
    print(f"existing concept path merges/skips: {len(merged_existing)}")
    print(f"skip-noise checked: {len(skip_checked)} rescued: {len(rescued)}")
    print(f"report: {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
