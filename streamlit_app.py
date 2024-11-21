import streamlit as st

# Terapkan tema warna dan CSS untuk tampilan yang menarik
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background: #f0f4f8;  /* Warna latar belakang lembut */
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f4e79; /* Warna biru tua */
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 1.2rem;
        color: #495057; /* Warna abu-abu tua */
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-section {
        background: #ffffff;  /* Background putih untuk kotak unggah */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Efek bayangan lembut */
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #6c757d; /* Warna abu-abu */
        margin-top: 50px;
    }
    .stButton>button {
        background: #1f4e79; /* Tombol warna biru tua */
        color: white;
        font-size: 1rem;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background: #145374; /* Biru lebih gelap saat di-hover */
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Terapkan CSS
    apply_custom_css()

    # Header aplikasi
    st.markdown("<div class='main-header'>Retina Vision Detection</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Upload your retina image to analyze glaucoma risks</div>", unsafe_allow_html=True)
    
    # Kotak unggah gambar
    st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Retina Image", type=["jpg", "jpeg", "png"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Placeholder untuk hasil analisis
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Retina Image", use_column_width=True)
        st.success("Image uploaded successfully! Analysis results will be displayed here.")
    else:
        st.info("Please upload an image to proceed.")

    # Tombol ajakan bertindak
    st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
    if st.button("Analyze Retina"):
        st.warning("Model not integrated yet. Please wait for updates.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>© 2024 Retina Vision Hub. All rights reserved.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
