import streamlit as st #type : ignore

# Initialize session state for storing tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'completed' not in st.session_state:
    st.session_state.completed = []

# Function to add a task
def add_task():
    task = st.session_state.task_input
    if task:
        st.session_state.tasks.append(task)
        st.session_state.task_input = ''  # Clear the input field after adding the task

# Title of the app
st.title("To-Do List App")

# Input area for adding tasks
st.text_input("Add a new task:", key="task_input")
st.button("Add Task", on_click=add_task)

# Sidebar filter options
filter_option = st.sidebar.selectbox("Show:", ["All Tasks", "Completed Tasks", "Incomplete Tasks"])

# Displaying tasks based on the selected filter
if filter_option == "All Tasks":
    st.header("All Tasks")
    for i, task in enumerate(st.session_state.tasks):
        is_completed = st.checkbox(task, key=f"task_{i}")
        if is_completed and task not in st.session_state.completed:
            st.session_state.completed.append(task)
elif filter_option == "Completed Tasks":
    st.header("Completed Tasks")
    for task in st.session_state.completed:
        st.write(f"✅ {task}")
else:
    st.header("Incomplete Tasks")
    for task in st.session_state.tasks:
        if task not in st.session_state.completed:
            st.write(f"🔲 {task}")

# Display the total tasks
st.sidebar.write(f"Total tasks: {len(st.session_state.tasks)}")
st.sidebar.write(f"Completed tasks: {len(st.session_state.completed)}")
