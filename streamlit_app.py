import streamlit as st

# 페이지 제목
st.title("🎈 Streamlit 요소 예시 페이지")

# 부제목
st.header("1. 텍스트 요소")

# 일반 텍스트
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트 출력

# 마크다운
st.markdown("**이것은 마크다운입니다.**")  # 마크다운 형식 텍스트
st.markdown("# 마크다운 헤더입니다.")  # 마크다운 헤더

# 코드 블록
st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록 표시

# 경고, 정보, 성공, 오류 메시지
st.success("성공 메시지입니다!")  # 성공 메시지
st.info("정보 메시지입니다.")     # 정보 메시지
st.warning("경고 메시지입니다!")  # 경고 메시지
st.error("오류 메시지입니다!")    # 오류 메시지

st.header("2. 입력 요소")

# 텍스트 입력
name = st.text_input("이름을 입력하세요")  # 텍스트 입력창

# 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력창

# 텍스트 영역
bio = st.text_area("자기소개를 입력하세요")  # 여러 줄 텍스트 입력창

# 체크박스
agree = st.checkbox("동의합니다")  # 체크박스

# 라디오 버튼
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼

# 셀렉트박스
country = st.selectbox("국가를 선택하세요", ["한국", "미국", "일본", "기타"])  # 드롭다운 셀렉트박스

# 멀티 셀렉트
hobbies = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "음악"])  # 다중 선택

# 슬라이더
score = st.slider("점수를 선택하세요", 0, 100, 50)  # 슬라이더

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드

st.header("3. 버튼 및 상호작용")

# 버튼
if st.button("클릭하세요"):  # 버튼
    st.write("버튼이 클릭되었습니다!")

# 다운로드 버튼
st.download_button("텍스트 다운로드", "이것은 다운로드할 텍스트입니다.", file_name="sample.txt")  # 다운로드 버튼

st.header("4. 데이터 표시")

# 테이블
import pandas as pd
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 32, 29]
})
st.table(df)  # 테이블 표시

# 데이터프레임
st.dataframe(df)  # 데이터프레임 표시 (스크롤 가능)

st.header("5. 차트 및 이미지")

# 라인 차트
st.line_chart(df['나이'])  # 라인 차트

# 바 차트
st.bar_chart(df['나이'])  # 바 차트

# 이미지 표시
from PIL import Image
import numpy as np
img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
st.image(img, caption="랜덤 이미지")  # 이미지 표시

st.header("6. 기타 요소")

# 진행률 표시줄
import time
progress = st.progress(0)  # 진행률 표시줄
for i in range(1, 101, 20):
    time.sleep(0.1)
    progress.progress(i)

# 스피너
with st.spinner("잠시만 기다려주세요..."):  # 스피너
    time.sleep(1)

# 사이드바
st.sidebar.title("사이드바 제목")  # 사이드바 제목
st.sidebar.write("사이드바에 표시되는 텍스트")  # 사이드바 텍스트

# Expander
with st.expander("더보기"):  # 확장 가능한 영역
    st.write("여기에 추가 정보를 입력하세요.")

# Divider
st.divider()  # 구분선

# 예시 페이지 끝
st.write("모든 Streamlit 주요 요소 예시가 포함되어 있습니다.")