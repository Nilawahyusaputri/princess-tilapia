import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import cv2

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
st.set_page_config(
    page_title="Deteksi Glaukoma",
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Tampilan header
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
        }
        .title {
            text-align: center;
            color: #3A3B3C;
        }
        .subheader {
            text-align: center;
            color: #555555;
            font-size: 18px;
        }
        .footer {
            text-align: center;
            color: #888888;
            margin-top: 30px;
            font-size: 14px;
        }
    </style>
    <h1 class="title">🧿 Web Deteksi Glaukoma</h1>
    <p class="subheader">Unggah gambar retina untuk mendeteksi apakah terdapat indikasi glaukoma.</p>
    """, unsafe_allow_html=True
)

# Memuat model
model = load_model()

# Ukuran gambar input
IMG_SIZE = 224  # Sesuaikan dengan ukuran model Anda

# Input gambar
uploaded_image = st.file_uploader("Unggah Gambar Retina Anda (JPG/PNG)", type=["jpg", "png", "jpeg"])

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
    st.markdown(
        "<h2 style='text-align: center; color: #3A3B3C;'>📊 Hasil Deteksi</h2>", 
        unsafe_allow_html=True
    )
    if prediction[0][0] > 0.5:
        st.markdown(
            f"<h3 style='text-align: center; color: #FF4B4B;'>💡 Positif Glaukoma</h3>"
            f"<p style='text-align: center; color: #3A3B3C;'>Probabilitas: {prediction[0][0] * 100:.2f}%</p>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<h3 style='text-align: center; color: #4CAF50;'>✅ Negatif Glaukoma</h3>"
            f"<p style='text-align: center; color: #3A3B3C;'>Probabilitas: {(1 - prediction[0][0]) * 100:.2f}%</p>",
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    """
    <div class="footer">
        Aplikasi ini menggunakan model machine learning untuk membantu deteksi dini glaukoma. 
        Hasil prediksi tidak menggantikan diagnosis dokter. Silakan konsultasikan hasil ke tenaga medis.
    </div>
    """, unsafe_allow_html=True
)
