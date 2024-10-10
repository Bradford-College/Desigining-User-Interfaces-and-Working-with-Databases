'''
A Simple Streamlit app for sidebar
'''
import streamlit as st # type: ignore
st.title('Working with Sidebar')

st.sidebar.title('Sidebar Title')
st.sidebar.header('Options')

'''
st.sidebar.title() and st.sidebar.header()
Add elements in a collapsible sidebar for navigation or organizing controls.
'''

option1 = st.sidebar.selectbox('Select an option', ['Option 1', 'Option 2'], key='selectbox1')
st.write(f'You selected {option1}')

'''
Sidebar Input Widgets
Same as main content, but in the sidebar:
Text Input: st.sidebar.text_input()
Sliders: st.sidebar.slider()
'''
option2 = st.sidebar.selectbox('Select an option', ['Option 1', 'Option 2'], key='selectbox2')
st.write(f'You selected {option2}')
