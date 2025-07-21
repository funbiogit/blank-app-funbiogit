import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("성적 분석 및 시각화")  # 페이지 제목

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])  # 파일 업로드 위젯

if uploaded_file is not None:
    # 2. 데이터 읽기
    df = pd.read_csv(uploaded_file)  # pandas로 데이터프레임 생성
    st.subheader("업로드된 데이터")  # 데이터 표시 제목
    st.dataframe(df)  # 데이터프레임 표시

    # 3. 학생별 평균 성적 계산
    score_cols = ['수학', '영어', '과학']
    if all(col in df.columns for col in ['이름'] + score_cols):
        df['평균'] = df[score_cols].mean(axis=1)
        st.subheader("학생별 평균 성적")
        st.dataframe(df[['이름', '평균']])

        # 4. 과목별 석차 계산 및 표시
        st.subheader("과목별 석차")
        rank_df = pd.DataFrame()
        rank_df['이름'] = df['이름']
        for col in score_cols:
            rank_df[f'{col}_석차'] = df[col].rank(ascending=False, method='min').astype(int)
        st.dataframe(rank_df)

        # 5. 과목별 성적 분포 시각화
        st.subheader("과목별 성적 분포")
        fig, ax = plt.subplots()
        for col in score_cols:
            ax.plot(df['이름'], df[col], marker='o', label=col)
        ax.set_title("학생별 과목 성적")
        ax.set_xlabel("이름")
        ax.set_ylabel("점수")
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("필요한 컬럼(이름, 수학, 영어, 과학)이 모두 존재해야 합니다.")
else:
    st.info("CSV 파일을 업로드하면 성적 분석 결과와 그래프가 표시됩니다.")