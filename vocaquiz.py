import streamlit as st
import random
import uilayout
# vocaquiz.py 상단에 추가
from sentence_transformers import SentenceTransformer, util

# ➕ vocaquiz.py에 이 함수 추가
@st.cache_resource
def load_sbert_model():
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def semantic_search_match(user_answer, correct_meaning, threshold=0.65):
    """의미 유사도 검증"""
    try:
        if 'sbert_loaded' not in st.session_state:
            with st.spinner("🔄 모델 로딩 중... (처음 한 번만)"):
                _ = load_sbert_model()
            st.session_state['sbert_loaded'] = True
            st.success("✨ 로드 완료! 게임을 시작하세요!")

            
            user_emb = model.encode(user_answer, convert_to_tensor=True)
            correct_emb = model.encode(correct_meaning, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(user_emb, correct_emb).item()
        return {
            'is_correct': similarity >= threshold,
            'similarity': similarity
        }
    except Exception as e:
        st.warning(f"오류: {str(e)}")
        return {'is_correct': False, 'similarity': 0.0}


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
        # ✅ 1단계: 정확한 일치 확인
        if user_ans.strip().lower() == real_ans.strip().lower():
            is_correct = True
            similarity = 1.0
            st.success("🎉 정답입니다! 반짝이는 보석을 얻었어요!")
            uilayout.throw_gems()
            # 🔥 별을 보석으로 변경
            st.markdown('<div class="star-rating"><div class="star">💎</div><div class="star">💎</div><div class="star">💎</div></div>', unsafe_allow_html=True)
        else:
            # ✅ 2단계: 의미 유사도 확인
            result = semantic_search_match(user_ans, real_ans, 0.65)
            is_correct = result['is_correct']
            similarity = result['similarity']
            st.error(f"😅 아쉽네요. 유사도:{similarity}")