# contract-reviewer

> 🇰🇷 [한국어 README](./README.ko.md)

**Contract review engine with 5 layers × 7 domains × 3 modes. Playbook 3-Tier, Redflag catalog, Korean law overlay default-on.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

Reviewing a contract without structure is a minefield: you spot one bad clause, miss three others, and hand back single-option edits the counterparty can kill with one line. `contract-reviewer` runs every contract through the same deterministic pipeline — Redflag screen → 5-layer diagnosis → 3-Tier playbook — so the output is negotiation-ready, not a one-shot opinion.

## When & How to Use

Trigger on contract review requests (NDA, SPA, MSA, DPA, SHA, employment, lease, construction, SaaS). The engine runs PREFLIGHT (mode · domain · text presence) → 12-Redflag screen → 5-layer application → domain overlay → Korean law overlay → output. Three modes: **M1 Diagnosis** (review memo), **M2 Design** (playbook), **M3 Redline** (before→after per clause). For actual negotiation simulation, hand off to `negotiation-skill`.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Review NDA before signing | `"이 NDA 검토해줘"` (with text) | M1 Diagnosis · D5 IP/Data · Redflag screen → L1/L2/L5 review memo + lawyer consult flag |
| Build SaaS MSA playbook | `"SaaS MSA 표준 Playbook 짜줘"` | M2 Design · D5 · Tier1/2/3 with DPA · PIPA · GDPR overlay |
| Redline vendor agreement | `"이 용역계약 을 입장으로 레드라인"` | M3 Redline · D4 · uncapped liability · IP assignment · non-compete prioritized |
| Korean law focus only | `"하도급계약 한국법 관점만 봐줘"` | L5 standalone · D3 · Subcontracting Act · Fair Trade Act unfair-clause screen |

## Key Features

- **5-Layer Analysis** — L1 Obligation matrix · L2 Risk 3×3 · L3 Playbook Tier1/2/3 · L4 Exit · L5 Korea overlay
- **7 Domains** — D1 Investment · D2 M&A · D3 Commercial · D4 Labor · D5 IP/Data · D6 Real Estate · D7 Construction
- **Redflag Catalog** — 12 global (Uncapped Liability, Indemnity, MFN, CoC, IP assignment, etc.) + 10 Korea-specific (약관법 14 types, 3법 overlay)
- **Korean Law Default-On** — 2025-2026 amendments baked in (상법 이사충실의무 2025.7.22, 집중투표 2025.9.9, 개인정보 DPA 2025.4)
- **3-Tier Playbook** — every contested clause outputs accept-case · negotiate-case · walk-away with BATNA/ZOPA anchors

## Works With

- **[negotiation-skill](https://github.com/jasonnamii/negotiation-skill)** — hands off to actual negotiation simulation after playbook design
- **[startup-investment](https://github.com/jasonnamii/startup-investment)** — D1 (SHA/SPA/Term Sheet) feeds investment-decision logic
- **[holdings-consulting](https://github.com/jasonnamii/holdings-consulting)** — D2 M&A contracts as structural-reorganization input
- **[copywriting-engine](https://github.com/jasonnamii/copywriting-engine)** — clause phrasing handoff after function/risk review

## Installation

```bash
git clone https://github.com/jasonnamii/contract-reviewer.git ~/.claude/skills/contract-reviewer
```

## Update

```bash
cd ~/.claude/skills/contract-reviewer && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
