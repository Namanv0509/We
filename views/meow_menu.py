import streamlit as st

# Initialize session state for the to-do list
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

st.title("Meowneu👨‍🍳👩‍🍳")

# Input to add a new task
new_task = st.text_input("Add a new task")

# Button to add the task
if st.button("Bhogu Appender"):
    if new_task:
        st.session_state.todo_list.append({"task": new_task, "done": False})
        st.success(f"Yummy '{new_task}' added!")
    else:
        st.warning("You Ordering Empty Plate or What💀.")

st.write("---")

# Sort tasks so that incomplete tasks come first
sorted_tasks = sorted(st.session_state.todo_list, key=lambda x: x['done'])

# Display current tasks
st.subheader("👉👈Our List")

if sorted_tasks:
    tasks_to_remove = []

    for idx, task in enumerate(sorted_tasks):
        task_desc = task["task"]
        is_done = task["done"]

        # Checkbox to mark task as done/undone
        checkbox_label = "Done" if not is_done else "Once More"
        if st.checkbox(checkbox_label, key=f"done_{idx}"):
            st.session_state.todo_list[idx]["done"] = not is_done

        # Display task with a strikethrough if done
        if is_done:
            st.write(f"~~{task_desc}~~")
        else:
            st.write(task_desc)

        # Button to delete the task
        if st.button("Oppsies", key=f"delete_{idx}"):
            tasks_to_remove.append(idx)

    # Remove tasks after iterating
    if tasks_to_remove:
        for idx in reversed(tasks_to_remove):
            del st.session_state.todo_list[idx]
else:
    st.write("Menu is empty!?!?!?!")
