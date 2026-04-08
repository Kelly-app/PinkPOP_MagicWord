import streamlit as st
import random

def inject_custom_css():
    st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; background-image: radial-gradient(#FFB6C1 1px, transparent 1px), radial-gradient(#98FB98 1px, transparent 1px); background-size: 50px 50px; background-position: 0 0, 25px 25px; }
    .main-header { background: linear-gradient(135deg, #FFB6C1 0%, #D8BFD8 50%, #98FB98 100%); border-radius: 0 0 30px 30px; padding: 1.5rem; text-align: center; box-shadow: 0 4px 15px rgba(255, 182, 193, 0.3); margin-bottom: 2rem; }
    .main-header h1 { color: white; font-family: 'Comic Sans MS', cursive; font-size: 2.8rem; text-shadow: 2px 2px 0px #FF69B4; margin: 0; letter-spacing: 1px; }
    .main-header p { color: white; font-size: 1.2rem; margin: 0.5rem 0 0 0; font-weight: bold; }
    .cloud-container { background: white; border-radius: 25px; border: 3px dashed #87CEFA; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 8px 20px rgba(135, 206, 250, 0.2); position: relative; }
    .cloud-container::before { content: '💎'; position: absolute; top: -15px; left: 20px; font-size: 1.5rem; }
    .korean-sentence { background: #FFFACD; border-radius: 20px; padding: 1rem; margin: 1rem 0; border: 2px solid #FFDAB9; font-size: 1.3rem; text-align: center; color: #4A4A4A; }
    .english-sentence { font-family: 'Comic Sans MS', cursive; font-size: 2rem; text-align: center; padding: 1rem; color: #FF69B4; background: linear-gradient(to right, #FFF0F5, #FFFFFF); border-radius: 15px; margin: 1rem 0; font-weight: bold; }
    .stTextInput > div > div > input { background: white; border: 2px solid #98FB98; border-radius: 15px; padding: 12px; font-size: 1.2rem; text-align: center; transition: all 0.3s ease; }
    .stTextInput > div > div > input:focus { border-color: #FFB6C1; box-shadow: 0 0 10px rgba(255, 182, 193, 0.8); }
    .stFormSubmitButton > button { background-color: #FF69B4 !important; color: white !important; width: 100%; font-size: 1.2rem; border-radius: 20px; border: none; padding: 12px 24px; font-weight: bold; }
    hr.divider { border: none; height: 3px; background: linear-gradient(to right, #FFB6C1, #D8BFD8, #98FB98); margin: 2rem 0; border-radius: 3px; }
    .star-rating { display: flex; justify-content: center; gap: 10px; margin: 1rem 0; }
    .star { font-size: 2.5rem; animation: twinkle 0.8s infinite alternate; }
    @keyframes twinkle { from { opacity: 0.6; transform: scale(0.9); } to { opacity: 1; transform: scale(1.2); } }
    </style>
    """, unsafe_allow_html=True)

def render_header(app_title="PinkPOP Magic Word Land", subtitle="맞추면 보석이 반짝!"):
    st.markdown(f"""
    <div class="main-header">
        <h1>✨ {app_title} ✨</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_problem_container(korean_sentence, english_blanked_sentence):
    with st.container():
        st.markdown('<div class="cloud-container">', unsafe_allow_html=True)
        st.markdown(f'<div class="korean-sentence">{korean_sentence}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="english-sentence">{english_blanked_sentence}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_input_fields(num_blanks):
    user_answers = []
    cols = st.columns(max(1, num_blanks if num_blanks <= 3 else 3))
    
    for i in range(num_blanks):
        col_idx = i % len(cols)
        with cols[col_idx]:
            ans = st.text_input(f"빈칸 {i+1}", key=f"input_{i}")
            user_answers.append(ans)
    return user_answers

def render_control_buttons():
    col1, col2, col3 = st.columns(3)
    hint_clicked = col1.button("💡 힌트 보기")
    answer_clicked = col2.button("👀 정답 보기")
    next_clicked = col3.button("⏭️ 다음 문제")
    return hint_clicked, answer_clicked, next_clicked

# --- 빈칸 채우기용 레이아웃 ---
def build_ui_layout(korean_sentence, english_blanked_sentence, answers, full_english_sentence, show_hint, show_answer):
    inject_custom_css()
    render_header(app_title="PinkPOP Magic Word Land 💎", subtitle="맞추면 보석이 반짝!")
    render_problem_container(korean_sentence, english_blanked_sentence)
    
    with st.form(key='answer_form'):
        user_answers = render_input_fields(len(answers))
        submit_clicked = st.form_submit_button(label='🔮 정답 확인하기', type="primary", use_container_width=True)
    
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    hint_clicked, answer_clicked, next_clicked = render_control_buttons()
    
    if show_hint:
        st.info("💡 힌트: " + " / ".join([f"첫 글자: '{ans[0]}...'" for ans in answers]))
    if show_answer:
        st.warning("✅ 정답: " + ", ".join(answers))
        st.markdown(f"**📖 전체 문장:** {full_english_sentence}")
        
    return {'user_answers': user_answers, 'submit_clicked': submit_clicked, 'hint_clicked': hint_clicked, 'answer_clicked': answer_clicked, 'next_clicked': next_clicked}

# --- Voca Quiz용 레이아웃 ---
def build_voca_ui_layout(word, meaning, show_hint, show_answer):
    inject_custom_css()
    # 타이틀 변경
    render_header(app_title="PinkPOP Magic Word Land 💎", subtitle="뜻을 맞추면 보석이 반짝!")
    
    with st.container():
        st.markdown('<div class="cloud-container">', unsafe_allow_html=True)
        # 🔥 화면 중앙에 'English Word'가 큼지막하게 표시됩니다!
        st.markdown(f'<div class="english-sentence">🔤 {word}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with st.form(key='voca_form'):
        # 🔥 입력창 질문 변경
        user_answer = st.text_input("이 단어의 영어 뜻(Meaning)은 무엇일까요?", key="voca_input_field")
        submit_clicked = st.form_submit_button(label='🔮 정답 확인하기', type="primary", use_container_width=True)
        
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    hint_clicked, answer_clicked, next_clicked = render_control_buttons()
    
    # 힌트는 정답인 'Meaning'의 첫 글자를 보여줍니다.
    if show_hint and meaning:
        st.info(f"💡 힌트: 뜻은 '{meaning[0]}' (으)로 시작해요!")
    if show_answer:
        st.warning(f"✅ 정답: {meaning}")
        
    return {'user_answer': user_answer, 'submit_clicked': submit_clicked, 'hint_clicked': hint_clicked, 'answer_clicked': answer_clicked, 'next_clicked': next_clicked}
    
def throw_gems():
    """정답 시 보석과 반짝이가 쏟아지는 커스텀 애니메이션"""
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
        0% { transform: translateY(-10vh) rotate(0deg) scale(1); opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg) scale(1.5); opacity: 0; }
    }
    </style>
    """
    
    # 💎 보석과 ✨ 반짝이를 화면 곳곳에 랜덤하게 생성
    emojis = ['💎', '✨', '💖', '💎', '🌟']
    for _ in range(30): # 30개의 보석이 떨어짐
        emoji = random.choice(emojis)
        left = random.randint(0, 100) # 가로 위치 랜덤 (0~100%)
        delay = random.uniform(0, 1.5) # 떨어지는 시간차 랜덤
        duration = random.uniform(2, 4) # 떨어지는 속도 랜덤
        size = random.uniform(1.5, 3) # 크기 랜덤
        
        html_code += f'<div class="gem-drop" style="left: {left}vw; animation-delay: {delay}s; animation-duration: {duration}s; font-size: {size}rem;">{emoji}</div>'
        
    st.markdown(html_code, unsafe_allow_html=True)