
# To-Do List App in Streamlit

## Overview

A To-Do List App is an excellent project to practice working with user input, dynamic interaction, and state management in Streamlit. This app will allow users to:

- Add new tasks.
- View a list of tasks.
- Mark tasks as completed, with a visual distinction for completed tasks.
- Use a sidebar to filter between all tasks, completed tasks, and incomplete tasks.

## App Features

### Task Input

Users can input a task using a text box and click a button to add it to the to-do list.

### Task Display

Tasks will be displayed on the main screen. Completed tasks will be visually distinguished from incomplete ones.

### Task Completion

Users can mark tasks as completed by clicking checkboxes.

### Sidebar Filter

The app will include a sidebar with options to filter between:

- All tasks
- Completed tasks
- Incomplete tasks

## Steps to Build the App

1. **Import Libraries**:
    - Use Streamlit for creating the web app.
    - Optionally, use `streamlit.session_state` to keep track of tasks and their states during user interaction.

2. **State Management**:
    - Use `streamlit.session_state` to dynamically store and manage tasks. This ensures that tasks persist and can be manipulated during the session.

3. **Input for New Tasks**:
    - Provide a text input field where users can enter new tasks.
    - Include an "Add Task" button that adds the input task to the to-do list.

4. **Display Tasks**:
    - Show all tasks in a list on the main screen.
    - Add checkboxes next to each task to allow users to mark tasks as completed.
    - Visually separate completed tasks from incomplete ones.

5. **Sidebar for Filtering Tasks**:
    - Add a sidebar with options to filter the task view:
      - "All Tasks": Shows all tasks regardless of completion status.
      - "Completed Tasks": Displays only tasks that have been marked as completed.
      - "Incomplete Tasks": Shows tasks that are still pending.