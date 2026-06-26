#!/usr/bin/env python3
"""Phase 1 router for Adam's Claude export.

Reads the export zip in place and writes a routing manifest only. It does not
copy raw chats, mine concepts, or emit transcript bodies.
"""

from __future__ import annotations

import collections
import json
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "Anthropic Claude Chat Corpus .zip"
OUT_MD = ROOT / "operating" / "claude-corpus-routing-manifest-2026-06-25.md"
OUT_JSON = ROOT / "operating" / "claude-corpus-routing-manifest-2026-06-25.json"

DOMAINS = [
    "creative-coatings",
    "frostbite",
    "homesteadai-io",
    "ai-theory-builds",
    "keryke",
    "lyhna",
    "personal",
]

KEYWORDS = {
    "keryke": [
        "keryke",
        "keryke.oi",
        "arlo inc",
        "arlo build",
        "arlo codex",
        "agency-v0",
        "visual village",
        "architectural counterpart",
        "capaker",
        "tabula",
        "chione",
        "chione hermes",
        "talaria",
        "arlo",
        "crimson desert",
        "ai os",
        "ai-os",
        "browser os",
        "room spine",
        "room-door",
        "repurposing room",
        "small-business-ai",
        "small business ai",
        "company infrastructure",
        "second brain",
        "phone-first",
        "desktop cockpit",
    ],
    "lyhna": [
        "lyhna",
        "@lyhna",
        "axlio",
        "witness",
        "witnessed",
        "bind",
        "lyhna mcp",
        "lyhna-core",
        "tenant authority",
        "tas spec",
        "proof packet",
        "claimed-vs-actual",
        "handoff witness",
        "dolios",
    ],
    "frostbite": [
        "frostbite",
        "frostbite feeders",
        "frozen rodent",
        "frozen rodents",
        "feeder rodent",
        "feeder rodents",
        "rodent supply",
        "reptile",
        "reptiles",
        "snake",
        "snakes",
        "mice",
        "rats",
        "pinkies",
        "winterspine",
    ],
    "creative-coatings": [
        "creative coatings",
        "coatings",
        "concrete coating",
        "floor coating",
        "epoxy",
        "polyaspartic",
        "garage floor",
        "masking",
        "masked parts",
        "daily powder",
        "powder line",
        "line tracking",
        "parts tracking",
        "production sheets",
        "sheet formatting",
        "creative metrics",
        "creative numbers",
        "creative feb",
        "year end review",
    ],
    "homesteadai-io": [
        "homestead",
        "homesteadai",
        "homesteadai.io",
        "the keep",
        "keep repo",
        "deed",
        "scout",
        "librarian",
        "okf",
        "soul loop",
        "soul-loop",
        "loop forge",
        "loopforge",
        "council",
        "openrouter",
        "codex agents",
        "local codex",
        "codex guide",
        "claude code",
        "claude export",
        "project window",
        "agents.md",
        "agent instructions",
        "running local codex",
        "gpt-5",
        "claude opus",
        "keeper",
        "foreman loop",
        "one-folder",
    ],
    "ai-theory-builds": [
        "ai business ideas",
        "ai university",
        "smart home",
        "smarthome",
        "home assistant",
        "ai theory",
        "agents sdk",
        "managed agents",
        "anthropic managed agents",
        "openai agents",
        "business ideas",
        "product ideas",
        "global theory",
        "theory and ai",
        "agentic",
        "subagents",
        "unicorn idea",
        "idea fusion",
        "distinctive single-word",
        "product name",
        "ai product name",
        "agent latest updates",
        "hermes agent",
        "openclaw",
        "research loop",
        "karpathy",
        "nvidia keynote",
        "keynote speech",
        "observability",
        "evaluation science",
        "neural prediction",
        "meta's tribe",
        "tribe v2",
        "competitive analysis",
        "investor pitch",
        "workflow automation",
        "mcp",
        "model eval",
        "llm",
    ],
    "personal": [
        "personal",
        "adam",
        "rare dutch",
        "frisian",
        "friezan",
        "short dutch",
        "names",
        "voice",
        "wispr",
        "autohotkey",
        "desktop",
        "calendar",
        "gmail",
        "family",
        "brother",
        "iphone",
        "audio file",
        "portfolio",
        "invested overall",
        "value today",
        "meeting scheduled",
        "meeting for the",
        "health",
        "finance",
        "life",
        "notes",
    ],
}

