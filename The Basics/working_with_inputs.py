'''
A Simple Streamlit app for user input 
'''

import streamlit as st # type: ignore
import pandas as pd
st.title('File Upload')

'''
File Uploads
'''
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    
'''
User Input
'''
user_name = st.text_input('Enter your name')
st.write(f'Hello, {user_name}!')


'''
Text Area
'''
user_message = st.text_area('Your message')
st.write(f'You wrote: {user_message}')
