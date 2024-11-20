import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2

# Load pre-trained model (pastikan model Anda sudah ada di folder)
model = load_model("path_to_your_model.h5")

# Function to preprocess image
def preprocess_image(image):
    # Convert the image to grayscale (as an example)
    image = image.convert("RGB")
    image = image.resize((224, 224))  # Resize to the expected size for the model
    image = np.array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize the image
    return image

# Function to make prediction
def predict(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Predict using the model
    prediction = model.predict(processed_image)
    
    # Assuming a binary classification for glaucoma (1 = Glaucoma, 0 = Normal)
    return prediction[0][0]  # Return the probability of having glaucoma

# Streamlit UI
st.title("Glaucoma Detection System")
st.write("Upload an image of the retina to detect glaucoma.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    
    # Show the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")
    
    # Make prediction
    prediction = predict(image)
    
    # Display results
    if prediction > 0.5:
        st.subheader("Result: Glaucoma Detected")
        st.write(f"Confidence: {prediction*100:.2f}%")
    else:
        st.subheader("Result: No Glaucoma")
        st.write(f"Confidence: {(1 - prediction)*100:.2f}%")
    
    # Additional output (optional)
    st.write("This result is based on the analysis of the retina image.")
