import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
#from st_aggrid import AgGrid

st.set_page_config(
    page_title='Multipage App',
    page_icon='πΌ'
)

st.title('Main Page')
#st.sidebar.success('select a page above')

st.sidebar.button('open_page')

data = st.file_uploader('μμν  νμΌμ μ ννμΈμ', type=['csv', 'txt'])

if data is not None:
    df = pd.read_csv(data)
    st.dataframe(df)

# if 'my_input' not in st.session_state:
#     st.session_state['my_input'] = ""

# my_input = st.text_input('λ΄μ©μ μλ ₯νμΈμ', st.session_state['my_input'])
# submit = st.button('νμΈ')

# if submit:
#     st.session_state['my_input'] = my_input
#     st.write('μλ ₯νμ  λ΄μ©μ: ', my_input)
