import streamlit as st
import os
from PIL import Image

def display_images_with_lines(image_folder):
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    row_index = 0
    col_index = 0

    st.markdown(
        """
        <style>
        .image-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .image-container {
            position: relative;
            width: 30%;
        }
        .image-container img {
            width: 100%;
            border: 2px solid #ddd;
            border-radius: 8px;
        }
        .image-container svg {
            position: absolute;
            top: 50%;
            left: 100%;
            transform: translateY(-50%);
            width: 40px;
            height: 40px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for i in range(0, len(image_files), 3):
        row_images = image_files[i:i + 3]
        st.markdown('<div class="image-row">', unsafe_allow_html=True)
        for idx, img_path in enumerate(row_images):
            img = Image.open(img_path)
            with st.container():
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(img, use_column_width=True)
                if idx < len(row_images) - 1:
                    st.markdown(
                        """
                        <svg viewBox="0 0 100 100">
                            <path d="M 0,50 Q 50,0 100,50 T 200,50" stroke="white" fill="transparent" />
                        </svg>
                        """,
                        unsafe_allow_html=True
                    )
                st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Folder containing the images
image_folder = "assets/Dashboard"

# Display images with lines connecting them
display_images_with_lines(image_folder)
