import functions
import streamlit as st

todos = functions._get_list()

def add_task():
    todo = st.session_state['_new_task_'] + '\n'
    todos.append(todo)
    functions._post_list(todos)


st.image('files/banner.jpg')
st.title('Web Todo')
st.subheader('This is a header.')
st.write("This is a simple text")


for todo in todos:
    st.checkbox(todo.title())

st.text_input(label="What you gonna do:",
            placeholder='Add new task...',
            on_change=add_task,
            key='_new_task_')


