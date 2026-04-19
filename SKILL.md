---
name: contract-reviewer
description: |
  계약 검토 5층×7도메인×3모드 엔진. Playbook 3-Tier·Redflag 카탈로그·한국법 디폴트 True.
  P1: 계약검토, 계약리뷰, contract review, 레드라인, redline, playbook, NDA, SPA, MSA, DPA, SHA, redflag, 계약리스크, 계약진단.
  P2: 검토해줘, 리뷰해줘, 레드라인 쳐줘, review, redline.
  P3: contract review, redline, playbook design, fallback position, CLM, indemnity review.
  P5: 리뷰메모로, 레드라인으로, 플레이북으로.
  NOT: 협상시뮬(→negotiation-skill), 투자판단(→startup-investment), 재무모델(→financial-model), 사업계획서(→bp-guide), 사업전략(→biz-skill).
---

# Contract Reviewer

계약서를 **5층 × 7도메인 × 3모드**로 검토하는 진단·설계·레드라인 엔진. 법률 자문 대체 ✗ — 검토·협상 준비 프레임까지. 한국 디폴트 True.

---

## 절대 규칙

| # | 규칙 | 이유 |
|---|------|------|
| 1 | **법률자문 경계** — 결론은 "검토 의견·협상안". "이건 법적으로 유효·무효" 확정 판단 ✗. 변호사 자문 권고 1줄 필수 | 무자격 법률자문 리스크 차단 |
| 2 | **Playbook 3-Tier 필수** — 모든 쟁점 조항은 Tier1 허용안·Tier2 협상안·Tier3 마지노선(Walk-away)으로 출력. 단일 권고 ✗ | 실무 표준(LegalOn·Ironclad). 협상 현장에서 즉시 대응 |
| 3 | **Redflag 12종 스크린 선행** — 조항별 검토 전 무조건 12종 카탈로그로 1차 스크린 → Red/Yellow/Green 태깅 | 중대 리스크 선식별 |
| 4 | **한국 디폴트 True** — 한국법 오버레이(L5) 자동 On. 해외법 준거·해외계약 명시 시만 Off | 사용자 절대 다수 한국 |
| 5 | **5층 독립 호출 가능** — "Redflag만"·"L5 한국법만" 요청 시 단일 층 단독 실행 | 강제 cascade 비효율 |
| 6 | **PREFLIGHT 3체크** — 모드·도메인·계약서 텍스트 유무 확인. 텍스트 없으면 샘플·체크리스트 모드로 전환 | 계약서 유/무가 산출물 형태 결정 |
| 7 | **최신 법령 주의** — 2025-2026 개정 자주(상법 이사충실의무·개인정보 DPA·약관법). 검토 시점 명시 필수 | 법령은 빠르게 변한다 |

---

## 실행 흐름

```
🚦 PREFLIGHT(모드·도메인·텍스트) → ① Redflag 12종 스크린 → ② 5층 적용 → ③ 도메인 오버레이 → ④ 한국 오버레이(L5) → ⑤ 산출물
```

### 🚦 PREFLIGHT (3체크)

| 체크 | 입력 | 미확정 시 |
|------|------|----------|
| 모드 | M1 진단 / M2 설계(초안·Playbook) / M3 레드라인 | 1줄 후보 제시 + 형 선택 |
| 도메인 | D1~D7 (아래 도메인 라우터) | 추정 + 확신도 태깅 + 진행 |
| 텍스트 유무 | 실제 계약서 ○ / 체크리스트만 ✗ | 없으면 체크리스트+Playbook 모드 |

### ① Redflag 12종 스크린 (1차 필터)

`→ references/redflag_catalog.md` (상세 정의·예문·대응)

| # | Redflag | 카테고리 | 기본 판정 |
|---|---------|---------|---------|
| 1 | Uncapped Liability / 무한책임 | 리스크할당 | Red |
| 2 | Uncapped Indemnity / 무한보상 | 리스크할당 | Red |
| 3 | Liquidated Damages Penalty / 과도위약금 | 리스크할당 | Yellow |
| 4 | Unilateral Termination / 편측해지 | 거버넌스 | Red |
| 5 | MFN (Most-Favored-Nation) | 거래조건 | Yellow |
| 6 | Change of Control Consent / 지배권승인 | 거버넌스 | Yellow |
| 7 | IP Broad Assignment / IP 포괄양도 | IP | Red |
| 8 | Exclusivity / 독점 | 거래조건 | Yellow |
| 9 | Arbitration Seat 편측 / 준거법 편측 | 분쟁해결 | Yellow |
| 10 | Perpetual Confidentiality / 무기한 비밀유지 | IP | Yellow |
| 11 | Unilateral Amendment / 일방적 변경권 | 거버넌스 | Red |
| 12 | Non-Compete 과다 / 비경쟁 장기·광역 | 노무·거래 | Yellow |

**한국 특이 Redflag 10종:** `→ references/redflag_korea.md` (약관법 14유형·공정거래·하도급·대리점·가맹·개정상법·개인정보)

### ② 5층 적용

| 층 | 내용 | 스포크 |
|----|------|--------|
| L1 OBLIGATION | 의무·권리 매트릭스 (당사자별 Who does What) | `→ references/L1_obligation.md` |
| L2 RISK | 리스크 식별·배분(3×3 Prob×Impact)·한계·카브아웃 | `→ references/L2_risk.md` |
| L3 PLAYBOOK | Tier1 허용·Tier2 협상·Tier3 마지노선 (BATNA/ZOPA 연동) | `→ references/L3_playbook.md` |
| L4 EXIT | 종료·해지·치유기간·잔존의무(Surviving Obligations) | `→ references/L4_exit.md` |
| L5 KOREA | 한국법 오버레이(민법·상법·약관·공정거래·3법·개인정보) | `→ references/L5_korea.md` |

