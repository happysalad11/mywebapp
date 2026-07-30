import random
from textwrap import dedent
import streamlit as st

# ---------------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="MBTI 영화 처방소",
    page_icon="🎬",
    layout="centered",
)

# ---------------------------------------------------------
# 영화 데이터
# 별도의 라이브러리나 외부 API 없이 파이썬 데이터만 사용합니다.
# ---------------------------------------------------------
MOVIES = {
    "ISTJ": [
        {
            "title": "인터스텔라",
            "genre": "SF · 드라마",
            "emoji": "🚀",
            "reason": "치밀한 설정과 책임감 있는 인물들의 선택을 따라가는 재미가 있어요.",
            "mood": "깊이 몰입하고 싶은 밤",
        },
        {
            "title": "히든 피겨스",
            "genre": "드라마 · 실화",
            "emoji": "🧮",
            "reason": "성실함과 정확함으로 어려움을 해결하는 인물들이 매력적이에요.",
            "mood": "차분한 용기가 필요한 날",
        },
        {
            "title": "마션",
            "genre": "SF · 어드벤처",
            "emoji": "🪐",
            "reason": "현실적인 계획과 끈기로 문제를 하나씩 해결하는 과정이 통쾌해요.",
            "mood": "문제 해결의 쾌감을 느끼고 싶은 날",
        },
    ],
    "ISFJ": [
        {
            "title": "리틀 포레스트",
            "genre": "드라마 · 힐링",
            "emoji": "🌿",
            "reason": "소박한 일상과 따뜻한 음식이 포근한 안정감을 전해줘요.",
            "mood": "마음을 천천히 쉬게 하고 싶은 날",
        },
        {
            "title": "원더",
            "genre": "가족 · 드라마",
            "emoji": "🌟",
            "reason": "다정함과 배려가 사람을 어떻게 변화시키는지 보여줘요.",
            "mood": "따뜻한 위로가 필요한 날",
        },
        {
            "title": "코다",
            "genre": "드라마 · 음악",
            "emoji": "🎶",
            "reason": "가족을 아끼는 마음과 자신의 꿈 사이에서 성장하는 이야기가 뭉클해요.",
            "mood": "따뜻하게 울고 싶은 날",
        },
    ],
    "INFJ": [
        {
            "title": "소울",
            "genre": "애니메이션 · 판타지",
            "emoji": "✨",
            "reason": "삶의 의미와 일상의 소중함을 섬세하게 생각하게 해줘요.",
            "mood": "조용히 나를 돌아보고 싶은 날",
        },
        {
            "title": "컨택트",
            "genre": "SF · 드라마",
            "emoji": "🛸",
            "reason": "언어와 시간, 관계에 관한 깊은 질문을 아름답게 풀어내요.",
            "mood": "여운이 긴 영화를 보고 싶은 밤",
        },
        {
            "title": "굿 윌 헌팅",
            "genre": "드라마",
            "emoji": "📚",
            "reason": "한 사람의 상처와 가능성을 진심으로 바라보는 과정이 인상적이에요.",
            "mood": "진솔한 위로가 필요한 날",
        },
    ],
    "INTJ": [
        {
            "title": "이미테이션 게임",
            "genre": "드라마 · 전기",
            "emoji": "🔐",
            "reason": "복잡한 문제를 독창적인 전략으로 해결하는 과정이 흥미로워요.",
            "mood": "지적인 몰입이 필요한 날",
        },
        {
            "title": "인셉션",
            "genre": "SF · 액션",
            "emoji": "🌀",
            "reason": "정교한 세계관과 여러 겹의 구조를 분석하는 재미가 커요.",
            "mood": "머리를 쓰며 몰입하고 싶은 밤",
        },
        {
            "title": "머니볼",
            "genre": "스포츠 · 드라마",
            "emoji": "📊",
            "reason": "기존의 방식을 의심하고 데이터로 새로운 전략을 만드는 이야기예요.",
            "mood": "새로운 관점이 필요한 날",
        },
    ],
    "ISTP": [
        {
            "title": "포드 V 페라리",
            "genre": "드라마 · 스포츠",
            "emoji": "🏎️",
            "reason": "기술, 속도, 현장 감각이 살아 있어 시원하게 몰입할 수 있어요.",
            "mood": "짜릿한 집중이 필요한 날",
        },
        {
            "title": "엣지 오브 투모로우",
            "genre": "SF · 액션",
            "emoji": "⚙️",
            "reason": "실패를 분석하고 즉시 전략을 바꾸는 전개가 빠르고 재미있어요.",
            "mood": "속도감 있는 영화를 보고 싶은 날",
        },
        {
            "title": "캐스트 어웨이",
            "genre": "드라마 · 어드벤처",
            "emoji": "🏝️",
            "reason": "제한된 환경에서 스스로 방법을 찾아 살아남는 과정이 인상적이에요.",
            "mood": "묵직한 생존 이야기가 끌리는 날",
        },
    ],
    "ISFP": [
        {
            "title": "월터의 상상은 현실이 된다",
            "genre": "어드벤처 · 드라마",
            "emoji": "📷",
            "reason": "아름다운 풍경과 조용한 용기가 감성을 살며시 깨워줘요.",
            "mood": "새로운 시작이 필요한 날",
        },
        {
            "title": "라라랜드",
            "genre": "음악 · 로맨스",
            "emoji": "🌙",
            "reason": "색감과 음악, 꿈을 향한 마음이 감각적으로 펼쳐져요.",
            "mood": "예쁜 장면과 음악에 빠지고 싶은 밤",
        },
        {
            "title": "플로리다 프로젝트",
            "genre": "드라마",
            "emoji": "🏰",
            "reason": "아이의 시선으로 바라본 일상이 선명한 색감과 깊은 여운을 남겨요.",
            "mood": "잔잔하지만 특별한 영화를 찾는 날",
        },
    ],
    "INFP": [
        {
            "title": "어바웃 타임",
            "genre": "로맨스 · 판타지",
            "emoji": "⏳",
            "reason": "평범한 하루와 사랑의 가치를 따뜻하게 되돌아보게 해줘요.",
            "mood": "포근한 감동이 필요한 날",
        },
        {
            "title": "이터널 선샤인",
            "genre": "로맨스 · SF",
            "emoji": "💭",
            "reason": "기억과 사랑의 의미를 독특하고 감성적인 방식으로 그려요.",
            "mood": "몽글몽글한 여운을 느끼고 싶은 밤",
        },
        {
            "title": "빅 피쉬",
            "genre": "판타지 · 드라마",
            "emoji": "🐟",
            "reason": "상상과 현실이 어우러진 이야기 속에서 관계의 의미를 발견하게 해요.",
            "mood": "동화 같은 감동이 필요한 날",
        },
    ],
    "INTP": [
        {
            "title": "트루먼 쇼",
            "genre": "드라마 · SF",
            "emoji": "📺",
            "reason": "현실과 자유의지에 관한 질문을 흥미로운 설정으로 던져요.",
            "mood": "생각할 거리가 필요한 날",
        },
        {
            "title": "프레스티지",
            "genre": "미스터리 · 드라마",
            "emoji": "🎩",
            "reason": "단서와 반전을 조립하며 이야기의 구조를 추리하는 재미가 있어요.",
            "mood": "복잡한 이야기에 빠지고 싶은 밤",
        },
        {
            "title": "그녀",
            "genre": "SF · 드라마",
            "emoji": "🤖",
            "reason": "기술과 감정, 관계의 경계를 섬세하게 탐구해요.",
            "mood": "조용한 철학적 여운이 필요한 날",
        },
    ],
    "ESTP": [
        {
            "title": "탑건: 매버릭",
            "genre": "액션 · 드라마",
            "emoji": "✈️",
            "reason": "빠른 속도와 현장감, 시원한 도전 정신을 모두 즐길 수 있어요.",
            "mood": "짜릿하게 기분 전환하고 싶은 날",
        },
        {
            "title": "베이비 드라이버",
            "genre": "액션 · 범죄",
            "emoji": "🎧",
            "reason": "음악과 액션의 박자가 정확하게 맞아떨어지는 쾌감이 있어요.",
            "mood": "리듬감 넘치는 영화를 보고 싶은 날",
        },
        {
            "title": "쥬만지: 새로운 세계",
            "genre": "코미디 · 어드벤처",
            "emoji": "🎮",
            "reason": "예측하기 어려운 모험과 유쾌한 팀플레이가 가볍게 즐거워요.",
            "mood": "친구들과 신나게 웃고 싶은 날",
        },
    ],
    "ESFP": [
        {
            "title": "맘마미아!",
            "genre": "음악 · 코미디",
            "emoji": "🌊",
            "reason": "밝은 음악과 풍경, 사랑스러운 에너지가 기분을 확 올려줘요.",
            "mood": "아무 생각 없이 행복해지고 싶은 날",
        },
        {
            "title": "씽",
            "genre": "애니메이션 · 음악",
            "emoji": "🎤",
            "reason": "개성 넘치는 인물과 신나는 무대가 즐거운 활력을 줘요.",
            "mood": "노래와 웃음이 필요한 날",
        },
        {
            "title": "크루엘라",
            "genre": "드라마 · 코미디",
            "emoji": "👗",
            "reason": "화려한 스타일과 당당한 주인공의 에너지가 강렬해요.",
            "mood": "스타일리시한 자극이 필요한 날",
        },
    ],
    "ENFP": [
        {
            "title": "업",
            "genre": "애니메이션 · 어드벤처",
            "emoji": "🎈",
            "reason": "새로운 모험과 예상 밖의 우정이 마음을 활짝 열어줘요.",
            "mood": "설레는 모험이 필요한 날",
        },
        {
            "title": "패딩턴 2",
            "genre": "가족 · 코미디",
            "emoji": "🐻",
            "reason": "다정함과 유쾌함이 가득해 보고 나면 세상이 조금 사랑스러워져요.",
            "mood": "기분 좋은 위로가 필요한 날",
        },
        {
            "title": "스쿨 오브 락",
            "genre": "코미디 · 음악",
            "emoji": "🎸",
            "reason": "자유로운 아이디어와 함께하는 즐거움이 통통 튀어요.",
            "mood": "신나게 에너지를 충전하고 싶은 날",
        },
    ],
    "ENTP": [
        {
            "title": "나이브스 아웃",
            "genre": "미스터리 · 코미디",
            "emoji": "🔎",
            "reason": "재치 있는 대화와 반전, 인물들의 심리전이 쉴 틈 없이 이어져요.",
            "mood": "유쾌하게 추리하고 싶은 날",
        },
        {
            "title": "소셜 네트워크",
            "genre": "드라마",
            "emoji": "💻",
            "reason": "아이디어, 경쟁, 관계가 빠른 대사와 함께 날카롭게 펼쳐져요.",
            "mood": "두뇌를 자극하는 이야기가 필요한 날",
        },
        {
            "title": "캐치 미 이프 유 캔",
            "genre": "범죄 · 드라마",
            "emoji": "🕶️",
            "reason": "기발한 임기응변과 팽팽한 추격이 경쾌하게 이어져요.",
            "mood": "영리하고 빠른 영화를 보고 싶은 날",
        },
    ],
    "ESTJ": [
        {
            "title": "인턴",
            "genre": "코미디 · 드라마",
            "emoji": "💼",
            "reason": "일과 관계를 책임감 있게 이끌어가는 인물들의 균형이 돋보여요.",
            "mood": "편안한 동기부여가 필요한 날",
        },
        {
            "title": "설리: 허드슨강의 기적",
            "genre": "드라마 · 실화",
            "emoji": "🛬",
            "reason": "위기 속 판단력과 책임감이 긴장감 있게 그려져요.",
            "mood": "단단한 리더십을 보고 싶은 날",
        },
        {
            "title": "에어",
            "genre": "드라마 · 스포츠",
            "emoji": "👟",
            "reason": "목표를 세우고 사람을 설득해 성과를 만드는 과정이 흥미로워요.",
            "mood": "일할 힘을 얻고 싶은 날",
        },
    ],
    "ESFJ": [
        {
            "title": "악마는 프라다를 입는다",
            "genre": "코미디 · 드라마",
            "emoji": "👜",
            "reason": "관계와 성장, 멋진 스타일이 경쾌하게 어우러져 있어요.",
            "mood": "가볍게 기분 전환하고 싶은 날",
        },
        {
            "title": "인사이드 아웃",
            "genre": "애니메이션 · 가족",
            "emoji": "🌈",
            "reason": "다양한 감정이 모두 소중하다는 메시지를 사랑스럽게 전해요.",
            "mood": "마음을 다독이고 싶은 날",
        },
        {
            "title": "원 데이",
            "genre": "로맨스 · 드라마",
            "emoji": "📅",
            "reason": "시간에 따라 변하는 관계와 감정을 섬세하게 따라가요.",
            "mood": "사람 사이의 인연을 생각하고 싶은 날",
        },
    ],
    "ENFJ": [
        {
            "title": "죽은 시인의 사회",
            "genre": "드라마",
            "emoji": "📖",
            "reason": "사람의 가능성을 믿고 용기를 북돋우는 메시지가 깊게 남아요.",
            "mood": "마음에 불을 켜고 싶은 날",
        },
        {
            "title": "위대한 쇼맨",
            "genre": "음악 · 드라마",
            "emoji": "🎪",
            "reason": "사람들을 하나로 모으는 열정과 화려한 음악이 큰 에너지를 줘요.",
            "mood": "벅찬 감동이 필요한 날",
        },
        {
            "title": "헬프",
            "genre": "드라마",
            "emoji": "🤝",
            "reason": "공감과 연대가 변화를 만드는 과정을 따뜻하고 힘 있게 보여줘요.",
            "mood": "사람의 선한 힘을 믿고 싶은 날",
        },
    ],
    "ENTJ": [
        {
            "title": "조이",
            "genre": "드라마 · 전기",
            "emoji": "💡",
            "reason": "아이디어를 현실로 만들기 위해 끈질기게 앞으로 나아가는 이야기예요.",
            "mood": "도전 의식을 깨우고 싶은 날",
        },
        {
            "title": "다크 나이트",
            "genre": "액션 · 드라마",
            "emoji": "🦇",
            "reason": "리더십과 선택, 질서에 관한 묵직한 갈등을 강렬하게 보여줘요.",
            "mood": "긴장감 있는 대작이 필요한 밤",
        },
        {
            "title": "스티브 잡스",
            "genre": "드라마 · 전기",
            "emoji": "🍎",
            "reason": "완벽을 향한 집념과 복잡한 인간관계가 빠른 대사로 펼쳐져요.",
            "mood": "강한 추진력의 이야기가 끌리는 날",
        },
    ],
}

