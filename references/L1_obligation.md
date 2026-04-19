# L1 OBLIGATION — 의무·권리 매트릭스

모든 계약검토의 기초. "누가 무엇을 하는가" 추출. 출처: Tina Stark "Drafting Contracts", Ken Adams MSCD.

## 원칙
- 모든 문장을 **의무(Shall)·권리(May)·조건(If)·선언(Is)** 4유형으로 분해
- 당사자별로 독립 매트릭스 작성 → 불균형 발견

## 매트릭스 템플릿

| # | 조항 | 당사자 | 유형 | 내용 | 이행기 | 불이행 결과 |
|---|------|-------|------|------|-------|-----------|
| 1 | §3.1 | 갑 | 의무(Shall) | 계약금액 지급 | 체결일+30일 | 지연이자 연 6% |
| 2 | §4.1 | 을 | 의무(Shall) | 용역 제공 | 체결일~12개월 | 위약금·해제 |
| 3 | §7 | 을 | 권리(May) | 3개월 Notice 후 해지 | anytime | Termination Fee |

## 검토 포인트

### 1. 균형성
- 갑·을 의무·권리 개수 비교
- 일방 과중 = Yellow/Red
- "Party A shall ... Party B may ..." 패턴 경계

### 2. 완결성 (Gap 점검)
- Consideration(대가) 흐름 양방향
- Performance Standard(이행기준) 명시 여부
- Representations & Warranties (진술·보장) 범위
- Acceptance Criteria (검수기준)
- Payment Terms (지급조건·지연이자)

### 3. 명확성 (Ambiguity 점검)
- "reasonable efforts" vs "best efforts" vs "commercially reasonable efforts"
- "shall" vs "will" vs "may" 일관성
- 용어 정의(Definitions) vs 본문 사용 일치
- 수량·기한 구체성 ("as soon as possible" → 금지, 구체 일수)

### 4. Consideration 대응성
- 갑 지급 ↔ 을 제공 = 대칭 흐름
- 선지급·분할지급·후지급 리스크 배분
- 에스크로·성과연동 필요성

## 산출 포맷
```markdown
### L1 의무·권리 매트릭스

#### 갑 측 의무 (N개)
| § | 내용 | 이행기 | 불이행 결과 |
|---|------|-------|-----------|

#### 을 측 의무 (N개)
| § | 내용 | 이행기 | 불이행 결과 |
|---|------|-------|-----------|

#### 균형성 진단
- 의무 개수: 갑 X개 vs 을 Y개
- 불균형 포인트: [조항 열거]

#### Gap 발견
- 누락된 조항: [R&W·Acceptance·Cure Period 등]
```

## 도메인별 필수 조항
| 도메인 | 필수 조항 |
|-------|----------|
| D1 투자금융 | 주주간 합의·우선매수·Drag/Tag·R&W·Indemnity·Escrow |
| D2 M&A | R&W·MAC(Material Adverse Change)·Closing Condition·Earn-out |
| D3 상업거래 | SLA·Acceptance·Warranty·Indemnity·Payment Terms |
| D4 노무 | 임금·근로시간·휴일·연차·퇴직금·비경쟁·직무발명 |
| D5 IP·데이터 | 라이선스 범위·Sublicense·Audit·DPA 9항목 |
| D6 부동산 | 임대료·보증금·관리비·원상복구·갱신·해지 |
| D7 건설·공공 | 공사기간·기성·하자보증·지체상금·준공검사 |
