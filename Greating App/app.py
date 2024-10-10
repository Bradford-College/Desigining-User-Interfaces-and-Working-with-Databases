import streamlit as st # type :ignore

# Set the title of the app
st.title("Personalized Greeting App")

# Sidebar options for greeting style
greeting_style = st.sidebar.selectbox(
    "Choose your greeting style:",
    ["Casual", "Formal", "Enthusiastic"]
)

# Main area for user input (name)
name = st.text_input("Enter your name:")

# Logic for generating greetings based on selected style
if name:
    if greeting_style == "Casual":
        greeting = f"Hey {name}, what's up?"
    elif greeting_style == "Formal":
        greeting = f"Good day, {name}. It's a pleasure to meet you."
    else:  # Enthusiastic
        greeting = f"Hello {name}!!! 🎉 Welcome aboard!"

    # Display the personalized greeting
    st.write(greeting)
else:
    st.write("Please enter your name to receive a personalized greeting.")
