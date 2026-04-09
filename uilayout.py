import streamlit as st
import random

def inject_custom_css():
    """
    새로운 와이어프레임 기준 CSS
    순서: Mini Hero -> 한국어 문제 -> 영어 문장 -> 입력 필드 -> Log Message -> Submit Button -> 하단 고정 버튼
    """
    st.markdown("""
    <style>
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

    /* ========== 상단바 (학습모드 선택) ========== */
    .stSelectbox {
        margin: 0 !important;
        padding: 0.5rem 1rem !important;
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
        font-family: 'Comic Sans MS', cursive;
        font-size: 2.0rem;
        text-shadow: 2px 2px 0px #FF69B4;
        margin: 0;
        letter-spacing: 1px;
        text-align: center;
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
        padding: 1rem 0.5rem;
        gap: 1rem;
    }

    /* ========== 문제 영역 (한국어) - 삭제됨 ========== */
    .problem-box {
        width: 100%;
        max-width: 600px;
        background-color: linear-gradient(to right, #FFF0F5, #FFFFFF);
        padding: 1.2rem;
        border-radius: 20px;
        border: 3px solid #FFB6C1;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.4);
        text-align: center;
        margin-bottom: 0.5rem;

    }

    .problem-label {
        font-size: 1.1rem;
        color: #C4DF25;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .korean-sentence {
        font-family: 'Nanum Gothic', sans-serif;
        font-size: 1.3rem;
        text-align: center;
        color: #DE8499;
        font-weight: bold;
        word-break: keep-all;
        line-height: 1.4;
    }

    /* ========== 영어 문장 영역 ========== */
    .english-section {
        width: 100%;
        max-width: 600px;
        text-align: center;
    }

    .english-label {
        font-size: 1.1rem;
        color: #C4DF25;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .english-sentence {
        font-family: 'Comic Sans MS', cursive;
        font-size: 1.3rem;
        text-align: center;
        padding: 1.2rem;
        color: #FF69B4;
        background: linear-gradient(to right, #FFF0F5, #FFFFFF);
        border-radius: 15px;
        border: 2px dashed #FFB6C1;
        font-weight: bold;
        line-height: 1.8;
        box-shadow: 0 4px 10px rgba(255, 182, 193, 0.2);
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
        align-items: center;
        justify-content: center;
        gap: 1rem;
        width: 100%;
        max-width: 600px;
        flex-wrap: wrap;
    }

    .input-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .input-icon {
        font-size: 1rem;
        font-weight: bold;
        color: #FF69B4;
        min-width: 20px;
        text-align: center;
    }

    .stTextInput > div > div > input {
        background: white !important;
        border: 3px solid #98FB98 !important;
        border-radius: 15px !important;
        padding: 10px 14px !important;
        font-size: 1.3rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important;
        color: #FF69B4 !important;
        min-width: 150px !important;
        max-width: 200px !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #FFB6C1 !important;
        box-shadow: 0 0 12px rgba(255, 182, 193, 0.8) !important;
        background: #FFF5F8 !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #ccc !important;
    }

    /* ========== Log Message 영역 ========== */
    .log-message {
        width: 100%;
        max-width: 600px;
        text-align: center;
        min-height: 2rem;
    }

    .stSuccess {
        background: #E8F8F5 !important;
        border: 2px solid #27AE60 !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
    }

    .stError {
        background: #FADBD8 !important;
        border: 2px solid #E74C3C !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
    }

    .stInfo {
        background: #D6EAF8 !important;
        border: 2px solid #3498DB !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
    }

    .stWarning {
        background: #FCF3CF !important;
        border: 2px solid #F39C12 !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
    }

    /* ========== Form Submit Button ========== */
    .stFormSubmitButton > button {
        background-color: #FF69B4 !important;
        color: white !important;
        width: 100% !important;
        max-width: 600px !important;
        font-size: 1.3rem !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        margin-bottom: 2rem !important;
    }

    .stFormSubmitButton > button:hover {
        background-color: #FF1493 !important;
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* ========== 하단 버튼 (고정) ========== */
    .bottom-buttons {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, #FFF0F5, #FFFFFF);
        padding: 1rem;
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
            padding: 0.8rem 0.3rem;
        }

        .problem-box {
            padding: 1rem;
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
    2. 한국어 문제 (박스)
    3. 영어 문장
    4. 입력 필드 (2개 나란히)
    5. Log Message
    6. Form Submit
    7. 하단 고정 버튼
    """
    inject_custom_css()
    render_mini_hero()
    
    # ========== 메인 컨테이너 시작 ==========
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    # --- [수정] 한국어 문제 영역 추가 ---
    st.markdown(f"""
    <div class="problem-box">
        <div class="problem-label">🌟 한글 문장이에요.</div>
        <div class="korean-sentence">{korean_sentence}</div>
    </div>
    """, unsafe_allow_html=True)
    # --- 영어 문장 영역 ---
    st.markdown(f"""
    <div class="english-section">
        <div class="english-label">📝 영어 문장이에요</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="english-sentence">{english_blanked_sentence}</div>', unsafe_allow_html=True)
    
    # --- 입력 필드 레이블 ---
    st.markdown("""
    <div class="input-label">✏️ 빈칸을 채워주세요</div>
    """, unsafe_allow_html=True)
    
    with st.form(key='answer_form'):
        # --- 입력 필드들 (2개 그룹) ---
        st.markdown('<div class="input-group">', unsafe_allow_html=True)
        
        user_answers = []
        for i in range(len(answers)):
            st.markdown(f"""
            <div class="input-item">
                <span class="input-icon">({i+1})</span>
            </div>
            """, unsafe_allow_html=True)
            ans = st.text_input(
                f"빈칸 {i+1}",
                key=f"input_{i}",
                placeholder="답",
                label_visibility="collapsed"
            )
            user_answers.append(ans)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Log Message 영역 ---
        st.markdown('<div class="log-message">', unsafe_allow_html=True)
        
        if show_hint:
            hint_text = " / ".join([f"({i+1}) '{ans[:2]}...'" for i, ans in enumerate(answers)])
            st.info(f"💡 힌트: {hint_text}")
        
        if show_answer:
            answer_text = " / ".join([f"({i+1}) {ans}" for i, ans in enumerate(answers)])
            st.warning(f"✅ 정답: {answer_text}")
            st.markdown(f"<p style='text-align: center; font-size: 1.3rem; color: #666; margin: 0.5rem 0 0 0;'><strong>전체:</strong> {full_english_sentence}</p>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # --- Form Submit 버튼 ---
        submit_clicked = st.form_submit_button(
            label='🔮 정답 확인하기',
            type="primary",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)  # main-container 종료
    
    # 하단 버튼 영역을 위한 여백
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # ========== 하단 버튼 (고정 위치) ==========
    st.markdown('<div class="bottom-buttons" id="bottom-buttons">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        check_clicked = st.button(
            "✅ 확인",
            key="btn_check",
            use_container_width=True,
            help="다시 확인"
        )
    
    with col2:
        hint_clicked = st.button(
            "💡 힌트",
            key="btn_hint",
            use_container_width=True,
            help="첫 글자 확인"
        )
    
    with col3:
        next_clicked = st.button(
            "⏭️ 다음",
            key="btn_next",
            use_container_width=True,
            help="다음 문제"
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
    inject_custom_css()
    render_mini_hero()
    
    # ========== 메인 컨테이너 시작 ==========
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # --- 입력 레이블 ---
    st.markdown("""
    <div class="input-label">✏️ 영어 뜻을 입력하세요</div>
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
