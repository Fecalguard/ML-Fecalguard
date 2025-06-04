import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# load model VGG16
model = load_model("./model/vgg16_model.h5") # sesuaikan lokesion model

# label output
class_names = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

st.title("⭐Inferensi Sederhana Klasifikasi Penyakit Ayam melalui Citra Feses")

uploaded_file = st.file_uploader("⬇️Unggah Gambar Citra Feses Ternak Ayam Disini⬇️", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            image, 
            caption="Pastikan anda mengunggah gambar feses ternak ayam dengan benar", 
            width=300
        )

    # preprocessing
    image_resized = image.resize((244, 244))
    img_array = img_to_array(image_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # prediksi gambar
    preds = model.predict(img_array)
    label_index = np.argmax(preds)
    confidence = np.max(preds)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("### 🔮 Hasil Prediksi:")
        st.markdown(f"**{class_names[label_index]}**")
        st.markdown("### 🔎 Confidence:")
        st.markdown(f"**{confidence:.4f}**")