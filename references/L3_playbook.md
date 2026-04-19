# L3 PLAYBOOK — Tier1/2/3 협상 경로

계약검토의 핵심 산출. 단일 권고 ✗, 3-Tier 필수. 출처: LegalOn·Spellbook·Harvard PON(BATNA·ZOPA).

## 3-Tier 구조

| Tier | 정의 | 의미 | 시기 |
|------|-----|-----|-----|
| **Tier1 허용안 (Primary)** | 우리 Standard Position | 첫 제안·초안에 삽입 | 초기 |
| **Tier2 협상안 (Fallback)** | 수용 가능한 대안 | 상대방 반대 시 양보안 | 중기 |
| **Tier3 마지노선 (Floor/Walk-away)** | 이 밑은 계약 결렬 | 최후 방어선 | 클로징 직전 |

## BATNA·ZOPA 연동

### BATNA (Best Alternative to Negotiated Agreement)
**질문:** "이 계약 결렬되면 뭐 할 건가?" = 협상 결렬 시 최선 대안
- 강한 BATNA → 공격적 Tier1, 낮은 Tier3
- 약한 BATNA → 방어적 Tier1, 유연한 Tier3

### ZOPA (Zone of Possible Agreement)
**정의:** 양측 Reservation Price 사이 중첩 영역
- 양측 Tier3가 겹치면 ZOPA 존재 → 계약 가능
- 겹치지 않으면 ZOPA 없음 → 재설계 or 결렬

## Playbook 작성 템플릿

```markdown
### 조항: [조항명 / §번호]

**현재 조항 (as-is):**
> "[원문 인용]"

**리스크 평가:** [Red/Yellow/Green]
**근거:** [Redflag 분류 / 법령 위반 / 업계 대비 이상]

---

**Tier1 허용안 (Primary):**
> "[수정안 1 - 우리 Standard]"

**근거·Why:** 업계 표준. 예) "2025 SaaS MSA 일반 실무"

---

**Tier2 협상안 (Fallback):**
> "[수정안 2 - 양보 수용안]"

**트리거:** 상대방이 Tier1 전면 거부 시
**Concession:** [무엇을 양보하는가 - Cap 확대, Carve-out 추가, 기간 연장 등]

---

**Tier3 마지노선 (Floor):**
> "[수정안 3 - 최후 방어선]"

**Walk-away 조건:** 이 밑이면 계약 포기. 근거: [법적 무효 / 비즈 불가능 / 평판 리스크]

---

**참고 레버리지:**
- BATNA: [결렬 시 대안]
- 상대방 약점: [알려진 협상 포인트]
- 업계 벤치마크: [유사 계약 사례]
```

## 핵심 조항별 Tier 표준 (예시)

### Liability Cap
| Tier | 내용 |
|------|-----|
| Tier1 | 12개월 fees 또는 계약금액 1x (낮은 쪽) |
| Tier2 | 2x, IP/기밀/고의 Carve-out |
| Tier3 | Uncapped 수용 시 보험 부보 의무 |

### Indemnity
| Tier | 내용 |
|------|-----|
| Tier1 | 상호 indemnity, 제3자 IP 클레임만 |
| Tier2 | Unilateral indemnity 수용하되 Cap = 계약금액 |
| Tier3 | Defense only, Hold Harmless ✗ |

### Termination
| Tier | 내용 |
|------|-----|
| Tier1 | For Cause만, Cure Period 30일 |
| Tier2 | For Convenience 허용하되 Notice 90일 + Termination Fee |
| Tier3 | Notice 180일 + 잔존 의무 명시 |

### IP Ownership
| Tier | 내용 |
|------|-----|
| Tier1 | Work Product만 양도, Background IP 유보 |
| Tier2 | Full Assignment + Perpetual License (Background IP) |
| Tier3 | Work Product 양도 + Background IP 라이선스 (기한·범위 제한) |

### Governing Law / Venue
| Tier | 내용 |
|------|-----|
| Tier1 | 한국법, 서울중앙지법 |
| Tier2 | 한국법, 대한상사중재원(KCAB) |
| Tier3 | 제3국 중재 (SIAC·HKIAC) |

## 주의
- **모든 Tier는 법적으로 유효해야 함** — Tier3도 약관법·공정거래 등 위반 ✗
- **업계 벤치마크 필수** — "표준"은 업계·도메인별 상이
- **BATNA 약한 경우** Tier1을 너무 강하게 쓰면 협상 결렬 → 시그널링 고려
