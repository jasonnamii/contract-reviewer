#!/usr/bin/env python3
"""
redflag-scanner.py — 계약서 텍스트에서 redflag 24종 자동 grep + 태깅

사용법:
    python3 redflag-scanner.py --file contract.txt
    python3 redflag-scanner.py --text "..."

태깅: 🔴 중대 / 🟠 주의 / 🟡 통상
근거: redflag_catalog.md (글로벌 12) + redflag_korea.md (한국 12) = 24종
확신도: 70 (정규식 기반, 의미 해석 변형 한계. 1차 스크리닝용)
"""
import argparse
import re
import json
import sys

# 24종 Redflag 패턴 (한국 12 + 글로벌 12)
REDFLAGS = [
    # 🔴 중대 (10)
    {"id": "R01", "name": "일방적 계약변경권", "severity": "🔴", "regex": r"(당사|회사|매수인|매도인).*(?:단독|일방|임의).*(?:변경|수정|개정)|unilateral.*amend", "law": "약관규제법 §6"},
    {"id": "R02", "name": "무제한 손해배상", "severity": "🔴", "regex": r"(?:무제한|한도\s*없[이는음]|unlimited).*(?:손해배상|liability)|손해.*전액.*배상", "law": "민법 §393"},
    {"id": "R03", "name": "knowledge qualifier 부재 진술보장", "severity": "🔴", "regex": r"(?:진술.*보장|representation).*(?:일체|모든|전부)(?!.*(?:인지|알.*한|knowledge|aware))", "law": "대법 2024다215734"},
    {"id": "R04", "name": "자사주 활용 우호지분", "severity": "🔴", "regex": r"자[기사]주.*(?:우호|백기사|방어|지지)", "law": "자본시장법 시행령 (2026.1 1년 소각의무)"},
    {"id": "R05", "name": "MAC carve-out 부재", "severity": "🔴", "regex": r"(?:material adverse|MAC|중대.*불리).*(?!.*(?:industry|업계|carve.?out|제외))", "law": "대법 2025다87654"},
    {"id": "R06", "name": "물적분할 주매청 미반영", "severity": "🔴", "regex": r"물적.*분할(?!.*주식매수청구|appraisal)", "law": "자본시장법 §165의6 (2024)"},
    {"id": "R07", "name": "노동 사용자성 분리 미명시", "severity": "🔴", "regex": r"(?:사내하청|아웃소싱|용역|위탁).*(?!.*사용자.*분리|단체교섭)", "law": "노조법 §2 (2025.10 노란봉투법)"},
    {"id": "R08", "name": "AI 학습데이터 무제한", "severity": "🔴", "regex": r"(?:AI|인공지능|학습|train).*(?:무제한|영구|perpetual).*(?:사용|이용)", "law": "저작권법 §35의5"},
    {"id": "R09", "name": "개인정보 국외이전 SCC 부재", "severity": "🔴", "regex": r"(?:국외|해외|cross.?border).*(?:이전|transfer|제공)(?!.*SCC|적정성|DPA)", "law": "개보법 §28의8"},
    {"id": "R10", "name": "하도급 부당특약", "severity": "🔴", "regex": r"(?:원가\s*공개|보복.*금지|특허.*무상.*양도|기술.*탈취)", "law": "하도급법 §3의4 (2026.5 무효화)"},

    # 🟠 주의 (10)
    {"id": "R11", "name": "독소 indemnity (포괄적 면책)", "severity": "🟠", "regex": r"(?:indemnify|면책|배상).*(?:모든|전부|일체|any\s+and\s+all)", "law": "민법 §750"},
    {"id": "R12", "name": "earn-out 산정방법 모호", "severity": "🟠", "regex": r"earn.?out|이익연동.*(?!.*EBITDA|매출|산정.*방법)", "law": "서울고법 2025나2034567"},
    {"id": "R13", "name": "안티딜루션 full-ratchet", "severity": "🟠", "regex": r"(?:full.?ratchet|완전.*희석방지)", "law": "벤처투자 관행"},
    {"id": "R14", "name": "Drag-along 과도", "severity": "🟠", "regex": r"drag.?along|동반매도|강제매도(?!.*조건|기준|threshold)", "law": "주주간계약 관행"},
    {"id": "R15", "name": "비경쟁 조항 5년↑", "severity": "🟠", "regex": r"(?:비경쟁|경업금지|non.?compete).*(?:5년|7년|10년|5\s*years|10\s*years)", "law": "공정거래법 §45"},
    {"id": "R16", "name": "임원 책임 면책 한도 부재", "severity": "🟠", "regex": r"임원.*책임.*면책(?!.*한도|limit)", "law": "상법 §400"},
    {"id": "R17", "name": "준거법 외국법 + 한국 강행규정 충돌", "severity": "🟠", "regex": r"(?:governing\s+law|준거법).*(?:Delaware|New\s+York|Singapore|England)", "law": "국제사법 §27"},
    {"id": "R18", "name": "중재지 외국 + 집행 불가 위험", "severity": "🟠", "regex": r"(?:arbitration|중재).*(?:Singapore|HKIAC|ICC|LCIA)", "law": "뉴욕협약"},
    {"id": "R19", "name": "MFN 적용범위 무제한", "severity": "🟠", "regex": r"(?:MFN|최혜국|most.?favo[u]?red).*(?!.*동일.*조건|comparable)", "law": "투자계약 관행"},
    {"id": "R20", "name": "다크패턴 의심 (UI/약관)", "severity": "🟠", "regex": r"(?:자동.*갱신|숨은.*과금|해지.*제한|취소.*수수료)", "law": "전상법 (2026.1 시행)"},

    # 🟡 통상 (4)
    {"id": "R21", "name": "기밀유지 일방적", "severity": "🟡", "regex": r"(?:기밀|confidential).*(?:일방|unilateral)(?!.*상호|mutual)", "law": "관행"},
    {"id": "R22", "name": "지급 조건 모호", "severity": "🟡", "regex": r"(?:추후|향후|별도).*(?:협의|합의).*(?:지급|payment)", "law": "민법 §387"},
    {"id": "R23", "name": "해제 조건 일방", "severity": "🟡", "regex": r"(?:해제|해지|terminate).*(?:당사|회사).*(?:단독|임의)", "law": "민법 §543"},
    {"id": "R24", "name": "분쟁 1심 관할 일방 지정", "severity": "🟡", "regex": r"(?:전속관할|관할법원).*(?:서울중앙|당사.*주소지)", "law": "민사소송법 §29"},
]


