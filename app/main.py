import os
import json
from PIL import Image

import numpy as np
import tensorflow as tf
import keras
import streamlit as st

from keras.applications.resnet50 import preprocess_input

# Reduce TensorFlow logging
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

st.set_page_config(
    page_title="Plant Disease Classifier",
    page_icon="🌿",
    layout="centered"
)

# =========================
# Paths
# =========================

working_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    working_dir, "trained_model", "plant_disease_prediction_model2.h5"
)

class_indices_path = os.path.join(
    working_dir, "class_indices.json"
)

# =========================
# Load Model (Cached)
# =========================

@st.cache_resource
def load_model():
    model = keras.models.load_model(model_path, compile=False)
    return model

model = load_model()

# =========================
# Load Class Labels (Cached)
# =========================

@st.cache_resource
def load_class_labels():

    with open(class_indices_path) as f:
        class_indices = json.load(f)

    if isinstance(list(class_indices.values())[0], int):
        return {v: k for k, v in class_indices.items()}
    else:
        return {int(k): v for k, v in class_indices.items()}

class_labels = load_class_labels()

# =========================
# Image Preprocessing
# =========================

@st.cache_data
def load_and_preprocess_image(image_bytes, target_size=(224, 224)):

    img = Image.open(image_bytes).convert("RGB")
    img = img.resize(target_size)

    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    img_array = preprocess_input(img_array)

    return img_array

# =========================
# Prediction
# =========================

def predict_image_class(model, image_file):

    processed_img = load_and_preprocess_image(image_file)

    predictions = model.predict(processed_img)

    predicted_index = int(np.argmax(predictions))

    predicted_class = class_labels[predicted_index]

    confidence = float(np.max(predictions)) * 100

    return predicted_class, confidence

# =========================
# Streamlit UI
# =========================

st.title("🌿 Plant Disease Classifier")

st.write("Upload a plant leaf image to detect plant disease.")

uploaded_image = st.file_uploader(
    "Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    image = Image.open(uploaded_image)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image")

    with col2:

        if st.button("Classify"):

            predicted_class, confidence = predict_image_class(model, uploaded_image)

            formatted_name = predicted_class.replace("___", " - ").replace("_", " ")

            st.success(f"Prediction: {formatted_name}")

            st.info(f"Confidence: {confidence:.2f}%")