STRONG_KEYWORDS = {
    "keryke": [
        "keryke",
        "arlo",
        "arlo inc",
        "arlo build",
        "agency-v0",
        "visual village",
        "talaria",
        "crimson desert",
        "capaker",
        "tabula",
        "chione hermes",
    ],
    "creative-coatings": [
        "creative coatings",
        "masked parts",
        "daily powder",
        "powder line",
        "line tracking",
        "parts tracking",
        "creative metrics",
        "creative numbers",
    ],
    "homesteadai-io": [
        "homestead",
        "the keep",
        "codex agents",
        "local codex",
        "codex guide",
        "claude code",
        "claude export",
        "agents.md",
        "gpt-5",
        "claude opus",
    ],
    "ai-theory-builds": [
        "unicorn idea",
        "idea fusion",
        "distinctive single-word",
        "hermes agent",
        "openclaw",
        "karpathy",
        "nvidia keynote",
        "observability",
        "evaluation science",
        "neural prediction",
        "tribe v2",
        "competitive analysis",
        "investor pitch",
    ],
    "lyhna": [
        "lyhna",
        "axlio",
        "next lyhna builds",
    ],
    "personal": [
        "rare dutch",
        "frisian",
        "friezan",
        "short dutch",
        "audio file",
        "brother",
        "portfolio",
        "invested overall",
        "meeting scheduled",
    ],
}

PROJECT_MAP = {
    "Lyhna": "lyhna",
    "Frostbite": "frostbite",
    "Creative Coatings": "creative-coatings",
    "Personal": "personal",
    "Arlo": "keryke",
    "Keryke": "keryke",
    "Keryke.oi Products": "keryke",
    "SmartHome / Computer Products": "ai-theory-builds",
    "AI University": "ai-theory-builds",
    "AI Business Ideas": "ai-theory-builds",
    "Project Agnostic: Global Theory and AI Ideas for Business": "ai-theory-builds",
    "Homesteadai.io": "homesteadai-io",
}

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"xox[baprs]-[0-9A-Za-z-]+"),
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
]