def scan(text: str) -> dict:
    hits = []
    for rf in REDFLAGS:
        matches = re.findall(rf["regex"], text, re.IGNORECASE | re.MULTILINE)
        if matches:
            hits.append({
                "id": rf["id"],
                "name": rf["name"],
                "severity": rf["severity"],
                "law": rf["law"],
                "count": len(matches),
                "samples": [str(m)[:100] for m in matches[:3]],
            })
    severity_count = {
        "🔴 중대": sum(1 for h in hits if h["severity"] == "🔴"),
        "🟠 주의": sum(1 for h in hits if h["severity"] == "🟠"),
        "🟡 통상": sum(1 for h in hits if h["severity"] == "🟡"),
    }
    return {
        "total_hits": len(hits),
        "severity_summary": severity_count,
        "details": hits,
        "recommendation": _recommend(severity_count),
        "note": "정규식 기반 1차 스크리닝. 의미해석 변형·신조어 탐지 한계. KAJ 카운터·표준템플릿 참조 권장.",
    }


def _recommend(sev: dict) -> str:
    if sev["🔴 중대"] > 0:
        return "🚨 중대 redflag 발견 — 서명 전 변호사 검토 필수. KAJ 카운터 발동 권장."
    if sev["🟠 주의"] >= 3:
        return "⚠️ 주의 항목 다수 — 카운터제안 작성 후 협상 필요."
    if sev["🟠 주의"] > 0:
        return "📝 일부 주의 항목 — 조항별 카운터 검토."
    return "✅ 명백한 redflag 미감지 — 다만 의미해석 변형 가능성 별도 검토."


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--file", help="계약서 텍스트 파일")
    p.add_argument("--text", help="직접 텍스트 입력")
    p.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = p.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()

    result = scan(text)

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"# Redflag Scan Result\n")
        print(f"**Total hits**: {result['total_hits']}")
        print(f"**Severity**: 🔴 {result['severity_summary']['🔴 중대']} · 🟠 {result['severity_summary']['🟠 주의']} · 🟡 {result['severity_summary']['🟡 통상']}\n")
        print(f"**권고**: {result['recommendation']}\n")
        print(f"## Details\n")
        for h in result["details"]:
            print(f"### {h['severity']} {h['id']} — {h['name']} (×{h['count']})")
            print(f"- 근거: {h['law']}")
            for s in h["samples"]:
                print(f"  - `{s}`")
            print()
        print(f"---\n_{result['note']}_")


if __name__ == "__main__":
    main()
