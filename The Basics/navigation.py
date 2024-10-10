
'''
Multi-page apps: Streamlit doesn’t have built-in multi-page support, but you can simulate it using sidebars, radio buttons, or custom navigation.
'''

import streamlit as st # type : ignore

page = st.sidebar.radio('Navigation', ['Home', 'About', 'Data'])
if page == 'Home':
    st.title('Home Page')
elif page == 'About':
    st.title('About Us')
elif page == 'Data':
    st.title('Data Page')
