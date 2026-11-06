import streamlit as st
import pandas as pd

st.title("나의 수업 시간표")
st.header("정적 시간표 (st.table)")
data = {"요일":["월","화","수","목","금"], "1교시":["심개","전공","","전공","컴탐"], "2교시":["심개","","","","컴탐"], "3교시":["심개","","","","컴탐"]}
df = pd.DataFrame(data)
st.table(df)

st.header("수업 정보 (st.json)")
json_data = {"컴탐":{"교수":"변해선","강의실":"26동 104호"},"심개":{"교수":"김수안","강의실":"83동 506호"},"전공":{"교수":"민경덕","강의실":"301동 301호"}}
st.json(json_data)

st.header("이번 학기 요약 (st.metric)")
st.metric(label="수강 과목 수", value="5")
st.metric(label="총 학점", value="130", delta="+14")
