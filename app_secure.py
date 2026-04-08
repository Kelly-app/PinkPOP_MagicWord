import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import spacy
import random

# 분리된 모듈 불러오기
import uilayout
import vocaquiz

# Credential info
import os
from pathlib import 

@st.cache_resource

def load_credentials():
    """Streamlit Secrets로부터 자격증명 로드"""
    credentials_dict = st.secrets["google_credentials"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict, 
        scope=["https://spreadsheets.google.com/feeds", 
               "https://www.googleapis.com/auth/drive"]
    )
    return creds


def load_nlp_model():
    return spacy.load("en_core_web_sm")

# 인자로 시트 이름(sheet_name)을 받도록 수정됨
@st.cache_data(ttl=600)
def load_data(sheet_name):
    try:
    
        creds = load_credentials()  # ✅ Secrets에서 로드
        
        client = gspread.authorize(creds)
        
        # 워크북 열기
        workbook = client.open_by_url("https://docs.google.com/spreadsheets/d/1LagGKqkKj_ToCtQ4v8OQ6jqy7qrKZnSahWbwg6drCoQ/edit")
        
        # sheet1 대신 인자로 받은 시트 이름으로 연결!
        sheet = workbook.worksheet(sheet_name)
        records = sheet.get_all_records()
        
        if not records:
            st.error(f"'{sheet_name}' 시트에 데이터가 없습니다.")
            return []
        return records
        
    except gspread.exceptions.WorksheetNotFound:
        st.error(f"❌ '{sheet_name}' 시트를 찾을 수 없습니다. 구글 시트 탭 이름을 정확히 변경해주세요!")
        return []
    except Exception as e:
        st.error(f"데이터 로드 실패: {str(e)}")
        return []

def create_blank_sentence(english_sentence):
    nlp = load_nlp_model()
    doc = nlp(english_sentence)
    candidates = [token for token in doc if token.pos_ in ['VERB', 'ADJ', 'ADV'] and token.is_alpha]
    if not candidates:
        candidates = [token for token in doc if token.pos_ in ['NOUN'] and token.is_alpha]
        
    num_blanks = min(2, len(candidates))
    chosen_tokens = random.sample(candidates, num_blanks)
    chosen_indices = [token.i for token in chosen_tokens]
    
    blanked_text = ""
    answers = []
    
    for token in doc:
        if token.i in chosen_indices:
            blanked_text += "______" + token.whitespace_
            answers.append(token.text)
        else:
            blanked_text += token.text_with_ws
            
    return blanked_text.strip(), answers

def next_fillblank_question(data):
    if not data:
        return
    row = random.choice(data)
    kor_sentence = row.get("Korean", "")
    eng_sentence = row.get("English", "")
    blanked_eng, answers = create_blank_sentence(eng_sentence)
    
    st.session_state['kor'] = kor_sentence
    st.session_state['eng_full'] = eng_sentence
    st.session_state['eng_blanked'] = blanked_eng
    st.session_state['answers'] = answers
    st.session_state['show_hint'] = False
    st.session_state['show_answer'] = False

def run_fillblank_logic(data):
    """빈칸 채우기 메인 실행 함수"""
    if 'kor' not in st.session_state or not st.session_state['kor']:
        next_fillblank_question(data)
    
    ui_result = uilayout.build_ui_layout(
        korean_sentence=st.session_state.get('kor', ''),
        english_blanked_sentence=st.session_state.get('eng_blanked', ''),
        answers=st.session_state.get('answers', []),
        full_english_sentence=st.session_state.get('eng_full', ''),
        show_hint=st.session_state.get('show_hint', False),
        show_answer=st.session_state.get('show_answer', False)
    )
    
    if ui_result['hint_clicked']:
        st.session_state['show_hint'] = True
        st.rerun()
    if ui_result['answer_clicked']:
        st.session_state['show_answer'] = True
        st.rerun()
    if ui_result['next_clicked']:
        next_fillblank_question(data)
        st.rerun()
        
    if ui_result['submit_clicked']:
        correct_answers = st.session_state.get('answers', [])
        user_answers = ui_result['user_answers']
        
        correct_count = 0
        for user_ans, real_ans in zip(user_answers, correct_answers):
            if user_ans.strip().lower() == real_ans.strip().lower():
                correct_count += 1
                
        total_blanks = len(correct_answers)
        if correct_count == total_blanks and total_blanks > 0:
            st.success("🎉 정답입니다! 완벽해요!")
            st.balloons()
            st.markdown('<div class="star-rating"><div class="star">⭐</div><div class="star">⭐</div><div class="star">⭐</div></div>', unsafe_allow_html=True)
        else:
            st.error(f"😅 아쉽네요. {total_blanks}개 중 {correct_count}개 맞췄습니다.")

def main():
    # 🔥 브라우저 탭 이름과 아이콘을 보석으로 변경
    st.set_page_config(page_title="PinkPOP Magic Word Land", page_icon="💎", layout="wide")
    
    mode = st.selectbox("🎯 학습 모드를 선택하세요!", ["✨ 빈칸채우기 (문장)", "📖 Voca Quiz (영단어)"])
    
    st.markdown("<br>", unsafe_allow_html=True) # 여백 추가
    
    if mode == "✨ 빈칸채우기 (문장)":
        data = load_data("FillBlnk") # FillBlnk 시트에서 데이터 가져옴
        if data:
            run_fillblank_logic(data)
            
    elif mode == "📖 Voca Quiz (영단어)":
        data = load_data("VocaQz") # VocaQz 시트에서 데이터 가져옴
        if data:
            vocaquiz.run_voca_quiz(data)
            
# 정답을 맞췄을 때 보석이 뜨도록 run_fillblank_logic 안의 성공 메시지도 수정
def run_fillblank_logic(data):
    if 'kor' not in st.session_state or not st.session_state['kor']:
        next_fillblank_question(data)
    
    ui_result = uilayout.build_ui_layout(
        korean_sentence=st.session_state.get('kor', ''),
        english_blanked_sentence=st.session_state.get('eng_blanked', ''),
        answers=st.session_state.get('answers', []),
        full_english_sentence=st.session_state.get('eng_full', ''),
        show_hint=st.session_state.get('show_hint', False),
        show_answer=st.session_state.get('show_answer', False)
    )
    
    if ui_result['hint_clicked']:
        st.session_state['show_hint'] = True
        st.rerun()
    if ui_result['answer_clicked']:
        st.session_state['show_answer'] = True
        st.rerun()
    if ui_result['next_clicked']:
        next_fillblank_question(data)
        st.rerun()
        
    if ui_result['submit_clicked']:
        correct_answers = st.session_state.get('answers', [])
        user_answers = ui_result['user_answers']
        
        correct_count = 0
        for user_ans, real_ans in zip(user_answers, correct_answers):
            if user_ans.strip().lower() == real_ans.strip().lower():
                correct_count += 1
                
        total_blanks = len(correct_answers)
        if correct_count == total_blanks and total_blanks > 0:
            st.success("🎉 정답입니다! 반짝이는 보석을 얻었어요!")
            uilayout.throw_gems()
            # 🔥 여기서 별 대신 보석 출력
            st.markdown('<div class="star-rating"><div class="star">💎</div><div class="star">💎</div><div class="star">💎</div></div>', unsafe_allow_html=True)
        else:
            st.error(f"😅 아쉽네요. {total_blanks}개 중 {correct_count}개 맞췄습니다.")
            
if __name__ == "__main__":
    main()