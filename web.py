import streamlit as st
import functions

todos = functions.get_todos()

st.title("Siphiwe's Todo App")
st.subheader("This is my Todo App")


for todo in todos:
    st.checkbox(todo)


#input
st.text_input(label="", placeholder="Add new todo..")