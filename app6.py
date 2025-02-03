# 파일 업로드 하는 방법
import streamlit as st
from datetime import datetime

def save_uploaded_file(directory, file): #파일을 
    # 1. 디렉토리가 없으면 만든다. 
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
    main()
    # 2. 이 디렉토리에 파일을 저정한다.
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장완료 됐으니 ,유저에게 알려준다.
    st.success(f'저장완료: {directory}에 {file.name} 저장되었습니다.')
                       


def main() :
    file = st.file_uploader('이미지 파일 선택하세요', type= ['jpg', 'png', 'jpeg', 'webp'] )
    # 업로드한 파일 저장하기
    if file is not None:
        # 유저가 올린 파일이 있을 때만, 파일을 저장하도록 한다.
        # 1. 파일명을 유니크하게 만든다.
        print(datetime.now().isoformat().replace(':','_') +  '.jpg' )
        new_filename = datetime.now().isoformat().replace(':','_') +  '.jpg' 
        file.name = new_filename
        save_uploaded_file('images', file)




if __name__ == '__main__' :
    main()