MBTI_NICKNAMES = {
    "ISTJ": "꼼꼼한 현실주의자",
    "ISFJ": "포근한 수호자",
    "INFJ": "깊은 통찰의 몽상가",
    "INTJ": "전략적인 설계자",
    "ISTP": "침착한 해결사",
    "ISFP": "감성적인 예술가",
    "INFP": "낭만적인 중재자",
    "INTP": "호기심 많은 탐구자",
    "ESTP": "짜릿한 모험가",
    "ESFP": "반짝이는 분위기 메이커",
    "ENFP": "통통 튀는 아이디어 요정",
    "ENTP": "재치 있는 발명가",
    "ESTJ": "든든한 관리자",
    "ESFJ": "다정한 인기쟁이",
    "ENFJ": "따뜻한 응원단장",
    "ENTJ": "당당한 지휘관",
}

# ---------------------------------------------------------
# 디자인
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 15% 10%, #ffe3f1 0, transparent 24%),
                radial-gradient(circle at 90% 20%, #e1f3ff 0, transparent 26%),
                linear-gradient(180deg, #fff9fc 0%, #fffdf7 100%);
        }

        .block-container {
            max-width: 780px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {
            text-align: center;
            padding: 2rem 1rem 1.2rem;
        }

        .hero-badge {
            display: inline-block;
            padding: 0.45rem 0.9rem;
            border-radius: 999px;
            background: #ffffffcc;
            border: 1px solid #ffd4e6;
            color: #d85b91;
            font-weight: 700;
            box-shadow: 0 8px 24px rgba(216, 91, 145, 0.08);
        }

        .hero-title {
            margin: 0.8rem 0 0.35rem;
            font-size: clamp(2.2rem, 7vw, 3.8rem);
            line-height: 1.15;
            color: #432f43;
            letter-spacing: -0.06em;
        }

        .hero-subtitle {
            color: #7f697c;
            font-size: 1rem;
            margin-bottom: 0;
        }

        .picker-box {
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(255, 203, 226, 0.9);
            border-radius: 26px;
            padding: 1.2rem 1.25rem 0.8rem;
            box-shadow: 0 18px 50px rgba(111, 73, 101, 0.09);
            backdrop-filter: blur(8px);
        }

        .movie-card {
            position: relative;
            overflow: hidden;
            margin-top: 1.35rem;
            background: linear-gradient(135deg, #ffffff 0%, #fff5fa 100%);
            border: 2px solid #ffd6e8;
            border-radius: 30px;
            padding: 1.7rem;
            box-shadow: 0 20px 55px rgba(160, 91, 127, 0.14);
        }

        .movie-card::after {
            content: "♡";
            position: absolute;
            right: 18px;
            top: 5px;
            font-size: 5.5rem;
            color: rgba(255, 167, 203, 0.22);
            transform: rotate(12deg);
        }

        .movie-emoji {
            font-size: 4.5rem;
            margin-bottom: 0.4rem;
        }

        .movie-label {
            display: inline-block;
            background: #ffdfec;
            color: #b84478;
            padding: 0.35rem 0.72rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 800;
        }

        .movie-title {
            color: #3f2e3d;
            margin: 0.55rem 0 0.25rem;
            font-size: 2rem;
            letter-spacing: -0.04em;
        }

        .movie-genre {
            color: #a06e88;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .reason-box {
            background: #ffffff;
            border-radius: 20px;
            padding: 1rem 1.05rem;
            border: 1px dashed #f2aac8;
            color: #5f4d5b;
            line-height: 1.7;
        }

        .mood {
            margin-top: 0.85rem;
            color: #8b6078;
            font-size: 0.93rem;
        }

        .tiny-note {
            text-align: center;
            color: #9a8795;
            font-size: 0.82rem;
            margin-top: 1.5rem;
        }

        div[data-testid="stSelectbox"] label {
            color: #594554;
            font-weight: 800;
            font-size: 1rem;
        }

        div.stButton > button {
            width: 100%;
            min-height: 3.2rem;
            border: 0;
            border-radius: 18px;
            background: linear-gradient(90deg, #ff8dbc, #a78bfa);
            color: white;
            font-weight: 800;
            font-size: 1rem;
            box-shadow: 0 10px 25px rgba(221, 110, 168, 0.25);
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 30px rgba(180, 103, 188, 0.32);
            color: white;
        }

        div.stButton > button:active {
            transform: translateY(0);
        }

        #MainMenu, footer, header {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 상태 관리
# ---------------------------------------------------------
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = "ENFP"

if "movie_index" not in st.session_state:
    st.session_state.movie_index = random.randrange(
        len(MOVIES[st.session_state.selected_mbti])
    )

def pick_new_movie():
    """현재 MBTI 안에서 이전 영화와 다른 작품을 고릅니다."""
    movie_count = len(MOVIES[st.session_state.selected_mbti])

    if movie_count <= 1:
        st.session_state.movie_index = 0
        return

    candidates = [
        index
        for index in range(movie_count)
        if index != st.session_state.movie_index
    ]
    st.session_state.movie_index = random.choice(candidates)

def change_mbti():
    """MBTI가 바뀌면 해당 유형의 첫 추천 영화를 무작위로 정합니다."""
    st.session_state.movie_index = random.randrange(
        len(MOVIES[st.session_state.selected_mbti])
    )

# ---------------------------------------------------------
# 화면
# ---------------------------------------------------------
st.markdown(
    dedent(
        """
        <section class="hero">
            <div class="hero-badge">🍿 오늘의 영화 취향 찾기</div>
            <h1 class="hero-title">MBTI 영화 처방소</h1>
            <p class="hero-subtitle">
                나의 MBTI를 고르면 오늘의 기분에 어울리는 영화를 추천해드려요.
            </p>
        </section>
        """
    ).strip(),
    unsafe_allow_html=True,
)

st.markdown('<div class="picker-box">', unsafe_allow_html=True)

st.selectbox(
    "나의 MBTI는?",
    options=list(MOVIES.keys()),
    key="selected_mbti",
    format_func=lambda mbti: f"{mbti} · {MBTI_NICKNAMES[mbti]}",
    on_change=change_mbti,
)

st.button(
    "💖 나에게 어울리는 영화 추천받기",
    on_click=pick_new_movie,
    use_container_width=True,
)

st.markdown("</div>", unsafe_allow_html=True)

mbti = st.session_state.selected_mbti
movie = MOVIES[mbti][st.session_state.movie_index]

st.markdown(
    dedent(
        f"""
        <article class="movie-card">
            <div class="movie-emoji">{movie["emoji"]}</div>
            <span class="movie-label">{mbti} 맞춤 추천</span>
            <h2 class="movie-title">{movie["title"]}</h2>
            <div class="movie-genre">{movie["genre"]}</div>

            <div class="reason-box">
                <strong>💌 추천 이유</strong><br>
                {movie["reason"]}
            </div>

            <div class="mood">
                <strong>🍿 오늘의 관람 처방</strong><br>
                {movie["mood"]}
            </div>
        </article>
        """
    ).strip(),
    unsafe_allow_html=True,
)

st.markdown(
    dedent(
        """
        <p class="tiny-note">
            MBTI 추천은 재미로 가볍게 즐겨주세요. 취향은 언제든 달라질 수 있어요! 🎀
        </p>
        """
    ).strip(),
    unsafe_allow_html=True,
)
