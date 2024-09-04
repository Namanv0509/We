import streamlit as st
from datetime import datetime
import os
from PIL import Image

# Ensure the directory exists for saving uploaded images
if not os.path.exists("uploaded_images"):
    os.makedirs("uploaded_images")

# Predefined images for selection
predefined_images = {
    "None": None,
    "Sun": "assets/1st.png",
    "Moon": "assets/3rd.png",
    "Star": "assets/4th.png",
    # Add paths to your predefined images here
}

# Session state initialization
if 'cards' not in st.session_state:
    st.session_state.cards = []

# Function to save user-uploaded images and resize them
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.resize((50, 50))  # Resize image to 50x50 pixels for profile picture
        save_path = os.path.join("uploaded_images", uploaded_file.name)
        image.save(save_path)
        return save_path
    return None

# Function to add a new card
def add_card(title, description, profile_image=None):
    new_card = {
        "title": title,
        "description": description,
        "profile_image": profile_image,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.cards.insert(0, new_card)  # Add new card at the top

# Title of the app
st.title("Interactive Cards with Profile Pictures")

# Input form for adding a new card
with st.form(key='card_form'):
    title = st.text_input("Card Title")
    description = st.text_area("Card Description")

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

    submit_button = st.form_submit_button(label='Add Card')

# Add card to the session state
if submit_button and title and description:
    add_card(title, description, profile_image)

# Display cards side by side with text vertically arranged
if st.session_state.cards:
    cols = st.columns(3)
    for i, card in enumerate(st.session_state.cards):
        profile_img_tag = f"<img src='{card['profile_image']}' style='width:50px; height:50px; border-radius:50%; margin-bottom:10px;' />" if card['profile_image'] else ""
        st.markdown(
            f"""
            <div style="
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 10px;
            ">
                {profile_img_tag}
                <h3 style="margin-bottom: 5px;">{card['title']}</h3>
                <p style="margin-top: 5px;">{card['description'].replace('\n', '<br>')}</p>
                <p style="font-size: 0.8em; color: gray;"><strong>Date:</strong> {card['date']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
