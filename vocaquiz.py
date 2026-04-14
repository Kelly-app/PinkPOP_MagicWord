import streamlit as st
import random
import uilayout

def init_voca_state():
    # Voca 퀴즈용 상태가 없으면 초기화
    if 'voca_word' not in st.session_state:
        st.session_state['voca_word'] = ""
        st.session_state['voca_meaning'] = ""
        st.session_state['voca_show_hint'] = False
        st.session_state['voca_show_answer'] = False
        st.session_state['voca_input_field'] = ""

def next_voca_question(voca_data):
    if not voca_data:
        return
        
    # 데이터에서 랜덤으로 한 줄 뽑기
    row = random.choice(voca_data)
    st.session_state['voca_word'] = str(row.get("Englishword", ""))
    st.session_state['voca_meaning'] = str(row.get("English Meaning", ""))
    st.session_state['voca_show_hint'] = False
    st.session_state['voca_show_answer'] = False
    # ➕ 입력값 초기화: 다음 문제로 이동할 때 input box 값 지우기
    if 'voca_input_field' not in st.session_state:
        st.session_state['voca_input_field'] = ""

def run_voca_quiz(voca_data):
    """Voca Quiz 메인 실행 함수"""
    init_voca_state()
    
    # 첫 문제 로딩
    if not st.session_state['voca_word'] and voca_data:
        next_voca_question(voca_data)
        
    # Voca Quiz 전용 UI 화면 그리기 (단어와 뜻의 순서 변경 반영)
    ui_result = uilayout.build_voca_ui_layout(
        word=st.session_state.get('voca_word', ''),
        meaning=st.session_state.get('voca_meaning', ''),
        show_hint=st.session_state.get('voca_show_hint', False),
        show_answer=st.session_state.get('voca_show_answer', False)
    )
    
    # 버튼 클릭 이벤트 처리
    if ui_result['hint_clicked']:
        st.session_state['voca_show_hint'] = True
        st.rerun()
        
    if ui_result['answer_clicked']:
        st.session_state['voca_show_answer'] = True
        st.rerun()
        
    if ui_result['next_clicked']:
        next_voca_question(voca_data)
        st.rerun()
        
    # 정답 제출 시 채점 로직
    if ui_result['submit_clicked']:
        user_ans = ui_result['user_answer']
        # 🔥 정답 비교 대상을 'word'에서 'meaning'으로 변경했습니다!
        real_ans = st.session_state['voca_meaning'] 
        
        # 공백 제거 및 대소문자 무시 비교
        if user_ans.strip().lower() == real_ans.strip().lower():
            st.success("🎉 정답입니다! 반짝이는 보석을 얻었어요!")
            uilayout.throw_gems()
            # 🔥 별을 보석으로 변경
            st.markdown('<div class="star-rating"><div class="star">💎</div><div class="star">💎</div><div class="star">💎</div></div>', unsafe_allow_html=True)
        else:
            st.error("😅 아쉽네요. 다시 한번 뜻을 생각해 볼까요?")