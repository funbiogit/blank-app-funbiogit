import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("Matplotlib 데이터 시각화 예시")

# 샘플 데이터 생성
x = np.arange(1, 11)
y = np.random.randint(10, 100, size=10)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', label='데이터 값')
ax.set_title('샘플 데이터 그래프 (한글 제목)')
ax.set_xlabel('X축 (한글)')
ax.set_ylabel('Y축 (한글)')
ax.legend()

# Streamlit에 그래프 표시
st.pyplot(fig)