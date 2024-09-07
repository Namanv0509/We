import streamlit as st
from datetime import datetime
import os
import json
from PIL import Image

# File paths
poems_json_file = "saved_poems.json"
uploaded_images_folder = "uploaded_images"

# Ensure the directory exists for saving uploaded images
if not os.path.exists(uploaded_images_folder):
    os.makedirs(uploaded_images_folder)

# Predefined images for selection
predefined_images = {
    "None": None,
    "Sun": "assets/1st.png",
    "Moon": "assets/3rd.png",
    "Star": "assets/4th.png",
    # Add paths to your predefined images here
}

# Load poems from the JSON file
def load_poems():
    if os.path.exists(poems_json_file):
        with open(poems_json_file, 'r') as f:
            return json.load(f)
    return []

# Save poems to the JSON file
def save_poems(poems):
    with open(poems_json_file, 'w') as f:
        json.dump(poems, f, indent=4)

# Function to save user-uploaded images and resize them
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.resize((50, 50))  # Resize image to 50x50 pixels for profile picture
        save_path = os.path.join(uploaded_images_folder, uploaded_file.name)
        image.save(save_path)
        return save_path
    return None

# Function to add a new poem
def add_poem(title, poem_text, profile_image=None):
    new_poem = {
        "title": title,
        "poem": poem_text,
        "profile_image": profile_image,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.poems.insert(0, new_poem)  # Add new poem at the top
    save_poems(st.session_state.poems)  # Save the updated poems list to JSON

# Initialize session state
if 'poems' not in st.session_state:
    st.session_state.poems = load_poems()  # Load poems from JSON file at the start

# Title of the app
st.title("Poetry Corner")

# Input form for adding a new poem
with st.form(key='poem_form'):
    title = st.text_input("Poem Title")
    poem_text = st.text_area("Your Poem")

    # Dropdown to select a predefined profile picture
    selected_image = st.selectbox("Select a Profile Picture", options=list(predefined_images.keys()))

    # Option to upload a profile picture
    profile_file = st.file_uploader("Or Upload Your Profile Picture (Optional)", type=["png", "jpg", "jpeg"])
    profile_image = None

    # Determine which profile image to use
    if profile_file is not None:
        profile_image = save_uploaded_file(profile_file)
    elif predefined_images[selected_image] is not None:
        profile_image = predefined_images[selected_image]

    submit_button = st.form_submit_button(label='Add Poem')

# Add poem to the session state and save to JSON
if submit_button and title and poem_text:
    add_poem(title, poem_text, profile_image)
    st.success(f"Poem '{title}' has been added and saved!")

# Display poems side by side with text vertically arranged
if st.session_state.poems:
    # Display poems side by side
    cols = st.columns(3)  # Three columns for arrangement
    for i, poem in enumerate(st.session_state.poems):
        # Create the profile image HTML tag if an image exists
        profile_img_tag = (
            f"<img src='{poem['profile_image']}' style='width:50px; height:50px; border-radius:50%; margin-bottom:10px;' />"
            if poem['profile_image'] else ""
        )
        
        # Create the HTML block for the poem card
        poem_card = f"""
        <div style="
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 10px;
        ">
            {profile_img_tag}
            <h3 style="margin-bottom: 5px;">{poem['title']}</h3>
            <p style="margin-top: 5px;">{poem['poem'].replace('\n', '<br>')}</p>
            <p style="font-size: 0.8em; color: gray;">
                <strong>Date:</strong> {poem['date']}
            </p>
        </div>
        """

        
        cols[i % 3].markdown(poem_card, unsafe_allow_html=True)