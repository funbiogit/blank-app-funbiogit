import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 폰트 설정을 위한 모듈 추가

st.title("학생 성적 분석 및 시각화")  # 페이지 제목

# 1. 데이터 직접 입력
data = {
    '이름': ['홍길동', '김영희', '이철수', '박민수', '최지은'],
    '수학': [85, 90, 70, 95, 60],
    '영어': [78, 88, 65, 92, 72],
    '과학': [92, 84, 75, 89, 68]
}
df = pd.DataFrame(data)  # 데이터프레임 생성

st.subheader("학생 성적 데이터")
st.dataframe(df)  # 데이터프레임 표시

# 2. 학생별 평균 성적 계산
score_cols = ['수학', '영어', '과학']
df['평균'] = df[score_cols].mean(axis=1)  # 평균 성적 계산
st.subheader("학생별 평균 성적")
st.dataframe(df[['이름', '평균']])  # 학생별 평균 성적 표시

# 3. 과목별 석차 계산
st.subheader("과목별 석차")
rank_df = pd.DataFrame()
rank_df['이름'] = df['이름']
for col in score_cols:
    rank_df[f'{col}_석차'] = df[col].rank(ascending=False, method='min').astype(int)  # 석차 계산
st.dataframe(rank_df)  # 과목별 석차 표시

# 4. 한글 폰트 설정 (NanumGothic-Bold.ttf 사용)
font_path = "./fonts/NanumGothic-Bold.ttf"
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 5. 과목별 성적 분포 시각화
st.subheader("과목별 성적 분포")
fig, ax = plt.subplots()
for col in score_cols:
    ax.plot(df['이름'], df[col], marker='o', label=col)  # 각 과목별 성적 그래프
ax.set_title("학생별 과목 성적", fontproperties=fontprop)
ax.set_xlabel("이름", fontproperties=fontprop)
ax.set_ylabel("점수", fontproperties=fontprop)
ax.legend(prop=fontprop)
plt.xticks(rotation=45, fontproperties=fontprop)
st.pyplot(fig) # 그래프 표시