# 파일을 분리해서 개발하는 방법 적용.

import streamlit as st

from app8_eda import run_eda
from app8_home import run_home
from app8_ml import run_ml

def main():
    st.title('대시보드 앱 예제')

    st.sidebar.title('사이드 바')
    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox('메뉴',menu )

    if choice == menu[0]:
        # 함수호출
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()
    elif choice == menu[3]:
        pass

if __name__ == '__main__':
    main()