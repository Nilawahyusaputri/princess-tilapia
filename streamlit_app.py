import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import cv2

st.title('👀 Glaucoma Imaging')

st.write('description ')


# Fungsi untuk memuat model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('model_glaukoma.h5')  # Ganti dengan path model Anda
    return model

# Fungsi untuk memproses gambar
def preprocess_image(image, img_size):
    image = image.resize((img_size, img_size))
    image_array = np.array(image) / 255.0  # Normalisasi
    if len(image_array.shape) == 2:  # Jika grayscale, ubah jadi RGB
        image_array = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)
    elif image_array.shape[-1] == 1:  # Jika channel 1, ubah jadi 3 channel
        image_array = np.repeat(image_array, 3, axis=-1)
    return np.expand_dims(image_array, axis=0)  # Tambahkan dimensi batch

# Fungsi untuk prediksi
def predict_glaucoma(image, model):
    prediction = model.predict(image)
    return prediction

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Deteksi Glaukoma", page_icon="🧿", layout="centered")

st.title("🧿 Web Deteksi Glaukoma dengan Gambar Retina")
st.write("Unggah gambar retina untuk mendeteksi apakah terdapat indikasi glaukoma.")

# Memuat model
model = load_model()

# Ukuran gambar input
IMG_SIZE = 224  # Sesuaikan dengan ukuran model Anda

# Input gambar
uploaded_image = st.file_uploader("Unggah Gambar Retina Anda", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Menampilkan gambar yang diunggah
    image = Image.open(uploaded_image)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    # Preprocessing gambar
    processed_image = preprocess_image(image, IMG_SIZE)

    # Prediksi dengan model
    st.write("⏳ Memproses gambar...")
    prediction = predict_glaucoma(processed_image, model)
    
    # Menampilkan hasil
    st.write("📊 **Hasil Deteksi:**")
    if prediction[0][0] > 0.5:
        st.write("💡 **Positif Glaukoma** dengan probabilitas {:.2f}%.".format(prediction[0][0] * 100))
    else:
        st.write("✅ **Negatif Glaukoma** dengan probabilitas {:.2f}%.".format((1 - prediction[0][0]) * 100))
