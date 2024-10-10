'''
A Simple Streamlit app for writing output
'''

import streamlit as st # type: ignore
import pandas as pd
st.title('Working with Output')

'''
st.write()
Displays various types of outputs, including text, data frames, charts, and more.
'''
df = [1,2,3,4]
st.write('This is a DataFrame:', df)

'''
Tables: st.table()
Renders a static table for displaying tabular data.
'''
st.table(df)

'''
Charts: st.line_chart(), st.bar_chart()
Used for visualizing data.
'''
st.line_chart(df)
