import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
#from st_aggrid import AgGrid

st.set_page_config(
    page_title='Multipage App',
    page_icon='🔼'
)

st.title('Main Page')
#st.sidebar.success('select a page above')

st.sidebar.button('open_page')

data = st.file_uploader('작업할 파일을 선택하세요', type=['csv', 'txt'])

if data is not None:
    df = pd.read_csv(data)
    st.dataframe(df)

# if 'my_input' not in st.session_state:
#     st.session_state['my_input'] = ""

# my_input = st.text_input('내용을 입력하세요', st.session_state['my_input'])
# submit = st.button('확인')

# if submit:
#     st.session_state['my_input'] = my_input
#     st.write('입력하신 내용은: ', my_input)
