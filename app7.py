# 파일 업로드 + 사이드바
from datetime import datetime
import pandas as pd
import streamlit as st

from app6 import save_uploaded_file


def main():
    st.title('파일 업로드 예제')
    st.sidebar.title('사이드바')
    menu = ['이미지 파일 업로드', 'CSV 파일 업로드', 'PDF 파일 업로드' ]
    choice = st.sidebar.selectbox('메뉴를 선택하세요', menu)
    print(choice)

    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')
        # 이미지 파일 업로드
        file = st.file_uploader('이미지 파일 업로드', type=['jpg', 'png', 'jpeg', 'webp'] )

        if file is not None:
        # 1. 파일 이름을 유니크하게 만든다.

           new_filename = datetime.now().isoformat().replace(':','_') +  '.jpg' 
           file.name = new_filename

        # 2. 파일 저장한다.
           save_uploaded_file('images', file)
    
        # 3. 저장완료 됐으니 ,유저에게 알려준다.
           st.image(file, use_container_width=True)


    elif choice == menu[1]:
        st.subheader('CSV 파일 업로드')

        file = st.file_uploader('CSV 파일 업로드', type=['csv'] )
        if file is not None:
            # 1. 파일 저장한다.
            save_uploaded_file('csv', file)
            df = pd.read_csv(file)
            # 2. csv 파일을 화면에 보여준다.
            st.dataframe(df)


    elif choice == menu[2]:
        st.subheader('PDF 파일 업로드')

        file = st.file_uploader('PDF 파일 업로드', type=['pdf'] )
        if file is not None:
            # 1. 파일을 저장하고,
            save_uploaded_file('pdf',file)
            # 2. pdf 파일을 화면에 보여준다.
            st.write(file)


if __name__ == '__main__':
    main()
