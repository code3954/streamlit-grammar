# home 눌렀을 때 웹화면에 표시되는 내용

import streamlit as st

def run_home() :
    st.subheader('홈 화면입니다.')
    st.text('이 앱은 Streamlit을 연습하는 앱입니다.')
    st.image('data/image_03.jpg', width= 300)
    



