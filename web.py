import streamlit as st
import functions

#Get the Todo List
todos = functions.get_todos()

#Function to update the Todo List, using session_state data
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#
st.title("Siphiwe's Todo App")
st.subheader("This is my Todo App")

#Format the todo list using checkbox
for todo in todos:
    st.checkbox(todo)


#input
st.text_input(label="", placeholder="Add new todo..", 
              on_change=add_todo, key="new_todo")