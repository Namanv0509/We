import sqlite3
import streamlit as st

# Function to create a SQLite database and table if it doesn't exist
def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new note to the database
def add_note(content):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (contepip install nt) VALUES (?)", (content,))
    conn.commit()
    conn.close()

# Function to retrieve all notes from the database
def get_notes():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT content FROM notes")
    notes = c.fetchall()
    conn.close()
    return [note[0] for note in notes]

# Initialize the database
init_db()

# Streamlit UI
def show_contact_form():
    user_input = st.text_input("Enter your note:")
    if st.button("MailMan🧙‍♂️"):
        if user_input:
            add_note(user_input)
            st.success("Yayyyyy!")
        else:
            st.warning("Saving the void ????(ノへ￣、)")

    st.write("### Your Notes:")
    notes = get_notes()
    for note in notes:
        st.write(f"- {note}")

# -- Hero Section --
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("assets/Wafflers .jpg", width=230)
with col2:
    st.title("Meow Meow")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    if st.button("💟 Talk To Me"):
        show_contact_form()
