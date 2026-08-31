python
import streamlit as st

# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="꿈꾸는 나침반",
    page_icon="🧭",
    layout="centered"
)

# =========================================================
# 스타일
# =========================================================

st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background: #F4FBF8;
    }

    /* 기본 글씨 */
    html, body, [class*="css"] {
        font-family: "Pretendard", "Noto Sans KR", sans-serif;
    }

    /* 제목 */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #315C52;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6D8580;
        margin-bottom: 25px;
    }

    /* 페이지 헤더 */
    .page-title {
        font-size: 32px;
        font-weight: 800;
        color: #315C52;
        margin-bottom: 5px;
    }

    .page-description {
        color: #718681;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* 카드 */
    .card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 12px 0;
        border: 1px solid #DDEDE8;
        box-shadow: 0 5px 18px rgba(70, 120, 105, 0.08);
    }

    .career-number {
        display: inline-block;
        background: #DDF4EC;
        color: #397466;
        border-radius: 50px;
        padding: 5px 12px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .career-title {
        font-size: 23px;
        font-weight: 800;
        color: #315C52;
        margin-bottom: 8px;
    }

    .career-description {
        color: #687D78;
        line-height: 1.7;
    }

    /* MBTI 카드 */
    .mbti-card {
        background: #E8F7F1;
        border-radius: 20px;
        padding: 22px;
        margin: 15px 0 25px 0;
        border: 1px solid #D2ECE3;
    }

    .mbti-name {
        font-size: 24px;
        font-weight: 800;
        color: #315C52;
    }

    .mbti-description {
        color: #637B75;
        margin-top: 8px;
    }

    /* TIP 카드 */
    .tip-card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        margin: 12px 0;
        border-left: 6px solid #9BD8C6;
        box-shadow: 0 4px 14px rgba(70, 120, 105, 0.07);
    }

    .tip-title {
        font-size: 19px;
        font-weight: 750;
        color: #315C52;
    }

    .tip-text {
        color: #687D78;
        line-height: 1.7;
        margin-top: 6px;
    }

    /* 하단 안내 */
    .footer {
        text-align: center;
        color: #91A7A1;
        font-size: 13px;
        padding: 30px 0 10px 0;
    }

    /* Streamlit 버튼 */
    div.stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid #C9E8DE;
        background: white;
        color: #397466;
        font-weight: 700;
        padding: 12px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #83C9B5;
        background: #E8F7F1;
        color: #315C52;
    }

    /* 선택창 */
    div[data-baseweb="select"] > div {
        border-radius: 14px;
        border-color: #C9E8DE;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# MBTI 데이터
# =========================================================

CAREERS = {
    "ISTJ": {
        "title": "신중하고 책임감 있는 현실주의자",
        "description": "체계적으로 계획하고 맡은 일을 끝까지 책임지는 성향이에요.",
        "jobs": [
            ("회계사", "숫자와 자료를 꼼꼼하게 다루는 능력을 활용할 수 있어요."),
            ("공무원", "규칙과 절차에 따라 꾸준하고 책임감 있게 일하는 데 잘 맞을 수 있어요."),
            ("품질관리원", "제품이나 서비스가 기준에 맞는지 꼼꼼하게 확인하는 직업이에요.")
        ]
    },
    "ISFJ": {
        "title": "따뜻하고 책임감 있는 수호자",
        "description": "다른 사람을 세심하게 살피고 맡은 일을 성실하게 해내는 성향이에요.",
        "jobs": [
            ("간호사", "사람을 세심하게 관찰하고 도움을 주는 능력을 활용할 수 있어요."),
            ("사회복지사", "사람들의 어려움을 이해하고 도움을 제공하는 직업이에요."),
            ("교사", "학생들을 꾸준히 관찰하고 성장하도록 도울 수 있어요.")
        ]
    },
    "INFJ": {
        "title": "통찰력 있는 이상주의자",
        "description": "사람을 이해하고 의미 있는 목표를 추구하는 성향이에요.",
        "jobs": [
            ("상담심리사", "다른 사람의 이야기를 듣고 이해하는 능력을 활용할 수 있어요."),
            ("작가", "자신의 생각과 가치관을 이야기로 표현할 수 있어요."),
            ("사회복지사", "사회 문제에 관심을 가지고 사람들에게 도움을 줄 수 있어요.")
        ]
    },
    "INTJ": {
        "title": "전략적인 계획가",
        "description": "논리적으로 생각하고 장기적인 목표를 세우는 성향이에요.",
        "jobs": [
            ("소프트웨어 개발자", "복잡한 문제를 논리적으로 분석하고 해결하는 능력을 활용할 수 있어요."),
            ("연구원", "하나의 주제를 깊게 탐구하고 새로운 해결책을 찾을 수 있어요."),
            ("데이터 분석가", "데이터에서 의미 있는 패턴과 결과를 찾아낼 수 있어요.")
        ]
    },
    "ISTP": {
        "title": "실용적인 문제 해결사",
        "description": "직접 문제를 해결하고 새로운 방법을 시도하는 성향이에요.",
        "jobs": [
            ("기계공학자", "기계의 원리를 이해하고 실제 문제를 해결하는 능력이 중요해요."),
            ("프로그래머", "논리적인 사고를 활용하여 실제로 작동하는 프로그램을 만들어요."),
            ("응급구조사", "긴급한 상황에서 빠르게 판단하고 행동해야 하는 직업이에요.")
        ]
    },
    "ISFP": {
        "title": "감각적인 예술가",
        "description": "자신만의 감각과 가치관을 중요하게 생각하는 성향이에요.",
        "jobs": [
            ("디자이너", "자신의 감각과 창의성을 활용하여 결과물을 만들 수 있어요."),
            ("사진작가", "자신만의 시각으로 세상을 표현할 수 있어요."),
            ("수의사", "동물을 세심하게 관찰하고 돌보는 능력을 활용할 수 있어요.")
        ]
    },
    "INFP": {
        "title": "창의적인 이상주의자",
        "description": "자신의 가치관과 상상력을 중요하게 생각하는 성향이에요.",
        "jobs": [
            ("작가", "풍부한 상상력과 생각을 이야기로 표현할 수 있어요."),
            ("콘텐츠 기획자", "새로운 아이디어를 콘텐츠로 발전시킬 수 있어요."),
            ("상담 관련 직업", "다른 사람의 감정을 이해하고 공감하는 능력을 활용할 수 있어요.")
        ]
    },
    "INTP": {
        "title": "논리적인 탐구자",
        "description": "새로운 지식을 탐구하고 원리를 분석하는 것을 좋아하는 성향이에요.",
        "jobs": [
            ("AI 연구원", "인공지능의 원리를 연구하고 새로운 기술을 개발해요."),
            ("소프트웨어 개발자", "논리적인 사고를 활용하여 프로그램의 문제를 해결해요."),
            ("과학 연구원", "궁금한 현상을 분석하고 새로운 지식을 발견해요.")
        ]
    },
    "ESTP": {
        "title": "행동력 있는 도전자",
        "description": "현실적인 상황에 빠르게 대응하고 직접 행동하는 성향이에요.",
        "jobs": [
            ("영업 전문가", "사람들과 직접 소통하고 상황에 맞게 문제를 해결해요."),
            ("기업가", "새로운 기회를 발견하고 직접 행동으로 옮길 수 있어요."),
            ("경찰관", "현장에서 상황을 빠르게 판단하고 대응해야 해요.")
        ]
    },
    "ESFP": {
        "title": "활기찬 분위기 메이커",
        "description": "사람들과 어울리고 즐거운 분위기를 만드는 것을 좋아하는 성향이에요.",
        "jobs": [
            ("이벤트 기획자", "사람들이 즐길 수 있는 행사와 프로그램을 기획해요."),
            ("방송인", "사람들과 소통하며 자신의 개성을 표현할 수 있어요."),
            ("관광 가이드", "다양한 사람들과 직접 소통하는 직업이에요.")
        ]
    },
    "ENFP": {
        "title": "열정적인 아이디어 탐험가",
        "description": "새로운 아이디어를 떠올리고 사람들과 소통하는 것을 좋아하는 성향이에요.",
        "jobs": [
            ("광고기획자", "새로운 아이디어를 만들고 사람들에게 효과적으로 전달해요."),
            ("콘텐츠 크리에이터", "자신의 아이디어와 개성을 콘텐츠로 표현할 수 있어요."),
            ("마케팅 기획자", "사람들의 관심을 분석하고 새로운 아이디어를 만들어요.")
        ]
    },
    "ENTP": {
        "title": "창의적인 아이디어 혁신가",
        "description": "새로운 가능성을 발견하고 기존의 방법을 다른 관점에서 바라보는 성향이에요.",
        "jobs": [
            ("창업가", "새로운 아이디어를 사업으로 발전시킬 수 있어요."),
            ("기획자", "새로운 서비스나 제품의 아이디어를 구체적인 계획으로 발전시켜요."),
            ("변호사", "논리적으로 주장을 구성하고 다양한 관점에서 문제를 분석해요.")
        ]
    },
    "ESTJ": {
        "title": "체계적인 관리자",
        "description": "목표를 정하고 사람과 자원을 효율적으로 관리하는 성향이에요.",
        "jobs": [
            ("경영 관리자", "조직의 목표를 설정하고 업무를 효율적으로 관리해요."),
            ("프로젝트 매니저", "여러 사람의 업무를 조정하여 프로젝트를 진행해요."),
            ("공무원", "규칙과 절차에 따라 조직적인 업무를 수행해요.")
        ]
    },
    "ESFJ": {
        "title": "사교적인 협력가",
        "description": "사람들과 협력하고 주변 사람들을 돕는 것을 중요하게 생각하는 성향이에요.",
        "jobs": [
            ("교사", "학생들과 소통하고 함께 성장할 수 있도록 도와요."),
            ("인사 담당자", "조직 구성원들과 소통하고 사람과 관련된 업무를 담당해요."),
            ("상담 관련 직업", "사람들의 이야기를 듣고 필요한 도움을 제공해요.")
        ]
    },
    "ENFJ": {
        "title": "사람을 이끄는 리더",
        "description": "사람들의 성장을 돕고 함께 목표를 이루는 것을 좋아하는 성향이에요.",
        "jobs": [
            ("교사", "학생들의 성장을 돕고 긍정적인 환경을 만들어요."),
            ("HR 전문가", "조직 구성원의 성장과 협력을 도와요."),
            ("상담심리사", "사람의 이야기를 듣고 성장을 지원해요.")
        ]
    },
    "ENTJ": {
        "title": "목표 지향적인 리더",
        "description": "목표를 세우고 사람과 자원을 조직하여 결과를 만들어내는 성향이에요.",
        "jobs": [
            ("기업 경영자", "조직의 방향을 결정하고 목표를 달성하기 위한 전략을 세워요."),
            ("프로젝트 매니저", "여러 사람과 업무를 조율하여 목표를 달성해요."),
            ("전략 컨설턴트", "조직의 문제를 분석하고 개선 전략을 제안해요.")
        ]
    }
}


# =========================================================
# 세션 상태
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_to(page):
    st.session_state.page = page


# =========================================================
# 사이드바
# =========================================================

with st.sidebar:
    st.markdown("## 🧭 꿈꾸는 나침반")
    st.caption("청소년 진로 탐색 도우미")

    st.divider()

    if st.button("🏠  홈"):
        go_to("home")

    if st.button("🧭  MBTI 진로 탐색"):
        go_to("mbti")

    if st.button("🌱  나의 진로 TIP"):
        go_to("tips")

    st.divider()

    st.caption("MBTI는 진로 선택의\n참고 자료로 활용해 주세요.")


# =========================================================
# 페이지 1 : 홈
# =========================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">🧭 꿈꾸는 나침반</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">나의 성향에서 시작하는 즐거운 진로 탐색</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h2>🌿 어떤 직업이 나에게 잘 맞을까?</h2>
        <p style="color:#687D78; line-height:1.8;">
        진로를 정하는 일은 생각보다 어려워요.<br>
        내가 좋아하는 것과 잘하는 것이 무엇인지 알아가는 것부터 시작해 봐요!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🧭 MBTI로 진로 탐색 시작하기"):
        go_to("mbti")
        st.rerun()

    st.write("")

    st.markdown("""
    <div class="tip-card">
        <div class="tip-title">💡 이 앱은 이렇게 사용해요</div>
        <div class="tip-text">
        ① 나의 MBTI를 선택해요<br>
        ② 나와 잘 맞을 수 있는 직업 3가지를 살펴봐요<br>
        ③ 관심 있는 직업을 직접 더 알아봐요
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        🌱 나에게 맞는 답을 찾는 것보다<br>
        나에게 맞는 길을 찾아가는 과정이 더 중요해요.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 페이지 2 : MBTI 진로 탐색
# =========================================================

elif st.session_state.page == "mbti":

    st.markdown(
        '<div class="page-title">🧭 MBTI 진로 탐색</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">나의 성향을 선택하고 어울릴 수 있는 직업을 알아봐요.</div>',
        unsafe_allow_html=True
    )

    mbti = st.selectbox(
        "✨ 나의 MBTI를 선택해 주세요",
        list(CAREERS.keys())
    )

    data = CAREERS[mbti]

    st.markdown(
        f"""
        <div class="mbti-card">
            <div class="mbti-name">{mbti} · {data['title']}</div>
            <div class="mbti-description">{data['description']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🎯 추천 직업 TOP 3")

    for index, (job, reason) in enumerate(data["jobs"], 1):

        st.markdown(
            f"""
            <div class="card">
                <div class="career-number">{index}번째 추천</div>
                <div class="career-title">💼 {job}</div>
                <div class="career-description">{reason}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "🌱 추천 결과는 '이 직업이 반드시 잘 맞는다'는 의미가 아니에요. "
        "새로운 직업을 발견하는 출발점으로 활용해 보세요!"
    )

    if st.button("🌱 진로 탐색 TIP 보기"):
        go_to("tips")
        st.rerun()


# =========================================================
# 페이지 3 : 진로 TIP
# =========================================================

elif st.session_state.page == "tips":

    st.markdown(
        '<div class="page-title">🌱 나의 진로 TIP</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">진로를 고민할 때 이런 것들을 함께 생각해 봐요.</div>',
        unsafe_allow_html=True
    )

    tips = [
        (
            "🔎 좋아하는 것을 찾아보기",
            "시간 가는 줄 모르고 하는 활동이 무엇인지 생각해 보세요. "
            "게임, 그림, 만들기, 사람들과 이야기하기 등 사소한 것도 좋은 단서가 될 수 있어요."
        ),
        (
            "💪 잘하는 것 발견하기",
            "친구나 선생님에게 내가 잘하는 것이 무엇인지 물어보는 것도 좋은 방법이에요. "
            "스스로는 당연하게 생각했던 능력이 강점일 수도 있어요."
        ),
        (
            "🧪 직접 경험해 보기",
            "관심 있는 분야가 있다면 관련 동아리, 프로젝트, 대회, 체험 활동 등을 경험해 보세요. "
            "직접 해보면 생각했던 것과 실제가 다른지도 알 수 있어요."
        ),
        (
            "📚 직업을 자세히 알아보기",
            "직업 이름만 보고 판단하지 말고 실제로 어떤 일을 하는지, "
            "어떤 능력이 필요한지, 어떤 환경에서 일하는지 찾아보세요."
        ),
        (
            "🗺️ 하나의 직업에 너무 빨리 결정하지 않기",
            "고등학생 때 진로가 완전히 정해져 있지 않아도 괜찮아요. "
            "여러 가능성을 탐색하면서 나에게 맞는 방향을 찾아가면 됩니다."
        )
    ]

    for title, text in tips:
        st.markdown(
            f"""
            <div class="tip-card">
                <div class="tip-title">{title}</div>
                <div class="tip-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.success(
        "✨ 진로는 한 번에 정답을 고르는 시험이 아니에요. "
        "여러 가지를 경험하면서 나에게 맞는 길을 찾아가는 과정이에요!"
    )

    if st.button("🏠 처음으로 돌아가기"):
        go_to("home")
        st.rerun()


# =========================================================
# 공통 하단
# =========================================================

st.divider()

st.caption(
    "🧭 꿈꾸는 나침반 · 청소년 진로 탐색용 프로그램 | "
    "MBTI는 진로 선택을 위한 참고 자료입니다."
)
