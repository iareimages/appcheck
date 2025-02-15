import streamlit as st
import face_recognition
from PIL import Image
import numpy as np

st.title("Face Recognition App")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    image_array = np.array(image)

    # Detect faces
    face_locations = face_recognition.face_locations(image_array)
    st.write(f"Number of faces detected: {len(face_locations)}")

    # Display the image with face locations
    for top, right, bottom, left in face_locations:
        st.image(image_array[top:bottom, left:right], caption="Detected Face")