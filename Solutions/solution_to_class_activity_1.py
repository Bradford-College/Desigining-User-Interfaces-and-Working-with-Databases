# streamlit_app.py

# Importing the Streamlit library
import streamlit as st  # type: ignore

# Step 1: Add a title to your app
# This will be displayed at the top of the page
st.title("My First Streamlit App")

# Step 2: Create User Input - Ask the user for their name
# Using st.text_input() to capture text input from the user
name = st.text_input("Enter your name:")

# Step 3: Add functionality based on input
# When the 'Submit' button is clicked, the app will display a greeting message
if st.button("Submit"):
    # st.write() is used to display output on the Streamlit app
    st.write(f"Hello, {name}! Welcome to your first Streamlit app.")

# Step 4: Add another input widget
# Here, we use a slider to ask for the user's age
# The slider has a range from 0 to 100, with a default value of 25
age = st.slider("Select your age:", 0, 100, 25)

# Step 5: Add another button for the age input
# When clicked, this button will display the user's age
if st.button("Submit Age"):
    st.write(f"You are {age} years old!")

# Step 6: Optional - Add a checkbox to show an additional message
# If the checkbox is checked, a welcome message will be displayed
if st.checkbox("Show Welcome Message"):
    st.write(f"Welcome {name}!")

# Instructions for the students to run the app:
# 1. Save this file as streamlit_app.py
# 2. Open a terminal, navigate to the directory where the file is saved
# 3. Run the following command to start the Streamlit app:
#    streamlit run streamlit_app.py
# 4. The app will open in your web browser where you can interact with it
