# L2 RISK — 리스크 식별·배분

3×3 Probability × Impact 매트릭스. 출처: Sirion·Optro·Risk Allocation Matrix (FIDIC·건설·금융 표준).

## 3×3 스코어링

|            | Impact 저(1) | 중(2) | 고(3) |
|-----------|-------------|------|------|
| **확률 고(3)** | 3 Yellow | 6 Red | 9 Red |
| **확률 중(2)** | 2 Green | 4 Yellow | 6 Red |
| **확률 저(1)** | 1 Green | 2 Green | 3 Yellow |

- Score ≥ 5 = 법무 재검토 필수
- Score ≥ 7 = Tier3 마지노선, Walk-away 고려

## 리스크 3대 카테고리

### R1. Financial (재무)
- Payment Default (미지급)
- FX Risk (환율변동)
- Cost Overrun (비용초과)
- Liquidated Damages (위약금)
- Indemnity Exposure (보상노출)

### R2. Legal (법률)
- Regulatory Change (법령 변경)
- IP Infringement (IP 침해)
- Privacy/Data Breach (개인정보 유출)
- Antitrust (독점금지)
- Licensing (인허가)

### R3. Operational (운영)
- Supply Chain (공급망)
- Performance Shortfall (성과미달)
- Personnel (인력변동)
- Technology Obsolescence (기술노후화)
- Force Majeure (불가항력)

## 배분 원칙 (Risk Allocation)

### 기본 원칙
**"리스크는 가장 잘 제어·예방·흡수할 수 있는 당사자에게 배분"**

### 배분 도구
| 도구 | 용도 | 한계 |
|------|-----|-----|
| **Cap** | 배상 상한 | 계약금액 1-2x 권장 |
| **Carve-out** | Cap 예외 (IP·기밀·고의) | 남용 시 Cap 무력화 |
| **Basket** (Deductible) | 최소 청구 금액 | Tipping vs Deductible 구분 |
| **Escrow** | 사후 지급·보증 | 금액·기간·해제조건 |
| **Insurance** | 리스크 이전 | 부보범위·한도 확인 |
| **Indemnity** | 제3자 클레임 방어 | Defense·Settlement 구분 |
| **Representation & Warranty** | 진술·보장 (사전 리스크) | Survival·Indemnity 연결 |
| **MAC Clause** | 중대한 부정적 변경 | M&A 필수 |

## 검토 체크리스트

```
[ ] Cap 존재? (금액·기간·유형)
[ ] Carve-out 합리? (IP·기밀·고의만 or 과다)
[ ] Indemnity 범위 (제3자 클레임만 or 직접 손해 포함)
[ ] Defense vs Hold Harmless 구분
[ ] R&W Survival 기간 (일반 12-18개월, Tax 7년)
[ ] Basket/Deductible 금액
[ ] Force Majeure 트리거·기간·결과
[ ] MAC 정의 (정량 기준 or 정성)
[ ] 보험 의무 (유형·한도·증명)
[ ] 분쟁해결·관할·준거법
```

## 산출 포맷

```markdown
### L2 리스크 매트릭스

#### 식별된 리스크 (N개)
| # | 리스크 | 카테고리 | 확률(1-3) | 임팩트(1-3) | 스코어 | 배분 도구 |
|---|-------|---------|---------|----------|-------|---------|
| 1 | IP 침해 소송 | Legal | 2 | 3 | 6 Red | Indemnity+Insurance |

#### Cap·Carve-out 진단
- Cap: [금액·기간]
- Carve-out: [범위]
- 평가: [적정/부족/과다]

#### 권고사항
- Tier1: [표준안]
- Tier2: [협상안]
- Tier3: [마지노선]
```
