import streamlit as st
import pandas as pd

st.title("나의 소개 페이지")
st.header("자기소개")
st.write("안녕하세요, 제 이름은 이해준입니다.")
st.write("저는 **기계설계**에 관심이 있습니다.")
st.subheader("좋아하는 것")
st.write("저는 노래 듣기를 좋아합니다.")
st.write("가장 자주 방문하는 사이트는 [구글](https://www.google.com)입니다.")
st.subheader("앞으로의 목표")
st.write("앞으로 각종 코드를 배워서 미래에 필요한 상황에 활용하고 싶습니다.")
st.caption("제가 좋아하는 파이썬 코드 예시")
st.code('import random\nlunch = ["Rice","Pasta","Pizza"]\nrandom.choice(lunch)')
