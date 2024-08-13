import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv("Pokemon.csv")

st.set_page_config(page_title='Myapp')
st.title('This is my first app')
st.subheader('This is my first code')
st.sidebar.title('MENU')
choice = st.sidebar.radio('options',['Data1','Data2','Data3'])

if choice == 'Data1':
    st.header('Presenting Dataset')
    st.dataframe(df)
 






