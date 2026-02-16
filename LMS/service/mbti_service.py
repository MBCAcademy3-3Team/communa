class MbtiService:
    # 질문 리스트 (E/I: 1-3, S/N: 4-6, T/F: 7-9, J/P: 10-12)
    QUESTIONS = [
        # 1. E vs I (협업 스타일)
        {
            "id": 1,
            "dimension": "EI",
            "question": "치명적인 버그가 발생했다! 해결해야 하는데...",
            "answers": [
                {"type": "E", "text": "동료들에게 상황을 알리고 다 같이 모여서 '집단 지성'으로 해결한다."},
                {"type": "I", "text": "일단 이어폰을 꽂고 로그부터 깊게 파고들어 혼자 원인을 찾는다."}
            ]
        },
        {
            "id": 2,
            "dimension": "EI",
            "question": "새로운 기술 스택을 도입해야 한다면?",
            "answers": [
                {"type": "E", "text": "팀원들과 스터디나 세미나를 열어 같이 토론하며 배운다."},
                {"type": "I", "text": "공식 문서나 강의를 보며 혼자 튜토리얼부터 따라 해본다."}
            ]
        },
        {
            "id": 3,
            "dimension": "EI",
            "question": "가장 선호하는 업무 환경은?",
            "answers": [
                {"type": "E", "text": "활발하게 의견이 오가는 개방형 오피스나 카페."},
                {"type": "I", "text": "아무도 말을 걸지 않는 조용한 새벽 시간이나 재택근무."}
            ]
        },
        # 2. S vs N (구현 관점)
        {
            "id": 4,
            "dimension": "SN",
            "question": "기획서에 없는 기능이 필요해 보인다. 당신의 선택은?",
            "answers": [
                {"type": "S", "text": "일단 기획서(스펙)대로 정확하게 구현하는 것이 우선이다."},
                {"type": "N", "text": "미래에 필요할 것 같으니, 확장성을 고려해 미리 구조를 잡아둔다."}
            ]
        },
        {
            "id": 5,
            "dimension": "SN",
            "question": "코드를 짤 때 더 중요하게 생각하는 것은?",
            "answers": [
                {"type": "S", "text": "당장 에러 없이 잘 돌아가는 '실용적인 코드'."},
                {"type": "N", "text": "중복을 제거하고 재사용성을 높인 '우아한 추상화 코드'."}
            ]
        },
        {
            "id": 6,
            "dimension": "SN",
            "question": "새 프로젝트를 시작할 때 나는?",
            "answers": [
                {"type": "S", "text": "검증된 라이브러리와 익숙한 패턴을 사용하여 안정성을 확보한다."},
                {"type": "N", "text": "요즘 핫하다는 신기술이나 새로운 아키텍처를 도입해보고 싶다."}
            ]
        },
        # 3. T vs F (리뷰 및 의사결정)
        {
            "id": 7,
            "dimension": "TF",
            "question": "동료의 코드 리뷰를 할 때 나는?",
            "answers": [
                {"type": "T", "text": "비효율적인 로직은 가차 없이 지적한다. (성능이 중요하니까!)"},
                {"type": "F", "text": "노고를 인정해주고, 조심스럽게 개선점을 제안한다. (상처받으면 안 되니까!)"}
            ]
        },
        {
            "id": 8,
            "dimension": "TF",
            "question": "라이브러리를 선택하는 기준은?",
            "answers": [
                {"type": "T", "text": "벤치마크 점수, 성능 지표, 다운로드 수 등 객관적 데이터."},
                {"type": "F", "text": "개발자 커뮤니티의 평판, 사용 편의성, 읽기 좋은 문서."}
            ]
        },
        {
            "id": 9,
            "dimension": "TF",
            "question": "팀원과 기술적인 의견 충돌이 발생했다.",
            "answers": [
                {"type": "T", "text": "누가 맞는지 끝까지 논리적으로 따져서 정답을 찾는다."},
                {"type": "F", "text": "팀의 분위기를 해치지 않는 선에서 서로 양보하며 절충안을 찾는다."}
            ]
        },
        # 4. J vs P (일정 관리)
        {
            "id": 10,
            "dimension": "JP",
            "question": "프로젝트 폴더 구조를 잡을 때 나는?",
            "answers": [
                {"type": "J", "text": "처음부터 컨벤션을 정하고 폴더 구조를 완벽하게 세팅하고 시작한다."},
                {"type": "P", "text": "일단 파일을 만들면서 코딩하다가, 나중에 필요하면 정리한다."}
            ]
        },
        {
            "id": 11,
            "dimension": "JP",
            "question": "개발 일정 관리 스타일은?",
            "answers": [
                {"type": "J", "text": "기능별로 데드라인을 쪼개서 계획대로 착착 진행한다."},
                {"type": "P", "text": "필 받은 날 밤새서 몰아서 개발하고, 안 될 땐 좀 쉰다."}
            ]
        },
        {
            "id": 12,
            "dimension": "JP",
            "question": "배포 날짜가 다가왔다!",
            "answers": [
                {"type": "J", "text": "이미 테스트까지 마쳤다. 여유롭게 배포 버튼을 누른다."},
                {"type": "P", "text": "막판 스퍼트! 버그 수정과 기능 추가를 배포 직전까지 한다."}
            ]
        }
    ]

    # MBTI 유형별 결과 데이터
    RESULTS = {
        "ISTJ": {"animal": "소금쟁이", "title": "현실적인 클린코더", "desc": "정해진 규칙과 원칙을 준수하며, 빈틈없는 코드를 작성하는 모범생 개발자입니다."},
        "ISFJ": {"animal": "꿀벌", "title": "친절한 수호자", "desc": "팀의 평화를 지키며, 보이지 않는 곳에서 묵묵히 레거시 코드를 유지 보수하는 천사입니다."},
        "INFJ": {"animal": "판다", "title": "통찰력 있는 예언자", "desc": "코드 이면에 있는 사용자 경험까지 고려하며, 팀의 정신적 지주 역할을 합니다."},
        "INTJ": {"animal": "독수리", "title": "고독한 아키텍트", "desc": "큰 그림을 그리며 시스템의 구조를 설계하는 것을 즐깁니다. 혼자 일할 때 가장 효율이 좋습니다."},
        "ISTP": {"animal": "고양이", "title": "만능 해결사", "desc": "필요한 최소한의 노력으로 최대의 효율을 냅니다. 디버깅의 귀재입니다."},
        "ISFP": {"animal": "토끼", "title": "감성적인 장인", "desc": "기능 구현뿐만 아니라 UI/UX의 디테일과 코드의 미적 아름다움을 중요하게 생각합니다."},
        "INFP": {"animal": "거북이", "title": "꿈꾸는 개발자", "desc": "이상적인 코드를 꿈꾸며, 자유로운 분위기에서 창의적인 기능을 만들어냅니다."},
        "INTP": {"animal": "부엉이", "title": "논리적인 사색가", "desc": "주어진 문제의 근본 원인을 파고듭니다. 코딩보다 설계와 아이디어 구상에 시간을 더 씁니다."},
        "ESTP": {"animal": "치타", "title": "현란한 버그 사냥꾼", "desc": "빠른 실행력으로 프로토타입을 순식간에 만들어냅니다. 일단 돌려보고 고치는 스타일입니다."},
        "ESFP": {"animal": "강아지", "title": "분위기 메이커", "desc": "즐겁게 일하는 것을 최우선으로 둡니다. 팀 회식과 해커톤을 사랑하는 인싸 개발자입니다."},
        "ENFP": {"animal": "돌고래", "title": "열정적인 스파크", "desc": "새로운 기술에 호기심이 많고, 팀원들에게 영감을 주는 아이디어 뱅크입니다."},
        "ENTP": {"animal": "원숭이", "title": "논쟁을 즐기는 발명가", "desc": "기존의 방식에 끊임없이 '왜?'를 던지며 혁신적인(때론 위험한) 리팩토링을 시도합니다."},
        "ESTJ": {"animal": "사자", "title": "엄격한 관리자", "desc": "프로젝트의 일정을 효율적으로 관리하고, 명확한 지시로 팀을 이끄는 리더형입니다."},
        "ESFJ": {"animal": "코끼리", "title": "사교적인 외교관", "desc": "동료들의 어려움을 잘 도와주며, 협업 툴과 문서를 꼼꼼하게 관리하여 팀을 돕습니다."},
        "ENFJ": {"animal": "리트리버", "title": "정의로운 멘토", "desc": "팀원들의 성장을 돕는 것을 좋아하며, 기술 공유와 코드 리뷰에 적극적입니다."},
        "ENTJ": {"animal": "호랑이", "title": "대담한 통솔자", "desc": "기술적 난관 앞에서도 주눅 들지 않고 팀을 진두지휘하여 목표를 달성해냅니다."}
    }

    @staticmethod
    def get_questions():
        return MbtiService.QUESTIONS

    @staticmethod
    def calculate_mbti(answers):
        # answers 예시: {'1': 'E', '2': 'I', ...}
        scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

        for ans in answers.values():
            if ans in scores:
                scores[ans] += 1

        mbti = ""
        mbti += "E" if scores['E'] >= scores['I'] else "I"
        mbti += "S" if scores['S'] >= scores['N'] else "N"
        mbti += "T" if scores['T'] >= scores['F'] else "F"
        mbti += "J" if scores['J'] >= scores['P'] else "P"

        return mbti, MbtiService.RESULTS.get(mbti)