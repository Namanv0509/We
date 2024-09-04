import json
import os

FILE_PATH = 'todo_list.json'

def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as f:
        json.dump(tasks, f)

def add_task(task, done=False):
    tasks = load_tasks()
    tasks.append({"task": task, "done": done})
    save_tasks(tasks)

def update_task(index, done):
    tasks = load_tasks()
    tasks[index]['done'] = done
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
