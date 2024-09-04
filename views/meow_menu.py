import streamlit as st
import json_file_storage as storage


# Load tasks from JSON file
tasks = storage.load_tasks()

st.title("Meowneu👨‍🍳👩‍🍳")

# Input to add a new task
new_task = st.text_input("Add a new task")

# Button to add the task
if st.button("Bhogu Appender"):
    if new_task:
        storage.add_task(new_task)
        st.success(f"Yummy '{new_task}' added!")
        tasks = storage.load_tasks()  # Reload tasks after adding
    else:
        st.warning("You Ordering Empty Plate or What💀.")

st.write("---")

# Sort tasks so that incomplete tasks come first
sorted_tasks = sorted(tasks, key=lambda x: x['done'])

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
            storage.update_task(sorted_tasks.index(task), not is_done)
            tasks = storage.load_tasks()  # Reload tasks after updating

        # Display task with a strikethrough if done
        if is_done:
            st.write(f"~~{task_desc}~~")
        else:
            st.write(task_desc)

        # Button to delete the task
        if st.button("Oppsies", key=f"delete_{idx}"):
            tasks_to_remove.append(sorted_tasks.index(task))

    # Remove tasks after iterating
    if tasks_to_remove:
        for idx in reversed(tasks_to_remove):
            storage.delete_task(idx)
            tasks = storage.load_tasks()  # Reload tasks after deleting
else:
    st.write("Menu is empty!?!?!?!")
