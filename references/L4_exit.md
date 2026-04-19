# L4 EXIT — 종료·해지·잔존의무

계약 마무리 시나리오 설계. CLM 6단계의 "갱신·종료" 구체화.

## 종료 유형 5가지

### E1. Natural Expiration (기간만료)
- 정해진 기간 경과 → 자동 종료
- 체크: 자동갱신(Auto-Renewal) 조항·Notice 기한

### E2. Termination for Convenience (편의해지)
- 사유 불요, Notice만으로 해지
- 체크: 양방 or 편측 / Notice 기간 / Termination Fee

### E3. Termination for Cause (정당사유 해지)
- 중대 위반 시 해지권 발동
- 체크: Material Breach 정의 / Cure Period / Cross-default

### E4. Termination for Change of Control (지배권 변동)
- M&A·경영권 변동 시 상대방 해지권
- 체크: Trigger 정의 / Notice·동의 필요 여부

### E5. Termination by Operation of Law (법령에 의한)
- 파산·청산·해산 / 허가 취소 / 위법화
- 체크: Automatic vs Optional

## Cure Period (치유기간)

| 위반 유형 | 표준 Cure Period |
|---------|-----------------|
| Payment Default | 10-15일 |
| Performance Default | 30일 |
| Material Breach (기타) | 30-60일 |
| IP Infringement | 즉시 (치유 불가 시 Cure 면제) |
| Confidentiality Breach | 일반적으로 Cure 불가 |

**한국 특이:** 민법 544조 최고(催告) 절차 필수 (K8 참조).

## 잔존 의무 (Surviving Obligations)

계약 종료 후에도 효력 유지하는 조항들:

| 조항 | 일반 Survival 기간 |
|------|-----------------|
| Confidentiality | 3-5년 (Trade Secret 영구) |
| IP Ownership | 영구 |
| Indemnity (pre-termination) | Statute of Limitations까지 |
| Payment for services rendered | 지급완료까지 |
| Governing Law / Dispute Resolution | 영구 |
| Audit Rights | 1-2년 |

**작성법:** "The following sections shall survive termination: §X, §Y, §Z"

## 해지 Consequences (결과)

종료 시 처리해야 할 것들:

```
[ ] 반환 의무 (Confidential Info, Documents, Equipment)
[ ] 파기 의무 (Personal Data per DPA)
[ ] 미지급금 정산 (Pro-rata, Outstanding Invoice)
[ ] Work Product 인도
[ ] 라이선스 Perpetual/Terminate 명시
[ ] Transition Support (협조 의무)
[ ] Non-Solicitation (채용 제한 기간)
[ ] Exit Interview·최종 회계감사
```

## 체크리스트

```
[ ] Expiration Date / Auto-Renewal 조건
[ ] Termination Triggers (5유형 중 어느 것 허용)
[ ] Cure Period (한국 민법 최고 절차 포함)
[ ] Termination Fee 유무·금액
[ ] Surviving Obligations 명시
[ ] Post-Termination 반환·파기·정산
[ ] Transition Assistance
[ ] Change of Control Rights
[ ] Bankruptcy/Insolvency 조항
[ ] 분쟁해결 조항의 Survival
```

## 산출 포맷

```markdown
### L4 종료 시나리오

#### 종료 트리거 (허용된 유형)
| 유형 | 조건 | Notice | Cure |
|------|-----|------|------|
| E2 편의해지 | 양방 | 90일 | - |
| E3 정당사유 | Material Breach | 30일 | 30일 |

#### 잔존 조항
- §Confidentiality (5년)
- §IP Ownership (영구)
- §Indemnity (3년)

#### 종료 시 처리
[ ] 반환 / 파기 / 정산 / Transition

#### 리스크
- [Gap 발견 사항]
```
