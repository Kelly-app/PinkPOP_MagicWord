import streamlit as st
import random


def inject_custom_css():
    """
    새로운 와이어프레임 기준 CSS
    순서: Mini Hero -> 한국어 문제 -> 영어 문장 -> 입력 필드 -> Log Message -> Submit Button -> 하단 고정 버튼
    """
    st.markdown("""
    <style>
    /* ✅ 올바른 문법 */
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

/* 그리고 CSS에서 사용 */
font-family: 'Comic Neue', 'Comic Sans MS', cursive, sans-serif;
    
    /* ========== 전체 배경 ========== */
    .stApp {
        background-color: #FFF0F5;
        background-image: 
            radial-gradient(#FFB6C1 1px, transparent 1px),
            radial-gradient(#98FB98 1px, transparent 1px);
        background-size: 50px 50px;
        background-position: 0 0, 25px 25px;
        padding: 0 !important;
    }


    /* ========== Mini Hero Header (80~100px) ========== */
    .mini-hero {
        background: linear-gradient(135deg, #FFB6C1 0%, #D8BFD8 50%, #98FB98 100%);
        padding: 0.7rem;
        text-align: center;
        border-radius: 0 0 20px 20px;
        margin: 0 !important;
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.3);
        min-height: 80px;
        max-height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .mini-hero h1 {
        color: white;
        font-family: 'Comic Neue', sans-serif,'Roboto', cursive;
        font-size: 2.0rem;
        text-shadow: 2px 2px 0px #FF69B4;
        margin: 0;
        letter-spacing: 1px;
        text-align: center;
        display: flex;                          /* ➕ Flexbox 사용 */
        align-items: center;                    /* ➕ 수직 중앙정렬 */
        justify-content: center;                /* ➕ 수평 중앙정렬 */
        gap: 0.5rem;                            /* ➕ 이모지와 텍스트 간격 */
        flex-wrap: wrap;                        /* ➕ 반응형 대비 */
    }

    /* ========== 메인 컨테이너 (중앙 정렬) ========== */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        max-width: 700px;
        margin: 0 auto;
        padding: 1rem;
        gap: 0.5rem;
        
        /* ✅ 반응형 패딩 조정 */
        @media (max-width: 428px) {  /* 아이폰 최대 너비 */
            .main-container {
                padding: 0.75rem;
                gap: 0.375rem;
            }
        }
    }
    /* ========== 상단바 (학습모드 선택) - 강조 버전 ========== */
    .stSelectbox {
        width: 90vw !important;        /* 화면의 90% */
        max-width: 400px !important;   /* 최대 400px */
        margin: 0 auto !important;
        padding: 0.8rem 1.5rem !important;
    
        text-align: center !important;
        background-color: white !important;     /* ➕ 배경색 추가 */
       
        /* ✅ 더 자연스러운 둥근 모서리 */
        border-radius: 15px !important;         /* ➕ 둥근 모서리 */
        box-shadow: 0 4px 12px rgba(255, 105, 180, 0.25) !important;  /* ➕ 부드러운 그림자 */
        border: 2px solid #FFB6C1 !important;   /* ➕ 테두리 추가 */
        
        /* ✅ 더 나은 호환성을 위한 너비 설정 */       
        min-width: min(300px, 80vw);  /* ✅ 최소 너비 보장 */       
    }

    .stSelectbox > div {
        text-align: center !important;
    }

    .stSelectbox label {
        font-size: 1.3rem !important;
        font-weight: bold !important;
        color: #FF69B4 !important;
        text-align: center !important;
        display: block !important;
        margin-bottom: 0.5rem !important;
    }

    /* ➕ 추가: selectbox 드롭다운 버튼 강조 */
    .stSelectbox [data-testid="selectbox"] {
        background-color: #FFF5FB !important;
        border: 2px solid #FFB6C1 !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
    }

    /* ========== 문제 영역 (한국어) problem-box: KR sentence + En Section ========== */
    .problem-box {
        width: 100%;
        max-width: 600px;
        background-color: linear-gradient(to right, #FFF0F5, #FFFFFF);
        border-radius: 20px;
        border: 1px solid #FFB6C1;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.4);
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .korean-sentence {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 0.5rem !important;
        margin: 1rem auto !important; /* 위아래 1rem, 좌우 auto로 중앙 정렬 */
        width: 90% !important;        /* PC에서도 너무 넓지 않게 조절 */
        max-width: 800px !important;   /* 최대 너비 제한 */
        text-align: center !important; /* 텍스트 중앙 정렬 */
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.3) !important;
    }

    /* ========== 영어 문장 box + sentence ========== */
   
    .english-sentence {
        font-family: 'Helvetica Neue', cursive;
        font-size: 1.3rem;
        text-align: center;
        padding: 1rem;                 /* ➕ 상하 패딩 증가 */
        color: #FF69B4;
        background: linear-gradient(to right, #FFF0F5, #FFFFFF);
        border-radius: 15px;
        border: 2px dashed #FFB6C1;
        font-weight: bold;
        line-height: 1.8;
        box-shadow: 0 4px 10px rgba(255, 182, 193, 0.2);
        width: 100%;                            /* ➕ 전체 너비 */
        max-width: 600px;                       /* ➕ 최대 너비 제한 */
        display: flex;                          /* ➕ Flexbox */
        flex-direction: column;                 /* ➕ 세로 배치 */
        align-items: center;                    /* ➕ 중앙정렬 */
        justify-content: center;                /* ➕ 수직 중앙정렬 */
    }

    /* ========== 입력 영역 레이블 ========== */
    .input-label {
        font-size: 1.3rem;
        color: #CD29DC;
        font-weight: bold;
        margin: 0.3rem 0 0.3rem 0;
        text-align: center;
    }

    /* ========== 입력 필드 그룹 (2개 함께) ========== */
    .input-group {
        display: flex;
        flex-direction: row;
        align-items: center;                    /* ✅ 강화: 상하 여백 동등 */
        justify-content: center;
        gap: 0.8rem;                            /* ➕ 간격 미세조정: 1rem→0.8rem */
        width: 100%;
        max-width: 600px;
        flex-wrap: wrap;
    }

    .input-item {
        display: flex;
        align-items: center;                    /* ✅ 수직 중앙정렬 강화 */
        gap: 0.5rem;
        height: 100%;                           /* ➕ 높이 최대화 */
    }

    .input-icon {
        font-size: 1rem;
        font-weight: bold;
        color: #FF69B4;
        min-width: 20px;
        text-align: center;
    }

    /* 입력 필드 스타일 (텍스트 중앙정렬 추가) */
    .stTextInput > div > div > input {
        min-width: 80px !important;
        max-width: 120px !important;
        padding: 8px 10px !important;           /* ➕ 패딩 증가: 2px 8px → 8px 10px */
        font-size: 1.1rem !important;
        height: 40px !important;                /* ➕ 높이 조정: 35px → 40px */
        border-radius: 8px !important;
        
        text-align: center !important;          /* ➕ 입력 텍스트 중앙정렬 */
        vertical-align: middle !important;      /* ➕ 수직 중앙정렬 */
    }

    .input-group {
        gap: 0.5rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #FFB6C1 !important;
        box-shadow: 0 0 12px rgba(255, 182, 193, 0.8) !important;
        background: #FFF5F8 !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #150303 !important;
        text-align: center !important;          /* ➕ placeholder도 중앙정렬 */
    }
    
    /* 입력 필드 사이의 간격(마진) 최소화 */
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.5rem !important;
    }
    /* ========== Log Message 영역 ========== */
    .log-message {
        width: 100%;
        max-width: 600px;
        text-align: center;
        min-height: 2rem;
        display: flex;
        justify-content: center; /* 수평 중앙 정렬 */
        align-items: center;     /* 수직 중앙 정렬 */
        margin: 0 auto;          /* 좌우 자동 마진 */
    }


    .stSuccess, .stError, .stInfo, .stWarning {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto !important;  /* ➕ 추가 */
        width: 100% !important;
        max-width: 600px !important;
        margin: 0 auto !important;
    }
    
    .stSuccess {
        background: #E8F8F5 !important;
        border: 2px solid #27AE60 !important;
        border-radius: 15px !important;
        padding: 1rem 1.5rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
        min-height: 3rem;        /* 최소 높이 */
        /*display: flex;           /* Flexbox */
        /* justify-content: center;  수평 중앙 정렬 */
        /*  align-items: center;     수직 중앙 정렬 */
        /* margin: 0 auto;          /* 좌우 자동 마진 */
        
        /* width: 100%;             /* 전체 너비 */
        /* max-width: 600px;        /*최대 너비 */
        /* margin: 0 auto;          /*중앙 정렬 */
    }

    .stError {
        background: #FADBD8 !important;
        border: 2px solid #E74C3C !important;
        border-radius: 15px !important;
        padding: 1rem 1.5rem!important; /*좌우 패딩 증가 /
        text-align: center !important;
        font-size: 1.3rem !important;
        display: flex            /* flex box */
        justify-content: center; /* 수평 중앙 정렬 */
        align-items: center;     /* 수직 중앙 정렬 */
        margin: 1rem auto;          /* 좌우 자동 마진 */
        min-height: 3rem;        /* 최소 높이 */
        width: 100%;             /* 전체 너비 */
        max-width: 600px;        /*최대 너비 */        
    }

    .stInfo {
        background: #D6EAF8 !important;
        border: 2px solid #3498DB !important;
        border-radius: 15px !important;
        padding: 1rem 1.5rem!important; /*좌우 패딩 증가 /
        text-align: center !important;
        font-size: 1.3rem !important;
        display: flex            /* flex box */
        justify-content: center; /* 수평 중앙 정렬 */
        align-items: center;     /* 수직 중앙 정렬 */
        margin: 0 auto;          /* 좌우 자동 마진 */
        min-height: 3rem;        /* 최소 높이 */
        width: 100%;             /* 전체 너비 */
        max-width: 600px;        /*최대 너비 */
        margin: 0 auto;          /*중앙 정렬 */
    }

    .stWarning {
        background: #FCF3CF !important;
        border: 2px solid #F39C12 !important;
        border-radius: 15px !important;
        padding: 1rem 1.5rem!important;
        text-align: center !important;
        font-size: 1.3rem !important;
        display: flex            /* flex box */
        justify-content: center; /* 수평 중앙 정렬 */
        align-items: center;     /* 수직 중앙 정렬 */
        margin: 0 auto;          /* 좌우 자동 마진 */
        min-height: 3rem;        /* 최소 높이 */
        width: 100%;             /* 전체 너비 */
        max-width: 600px;        /*최대 너비 */
        margin: 0 auto;          /*중앙 정렬 */
    }

    /* ========== Form Submit Button ========== */
    .stFormSubmitButton {
        display: flex !important;               /* ➕ Flexbox 래퍼 */
        justify-content: center !important;     /* ➕ 중앙정렬 */
        align-items: center !important;         /* ➕ 수직 중앙정렬 */
        width: 100% !important;
        margin-bottom: 0rem !important;         /* 에러 메시지와의 간격 확보 */
        padding-bottom: 0.5rem !important;  /* 기본 패딩을 절반으로 축소 */
    }

    .stFormSubmitButton > button {
        background-color: #FF69B4 !important;
        color: white !important;
        width: fit-content !important;          /* ➕ 변경: 100% → fit-content */
        min-width: 150px !important;            /* ➕ 최소 너비 */
        max-width: 600px !important;
        font-size: 1.3rem !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 12px 40px !important;          /* ➕ 좌우 패딩 증가: 24px → 40px */
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        margin-bottom: 0.5rem !important;
        display: flex !important;               /* ➕ Flexbox */
        align-items: center !important;         /* ➕ 수직 중앙정렬 */
        justify-content: center !important;     /* ➕ 수평 중앙정렬 */
        gap: 0.5rem !important;                 /* ➕ 아이콘과 텍스트 간격 */
    }

    .stFormSubmitButton > button:hover {
        background-color: #FF1493 !important;
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    /* 2. 공통 박스 스타일 (기존 st.info/warning 느낌) */
    .custom-box {
        width: 100%;
        max-width: 800px; /* 너무 넓으면 가독성이 떨어지므로 제한 */
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center; /* 텍스트 가로 중앙 정렬 */
        font-size: 1.1rem;
        line-height: 1.5;
    }

    /* 3. 힌트 박스 (Blue) */
    .hint-box {
        background-color: #e1f5fe;
        color: #01579b;
        border: 1px solid #b3e5fc;
    }

    /* 4. 정답 박스 (Orange) */
    .answer-box {
        background-color: #fff3e0;
        color: #e65100;
        border: 1px solid #ffe0b2;
    }
    
    /* 5. 전체 문장 텍스트 */
    .full-sentence {
        text-align: center;
        font-size: 1.3rem;
        color: #444;
        margin-top: 10px;
        font-weight: 600;
    }
    
    /* ========== 하단 버튼 (고정) ========== */
    .bottom-buttons {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, #FFF0F5, #FFFFFF);
        padding: 0.5rem;
        display: flex;
        gap: 0.8rem;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        box-shadow: 0 -4px 15px rgba(255, 182, 193, 0.2);
        z-index: 100;
        border-top: 2px solid #FFB6C1;
    }

    .bottom-buttons button {
        border-radius: 20px !important;
        font-weight: bold !important;
        font-size: 1.3rem !important;
        padding: 10px 18px !important;
        transition: all 0.3s ease !important;
        border: 2px solid !important;
        min-width: 100px !important;
    }

    .bottom-buttons button:hover {
        transform: scale(1.05) !important;
    }

    /* 확인 버튼: 연한 파랑 (SkyBlue) */
    .btn-check {
        background-color: #87CEEB !important;
        color: white !important;
        border-color: #4682B4 !important;
    }

    .btn-check:hover {
        background-color: #4682B4 !important;
        box-shadow: 0 4px 15px rgba(70, 130, 180, 0.4) !important;
    }

    /* 힌트 버튼: 연한 노랑 (Yellow Pastel) */
    .btn-hint {
        background-color: #FFEB99 !important;
        color: #333 !important;
        border-color: #FFD700 !important;
    }

    .btn-hint:hover {
        background-color: #FFD700 !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4) !important;
    }

    /* 다음 버튼: 연한 분홍 (BabyPink) */
    .btn-next {
        background-color: #FFB6D9 !important;
        color: #333 !important;
        border-color: #FF69B4 !important;
    }

    .btn-next:hover {
        background-color: #FF69B4 !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4) !important;
    }

    /* ========== 보석/별 애니메이션 ========== */
    .star-rating {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 1rem 0;
        text-align: center;
    }

    .star {
        font-size: 2.5rem;
        animation: twinkle 0.8s infinite alternate;
    }

    @keyframes twinkle {
        from {
            opacity: 0.6;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1.2);
        }
    }

    /* ========== 반응형 디자인 ========== */
    @media (max-width: 600px) {
        .mini-hero h1 {
            font-size: 1.8rem;
        }

        .english-sentence {
            font-size: 1.3rem;
        }

        .korean-sentence {
            font-size: 1.3rem;
        }

        .input-group {
            flex-direction: column;
            gap: 0.8rem;
        }

        .stTextInput > div > div > input {
            min-width: 140px !important;
            max-width: 200px !important;
            font-size: 1.3rem !important;
            text-align: center !important;
        }

        .bottom-buttons {
            flex-direction: column;
            gap: 0.5rem;
            padding: 0.8rem;
        }

        .bottom-buttons button {
            width: 100% !important;
            min-width: unset !important;
        }

        .main-container {
            padding: 0.5rem 0.3rem;
        }

        .problem-box {
            padding: 0.5rem;
        }
    }

    /* ========== 매우 큰 화면 (데스크톱) ========== */
    @media (min-width: 1200px) {
        .main-container {
            max-width: 800px;
        }

        .problem-box,
        .english-section,
        .input-group,
        .log-message {
            max-width: 800px;
        }

        .stFormSubmitButton > button {
            max-width: 800px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_mini_hero(app_title="✨ PinkPOP Word Land 💎"):
    """Mini Hero Header (80~100px)"""
    st.markdown(f"""
    <div class="mini-hero">
        <h1>{app_title}</h1>
    </div>
    """, unsafe_allow_html=True)

def build_ui_layout(korean_sentence, english_blanked_sentence, answers, full_english_sentence, show_hint, show_answer):
    """
    새로운 와이어프레임 레이아웃
    
    순서:
    1. Mini Hero
    2. 학습모드 선택 
    3. 한국어 문제 + 영어 문장
    4. 입력 필드 (2개 나란히)
    5. Log Message
    6. Form Submit
    7. 하단 고정 버튼
    8. 에러메세지. 별* 획득 
    """

    # ========== 메인 컨테이너 시작 ==========
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    # --- [수정] 한국어 /영어문제 영역 추가
    st.markdown(f"""
    <div class="problem-box">      
        <div class="korean-sentence">{korean_sentence}</div>
        <div class="english-sentence">{english_blanked_sentence}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form(key='answer_form'):
        # 컨테이너 생성 (CSS로 가로 정렬 강제)
        st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">', unsafe_allow_html=True)
        
        # 컬렉션을 사용하여 한 줄에 배치 (예: 3칸이면 3컬럼)
        cols = st.columns(len(answers)) 
        user_answers = []        

        for i, ans_text in enumerate(answers):
            with cols[i]:
                # 라벨을 (1), (2) 형태로 짧게 넣어 공간 절약
                ans = st.text_input(
                    f"({i+1})", 
                    key=f"input_{i}",
                    placeholder="Fill here",
                    label_visibility="visible" # 숫자를 라벨로 써서 위젯 높이 축소
                )
                user_answers.append(ans)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Log Message 영역 ---
        st.markdown('<div class="log-message">', unsafe_allow_html=True)
        
        if show_hint:
            hint_text = " / ".join([f"({i+1}) '{ans[:2]}...'" for i, ans in enumerate(answers)])
            # 커스텀 힌트 박스 적용
            st.markdown(f'<div class="custom-box hint-box">💡 Hint: {hint_text}</div>', unsafe_allow_html=True)

        if show_answer:
            answer_text = " / ".join([f"({i+1}) {ans}" for i, ans in enumerate(answers)])
            # 커스텀 정답 박스 적용
            st.markdown(f'<div class="custom-box answer-box">✅ Right Answer: {answer_text}</div>', unsafe_allow_html=True)
            # 전체 문장도 클래스로 관리
            st.markdown(f'<div class="full-sentence"><strong>전체:</strong> {full_english_sentence}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Form Submit 버튼 ---
        submit_clicked = st.form_submit_button(
            label='🔮 Check Answer',
            type="primary",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)  # main-container 종료
    
    # 하단 버튼 영역을 위한 여백
    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    
    # ========== 하단 버튼 (고정 위치) ==========
    st.markdown('<div class="bottom-buttons" id="bottom-buttons">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    # 개선: Streamlit columns 대신 HTML/CSS flexbox 사용
    st.markdown("""
    <div style="
        display: flex;
        gap: 0.8rem;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        width: 100%;
    ">
    """, unsafe_allow_html=True)
    
    with col1:
        check_clicked = st.button(
            "✅ Check",
            key="btn_check",
            use_container_width=True,
            help="Recheck"
        )
    
    with col2:
        hint_clicked = st.button(
            "💡 Hint",
            key="btn_hint",
            use_container_width=True,
            help="Check chars"
        )
    
    with col3:
        next_clicked = st.button(
            "⏭️ Next",
            key="btn_next",
            use_container_width=True,
            help="Next"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return {
        'user_answers': user_answers,
        'submit_clicked': submit_clicked,
        'hint_clicked': hint_clicked,
        'answer_clicked': check_clicked,
        'next_clicked': next_clicked
    }

def build_voca_ui_layout(word, meaning, show_hint, show_answer):
    """
    새로운 와이어프레임 기준 Voca Quiz 레이아웃
    """

    
    # ========== 메인 컨테이너 시작 ==========
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="english-sentence">{word}</div>', unsafe_allow_html=True)
    # --- 입력 레이블 ---
    st.markdown("""
    <div class="input-label">✏️ Input English Meaning</div>
    """, unsafe_allow_html=True)
    
    with st.form(key='voca_form'):
        st.markdown('<div class="input-group" style="justify-content: center;">', unsafe_allow_html=True)
        
        user_answer = st.text_input(
            "뜻",
            key="voca_input_field",
            placeholder="답",
            label_visibility="collapsed"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Log Message 영역 ---
        st.markdown('<div class="log-message">', unsafe_allow_html=True)
        
        if show_hint and meaning:
            st.info(f"💡 힌트: '{meaning[:2]}' (으)로 시작합니다!")
        
        if show_answer:
            st.warning(f"✅ 정답: {meaning}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Form Submit 버튼 ---
        submit_clicked = st.form_submit_button(
            label='🔮 정답 확인하기',
            type="primary",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)  # main-container 종료
    
    # 하단 버튼 영역을 위한 여백
    st.markdown("<div style='height: 6rem;'></div>", unsafe_allow_html=True)
    
    # ========== 하단 버튼 (고정 위치) ==========
    st.markdown('<div class="bottom-buttons" id="bottom-buttons">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        check_clicked = st.button(
            "✅ 확인",
            key="btn_check_voca",
            use_container_width=True,
            help="다시 확인"
        )
    
    with col2:
        hint_clicked = st.button(
            "💡 힌트",
            key="btn_hint_voca",
            use_container_width=True,
            help="첫 글자 확인"
        )
    
    with col3:
        next_clicked = st.button(
            "⏭️ 다음",
            key="btn_next_voca",
            use_container_width=True,
            help="다음 문제"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return {
        'user_answer': user_answer,
        'submit_clicked': submit_clicked,
        'hint_clicked': hint_clicked,
        'answer_clicked': check_clicked,
        'next_clicked': next_clicked
    }

def throw_gems():
    """정답 시 보석과 반짝이가 쏟아지는 애니메이션"""
    html_code = """
    <style>
    .gem-drop {
        position: fixed;
        top: -10vh;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation: fall linear forwards;
    }
    @keyframes fall {
        0% {
            transform: translateY(-10vh) rotate(0deg) scale(1);
            opacity: 1;
        }
        80% {
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(360deg) scale(1.5);
            opacity: 0;
        }
    }
    </style>
    """
    
    emojis = ['💎', '✨', '💖', '🌟']
    for _ in range(30):
        emoji = random.choice(emojis)
        left = random.randint(0, 100)
        delay = random.uniform(0, 1.5)
        duration = random.uniform(2, 4)
        size = random.uniform(1.5, 3)
        
        html_code += f'<div class="gem-drop" style="left: {left}vw; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}rem;">{emoji}</div>'
    
    st.markdown(html_code, unsafe_allow_html=True)
