# D5 — IP·데이터 계약

대표 계약: NDA, IP 양도, 기술라이선스, DPA, SaaS MSA, 공동개발(JDA).

## 필수 조항

### NDA
- **Definition of Confidential Info** — 범위
- **Permitted Use** — 목적 제한
- **Excluded Info** — 공지·독립개발·제3자 취득
- **Term of Confidentiality** — 3-5년 (Trade Secret 영구)
- **Return / Destruction** — 종료 시
- **No License** — 정보 제공 ≠ 라이선스 부여

### IP License
- **Licensed IP** — 특허·저작권·상표·영업비밀 구체
- **Grant** — Exclusive/Non-exclusive, Sublicense, Territory, Field
- **Term** — 기간·갱신
- **Royalty** — 고정·수수료·Milestone
- **Audit Rights** — 회계감사
- **Improvements** — 소유·라이선스
- **IP Indemnity** — 제3자 클레임

### DPA (데이터 처리 위탁)
**개인정보보호법 제26조 필수 9항목:**
1. 위탁업무 목적·범위
2. 처리방법
3. 위탁기간
4. 재위탁 제한
5. 안전조치 의무
6. 관리·감독
7. 손해배상
8. 목적달성 후 파기
9. 정보주체 권리 보장

**GDPR 병렬 시 추가:**
- Data Subject Rights (Article 28)
- Sub-processor list 공개
- Breach Notification 72h
- SCC (Standard Contractual Clauses) for Cross-border

### SaaS MSA
- **Service Description** — 기능·가동률
- **User Access** — 라이선스 수·Identity
- **Data Ownership** — 고객 데이터 소유
- **Data Export / Portability** — 종료 시 반환
- **Uptime SLA** — 99.9% 등·Service Credit
- **Security** — SOC2·ISO27001 등 인증
- **Subprocessor** — 제3자 공개·동의

## Domain-Specific Redflag
- NDA Perpetual Confidentiality (Trade Secret 외 무기한)
- IP Assignment 대신 Full License (범위 미정)
- DPA 9항목 미충족
- SaaS 데이터 반환 절차 부재
- Cross-border transfer에 적법성 조치 부재 (GDPR·PIPA)

## L5 Korea 연결
- **K-F 개인정보보호법:** DPA 9항목 필수, 2025.4 처리방침 지침
- **특허법·저작권법·부정경쟁방지법**
- **K-A 민법 제398:** 손해배상 예정액 감액

## Tier 표준
- DPA: 9항목 전수 필수 (협상 여지 없음, 미기재 = 위법)
- Cross-border: Tier1 한국 내 저장 / Tier2 SCC+적정성 / Tier3 명시적 동의
- Trade Secret: 기간 제한 없음 허용