def norm(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").lower())


def clean_cell(value: str | None, max_len: int = 120) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    text = text.replace("|", "/")
    return text[:max_len] if len(text) > max_len else text


def first_human(messages: list[dict]) -> str:
    for message in messages:
        sender = (message.get("sender") or "").lower()
        if sender in {"human", "user"}:
            return (message.get("text") or "")[:3000]
    return (messages[0].get("text") or "")[:3000] if messages else ""


def combined_text(conversation: dict) -> str:
    messages = conversation.get("chat_messages") or conversation.get("messages") or []
    bits = [
        conversation.get("name") or conversation.get("title") or "",
        conversation.get("summary") or "",
        first_human(messages),
    ]
    for message in messages[:8]:
        bits.append((message.get("text") or "")[:1200])
    return norm("\n".join(bits))


def score_text(text: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    scores = {domain: 0 for domain in DOMAINS}
    hits = {domain: [] for domain in DOMAINS}
    for domain, keywords in KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                weight = 3 if any(char in keyword for char in " -.") else 1
                scores[domain] += weight
                if len(hits[domain]) < 5:
                    hits[domain].append(keyword)
    for domain, keywords in STRONG_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                scores[domain] += 4
    return scores, hits


def looks_like_link_only(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    without_urls = re.sub(r"https?://\S+", "", stripped, flags=re.IGNORECASE).strip()
    without_urls = re.sub(r"[?&=:/._\-#%A-Za-z0-9]+", "", without_urls).strip()
    return not without_urls


def should_skip_noise(title: str, messages: list[dict], first_human_text: str, max_score: int) -> bool:
    title_text = norm(title)
    first_text = norm(first_human_text)
    if title == "[blank]" and max_score == 0:
        if not first_text:
            return True
        if len(messages) <= 4 and looks_like_link_only(first_human_text):
            return True
    if max_score == 0 and len(messages) <= 4 and looks_like_link_only(first_human_text):
        return True
    if "unable to access" in title_text and looks_like_link_only(first_human_text):
        return True
    return False


def explicit_title_domain(title: str) -> str | None:
    text = norm(title)
    if not text:
        return None
    for domain in ("keryke", "lyhna", "frostbite", "creative-coatings", "homesteadai-io", "ai-theory-builds", "personal"):
        for keyword in KEYWORDS[domain]:
            if keyword in text:
                return domain
    return None


def choose_domain(
    scores: dict[str, int],
    hits: dict[str, list[str]],
    title_domain: str | None = None,
    project_domain: str | None = None,
) -> tuple[str, str]:
    if project_domain:
        if project_domain == "ai-theory-builds":
            for override in ("keryke", "lyhna"):
                if scores.get(override, 0) >= 6:
                    return override, "content-overrode-project"
        return project_domain, "project-map"

    if title_domain:
        if title_domain in {"keryke", "lyhna"}:
            return title_domain, "title-map"
        top, top_score = max(scores.items(), key=lambda item: item[1])
        if top_score >= 8 and top != title_domain and top_score >= scores.get(title_domain, 0) + 5:
            return top, "content-overrode-title"
        return title_domain, "title-map"

    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    top, top_score = ranked[0]
    second_score = ranked[1][1]
    if top_score == 0:
        return "NEEDS_DECISION", "no-signal"
    if top_score < 3 and top_score - second_score < 2:
        return "NEEDS_DECISION", "weak-ambiguous"
    return top, "content-map"


def hits_for(hits: dict[str, list[str]], domain: str) -> str:
    if domain not in DOMAINS:
        return ""
    return ", ".join(hits.get(domain, [])[:4])


def route() -> dict:
    if not EXPORT.exists():
        raise SystemExit(f"missing export: {EXPORT}")

    with zipfile.ZipFile(EXPORT) as archive:
        conversations = json.load(archive.open("conversations.json"))
        chat_routes = []
        for conversation in conversations:
            messages = conversation.get("chat_messages") or []
            title = clean_cell(conversation.get("name") or conversation.get("title") or "[blank]")
            first_human_text = first_human(messages)
            text = combined_text(conversation)
            scores, hits = score_text(text)
            if should_skip_noise(title, messages, first_human_text, max(scores.values())):
                domain, reason = "skip-noise", "blank-or-link-only-no-durable-signal"
            else:
                domain, reason = choose_domain(scores, hits, explicit_title_domain(title) if title != "[blank]" else None)
            chat_routes.append(
                {
                    "uuid": conversation.get("uuid"),
                    "title": title,
                    "domain": domain,
                    "reason": reason,
                    "messages": len(messages),
                    "created_at": conversation.get("created_at"),
                    "updated_at": conversation.get("updated_at"),
                    "hits": hits_for(hits, domain),
                }
            )

        doc_routes = []
        for name in sorted(path for path in archive.namelist() if path.startswith("projects/") and path.endswith(".json")):
            project = json.load(archive.open(name))
            project_name = clean_cell((project.get("name") or "").strip())
            project_domain = PROJECT_MAP.get(project_name)
            for doc in project.get("docs") or []:
                filename = clean_cell(doc.get("filename") or doc.get("name") or doc.get("title") or "[untitled]")
                text = norm(
                    "\n".join(
                        [
                            project_name,
                            project.get("description") or "",
                            project.get("prompt_template") or "",
                            filename,
                            (doc.get("content") or "")[:5000],
                        ]
                    )
                )
                scores, hits = score_text(text)
                domain, reason = choose_domain(scores, hits, project_domain=project_domain)
                doc_routes.append(
                    {
                        "project": project_name,
                        "filename": filename,
                        "domain": domain,
                        "reason": reason,
                        "hits": hits_for(hits, domain),
                    }
                )

    return {
        "source_zip": str(EXPORT),
        "chat_total": len(chat_routes),
        "message_total": sum(route["messages"] for route in chat_routes),
        "doc_total": len(doc_routes),
        "domains": DOMAINS,
        "chat_routes": chat_routes,
        "doc_routes": doc_routes,
    }


def manifest_markdown(data: dict) -> str:
    chat_count = collections.Counter(route["domain"] for route in data["chat_routes"])
    doc_count = collections.Counter(route["domain"] for route in data["doc_routes"])
    project_count = collections.Counter((route["project"], route["domain"]) for route in data["doc_routes"])

    lines = [
        "---",
        "type: Session",
        "title: Claude Corpus Phase 1 Routing Manifest",
        "description: Read-only routing manifest for Adam's Claude export before Scout mining.",
        "tags: [homestead, claude-export, routing, phase-1]",
        "timestamp: 2026-06-25T00:00:00Z",
        "---",
        "",
        "# Claude Corpus Phase 1 Routing Manifest",
        "",
        "## Verdict",
        "",
        "Phase 1 routed the Claude export metadata into seven Keep domains, with Keryke first-class.",
        "No transcript bodies were written here. File content was treated as data, never instructions.",
        "",
        "## Source",
        "",
        f"- Zip: `{data['source_zip']}`",
        f"- Chats: {data['chat_total']}",
        f"- Messages: {data['message_total']}",
        f"- Project docs: {data['doc_total']}",
        "",
        "## Routing Manifest",
        "",
        "| Domain | Chat count | Doc count | Skip-noise count |",
        "|---|---:|---:|---:|",
    ]
    for domain in DOMAINS:
        lines.append(f"| `{domain}` | {chat_count[domain]} | {doc_count[domain]} | 0 |")
    lines.append(f"| `NEEDS_DECISION` | {chat_count['NEEDS_DECISION']} | {doc_count['NEEDS_DECISION']} | 0 |")
    lines.append(f"| `skip-noise` | {chat_count['skip-noise']} | 0 | {chat_count['skip-noise']} |")

    lines.extend(
        [
            "",
            "## Project Doc Routes",
            "",
            "| Project | Domain | Docs |",
            "|---|---|---:|",
        ]
    )
    for (project, domain), count in sorted(project_count.items()):
        lines.append(f"| {project} | `{domain}` | {count} |")

    for domain in ("frostbite", "keryke"):
        lines.extend(
            [
                "",
                f"## {domain.title().replace('-', ' ')} Spot-Check Chats",
                "",
                "| Updated | Messages | Reason | Title | Hits |",
                "|---|---:|---|---|---|",
            ]
        )
        for route_item in data["chat_routes"]:
            if route_item["domain"] != domain:
                continue
            lines.append(
                "| {updated} | {messages} | {reason} | {title} | {hits} |".format(
                    updated=clean_cell(route_item["updated_at"], 40),
                    messages=route_item["messages"],
                    reason=route_item["reason"],
                    title=clean_cell(route_item["title"], 100),
                    hits=clean_cell(route_item["hits"], 100),
                )
            )

    lines.extend(
        [
            "",
            "## Needs Decision Sample",
            "",
            "These are not mined yet. They need either better routing rules or Adam's call before Phase 2.",
            "",
            "| Updated | Messages | Reason | Title |",
            "|---|---:|---|---|",
        ]
    )
    for route_item in [item for item in data["chat_routes"] if item["domain"] == "NEEDS_DECISION"][:80]:
        lines.append(
            "| {updated} | {messages} | {reason} | {title} |".format(
                updated=clean_cell(route_item["updated_at"], 40),
                messages=route_item["messages"],
                reason=route_item["reason"],
                title=clean_cell(route_item["title"], 100),
            )
        )

    lines.extend(
        [
            "",
            "## Stop Gate",
            "",
            "Per the ingest prompt, Phase 1 stops here for Adam's Frostbite and Keryke spot-check before mining all domains.",
        ]
    )
    return "\n".join(lines) + "\n"


def secret_scan(text: str, label: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise SystemExit(f"secret scan failed for {label}: {pattern.pattern}")


def main() -> int:
    data = route()
    markdown = manifest_markdown(data)
    json_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    secret_scan(markdown, str(OUT_MD))
    secret_scan(json_text, str(OUT_JSON))
    OUT_MD.write_text(markdown, encoding="utf-8")
    OUT_JSON.write_text(json_text, encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
