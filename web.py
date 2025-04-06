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


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions._post_list(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="What you gonna do:",
            placeholder='Add new task...',
            on_change=add_task,
            key='_new_task_')


# debug
st.session_state
