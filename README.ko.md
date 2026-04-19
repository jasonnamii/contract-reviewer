# contract-reviewer

> 🇺🇸 [English README](./README.md)

**계약 검토 5층×7도메인×3모드 엔진. Playbook 3-Tier·Redflag 카탈로그·한국법 디폴트 True.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경

## 목표

구조 없는 계약 검토는 지뢰밭. 나쁜 조항 하나 잡으면 세 개 놓치고, 상대가 한 줄로 눌러버릴 단일 수정안만 돌려주기 십상. `contract-reviewer`는 어떤 계약이든 같은 결정적 파이프라인(Redflag 스크린 → 5층 진단 → 3-Tier 플레이북)으로 돌려 협상 현장에 바로 쓸 수 있는 산출물을 뽑는다.

## 사용 시점 & 방법

계약 검토 요청시 자동 발동 (NDA, SPA, MSA, DPA, SHA, 고용, 임대차, 건설, SaaS 등). PREFLIGHT(모드·도메인·텍스트 유무) → Redflag 12종 스크린 → 5층 적용 → 도메인 오버레이 → 한국법 오버레이 → 산출물. 3모드: **M1 진단**(리뷰메모), **M2 설계**(플레이북), **M3 레드라인**(조항별 before→after). 실제 협상 시뮬은 `negotiation-skill`로 위임.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| NDA 체결 전 검토 | `"이 NDA 검토해줘"` (텍스트 첨부) | M1 진단 · D5 IP/데이터 · Redflag 스크린 → L1/L2/L5 리뷰메모 + 변호사 상담 권고 |
| SaaS MSA 표준 플레이북 | `"SaaS MSA 표준 Playbook 짜줘"` | M2 설계 · D5 · Tier1/2/3 + DPA·PIPA·GDPR 오버레이 |
| 용역계약 레드라인 | `"이 용역계약 을 입장으로 레드라인"` | M3 레드라인 · D4 · 무한책임·IP포괄양도·비경쟁 우선수정 |
| 한국법 관점만 검토 | `"하도급계약 한국법 관점만 봐줘"` | L5 단독 · D3 · 하도급법·공정거래법 불공정조항 스크린 |

## 주요 기능

- **5층 분석** — L1 의무·권리 매트릭스 · L2 리스크 3×3 · L3 플레이북 Tier1/2/3 · L4 Exit · L5 한국법 오버레이
- **7 도메인** — D1 투자금융 · D2 M&A · D3 상업거래 · D4 노무·용역 · D5 IP·데이터 · D6 부동산 · D7 건설·공공조달
- **Redflag 카탈로그** — 글로벌 12종(무한책임·Indemnity·MFN·CoC·IP 포괄양도 등) + 한국 특이 10종(약관법 14유형·3법 오버레이)
- **한국법 디폴트 True** — 2025-2026 개정 반영(상법 이사충실의무 2025.7.22, 집중투표 2025.9.9, 개인정보 DPA 2025.4)
- **3-Tier Playbook** — 쟁점 조항마다 허용안·협상안·마지노선(Walk-away) + BATNA/ZOPA 앵커

## 연동 스킬

- **[negotiation-skill](https://github.com/jasonnamii/negotiation-skill)** — 플레이북 설계 후 실제 협상 시뮬 위임
- **[startup-investment](https://github.com/jasonnamii/startup-investment)** — D1(SHA·SPA·텀시트) → 투자 판단 로직 연계
- **[holdings-consulting](https://github.com/jasonnamii/holdings-consulting)** — D2 M&A 계약 → 지주·구조조정 입력
- **[copywriting-engine](https://github.com/jasonnamii/copywriting-engine)** — 조항 기능·리스크 검토 후 문구 톤 위임

## 설치

```bash
git clone https://github.com/jasonnamii/contract-reviewer.git ~/.claude/skills/contract-reviewer
```

## 업데이트

```bash
cd ~/.claude/skills/contract-reviewer && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.