### ③ 도메인 라우터 (7도메인)

`→ references/domains/` (D1~D7 각 .md)

| 코드 | 도메인 | 대표 계약 |
|-----|-------|---------|
| D1 | 투자금융 | SHA·SPA·Term Sheet·전환사채(CB)·RCPS·SAFE |
| D2 | M&A·지배구조 | 합병계약·주식양수도·자산양수도·경영권계약 |
| D3 | 상업거래 | 공급·판매·유통·라이선스·파트너십·대리점·가맹 |
| D4 | 노무·용역 | 고용계약·용역·컨설팅·비경쟁·직무발명 |
| D5 | IP·데이터 | NDA·IP양도·라이선스·DPA·SaaS MSA |
| D6 | 부동산 | 임대차(주택·상가)·매매·임대관리·개발 |
| D7 | 건설·공공조달 | FIDIC·시공·설계감리·정부계약·나라장터 |

### ④ 한국 오버레이 (L5, 디폴트 True)

`→ references/L5_korea.md` 상세 7축: 민법계약편·상법·약관법·공정거래·3법(하도급·대리점·가맹)·개인정보·개정상법(2025.7.22·2025.9.9)

### ⑤ 산출물

`→ references/modes/M{1,2,3}.md` 모드별 포맷.

---

## 모드별 산출물

| 모드 | 입력 | 출력 | 포맷 |
|------|------|------|------|
| M1 진단 | 계약서 텍스트 | Redflag 태깅표 + 5층 진단 + 리스크매트릭스 + 변호사 상담 필요도 | 리뷰메모.md |
| M2 설계 | 계약유형·목표·당사자 | Playbook(Tier1/2/3) + 조항별 대안 + 한국 오버레이 | 플레이북.md |
| M3 레드라인 | 계약서 텍스트 + 입장(갑/을) | 조항별 수정제안(before→after) + 코멘트 + 우선순위 | 레드라인.md |

---

## 예시

| 입력 | 라우팅 |
|------|--------|
| "이 NDA 검토해줘" (텍스트 첨부) | M1 진단 / D5 IP·데이터 / Redflag 스크린 → L1/L2/L5 + 변호사 상담 권고 |
| "SaaS MSA 표준 Playbook 짜줘" | M2 설계 / D5 / Tier1/2/3 + DPA·GDPR·PIPA 오버레이 |
| "이 용역계약 을 입장으로 레드라인" | M3 레드라인 / D4 / 무한책임·IP포괄양도·비경쟁 조항 우선수정 |
| "하도급계약 한국법 관점만 봐줘" | L5 단독 호출 / D3 / 하도급법·공정거래법 불공정조항 스크린 |
| "M&A SPA 진술보장 조항 위험도" | M1 진단 / D2 / L2 리스크매트릭스 + 에스크로·Cap·Basket |

---

## Gotchas

| 함정 | 대응 |
|------|------|
| 단일 권고("이렇게 고치세요") 출력 | 절대규칙 2 — 반드시 Tier1/2/3 3-Tier Playbook |
| 법적 유효·무효 단정 | 절대규칙 1 — "검토 의견" 명시, 변호사 상담 권고 1줄 필수 |
| 한국 오버레이 자동 Off | 절대규칙 4 — 한국 디폴트 True, 해외 명시될 때만 Off |
| Redflag 스크린 스킵 후 조항별 리뷰 직행 | 중대 리스크 놓침. 절대규칙 3 — 12종 스크린 선행 |
| 2024년 이전 기준으로 한국법 분석 | 2025-2026 개정 다수(상법·개인정보). 검토 시점 반드시 명시 |
| negotiation-skill 영역 침범(가격 협상 시뮬) | L3 Playbook까지. 실제 협상 시뮬·복기는 negotiation-skill 위임 |
| copywriting-engine 영역 침범(계약 문구 미려화) | 조항 기능·리스크까지. 문구 톤은 copywriting-engine 위임 |
| 7도메인 강제 매칭(애매 케이스) | PREFLIGHT에서 확인. 모호 시 가장 가까운 도메인 + 인접 도메인 메모 |
| DPA/SaaS MSA를 D3 상업거래로만 처리 | D5 IP·데이터가 우선. 개인정보 처리 포함 시 무조건 L5 개인정보 오버레이 |

---

## 트리거 사전 (한 줄 매칭)

**핵심 키워드:** 계약검토 · 계약리뷰 · 레드라인 · Playbook · Redflag · 계약리스크 · 계약진단

| 입력 단어 | 모드 | 도메인 |
|-----------|------|--------|
| "검토·진단·리뷰·redflag·리스크" | M1 | 입력 의존 |
| "설계·초안·플레이북·playbook·template" | M2 | 입력 의존 |
| "레드라인·redline·수정제안·코멘트" | M3 | 입력 의존 |
| "SHA·SPA·Term Sheet·CB·RCPS·SAFE" | - | D1 |
| "합병·인수·경영권·M&A·SPA" | - | D2 |
| "공급·유통·라이선스·대리점·가맹·프랜차이즈" | - | D3 |
| "고용·용역·컨설팅·비경쟁·직무발명" | - | D4 |
| "NDA·비밀유지·IP양도·DPA·GDPR·PIPA·SaaS·MSA" | - | D5 |
| "임대차·매매·상가·주택·부동산" | - | D6 |
| "시공·건설·FIDIC·정부계약·나라장터·공공조달" | - | D7 |
