import streamlit as st

# Fungsi untuk gaya visual
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e8f0fe, #ffffff); /* Latar warna menarik */
        font-family: 'Arial', sans-serif;
    }
    .header {
        font-size: 3rem; /* Pertebal dan perbesar */
        font-weight: bold;
        color: #1a73e8; /* Warna biru menarik */
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 1.2rem;
        color: #5f6368; /* Abu-abu lembut */
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-section {
        background: #ffffff; /* Kotak putih */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Efek bayangan lembut */
        margin-bottom: 20px;
    }
    .info-box {
        background: #f1f8ff; /* Warna biru lembut */
        border-left: 5px solid #1a73e8; /* Garis biru di sisi kiri */
        border-radius: 10px;
        padding: 15px;
        margin: 20px 0;
        font-size: 1rem;
        color: #1a202c;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #6c757d; /* Warna abu-abu */
        margin-top: 50px;
    }
    .stButton>button {
        background: #1a73e8; /* Tombol warna biru */
        color: white;
        font-size: 1rem;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background: #155cb0; /* Biru lebih gelap saat di-hover */
    }
    .detection-header {
        font-size: 1.5rem; /* Perkecil ukuran */
        font-weight: bold;
        color: #1a73e8;
        text-align: center;
        margin-bottom: 10px;
    }
    .image-container {
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Aplikasi utama
def main():
    # Terapkan CSS
    apply_custom_css()
    
    # Header utama
    st.markdown("<div class='header'>GLAUCOLens</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>See the World Clearly, Detect Glaucoma Early</div>", unsafe_allow_html=True)

    # Simulasi fitur interaktif
    menu = ["Home", "Vision Simulator", "Detection"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.subheader("👁️ About GLAUCOLens")
        st.write("""
        Welcome to the **GLAUCOLens**, a platform dedicated to raising awareness about glaucoma 
        and helping users detect the disease early through image-based analysis.
        
        Why it matters:
        - Glaucoma is a leading cause of irreversible blindness.
        - Early detection can slow down or prevent vision loss.
        
        Explore our features:
        - Vision Simulator: Visualize the impact of glaucoma on vision.
        - Detection: Upload retina images to analyze glaucoma risks.
        """)
        st.image("https://via.placeholder.com/800x400.png?text=GLAUCOLens+-+Protect+Your+Vision", 
                 caption="Join us in preventing glaucoma blindness.", use_column_width=True)

    elif choice == "Vision Simulator":
        st.subheader("🔍 Vision Simulator")
        st.write("Adjust the slider to simulate how glaucoma affects vision.")
        severity = st.slider("Select Glaucoma Severity Level", 0, 100, 25)
        
        st.write("### Simulation Result")
        if severity < 30:
            st.image("https://via.placeholder.com/400x200.png?text=Normal+Vision")
        elif severity < 70:
            st.image("https://via.placeholder.com/400x200.png?text=Mild+Glaucoma")
        else:
            st.image("https://via.placeholder.com/400x200.png?text=Severe+Glaucoma")
        
    elif choice == "Detection":
        # Header deteksi diperbaiki
        st.markdown("<div class='detection-header'>Glaucoma Detection</div>", unsafe_allow_html=True)
        
        # Info box untuk instruksi
        st.markdown("""
        <div class='info-box'>
        Could you upload a picture of the inside of your eye (fundus)? 
        It's the photo that shows the retina and blood vessels.
        </div>
        """, unsafe_allow_html=True)
        
        # Kotak unggah gambar
        st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Fundus Image", type=["jpg", "jpeg", "png"])
        st.markdown("</div>", unsafe_allow_html=True)

        # Placeholder untuk hasil analisis
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Fundus Image", use_column_width=True)
            st.success("Image uploaded successfully! Analysis results will be displayed below.")
        else:
            st.info("Please upload an image to proceed.")

        # Tombol ajakan bertindak
        st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
        if st.button("Analyze Fundus"):
            st.warning("Analysis model integration is in progress. Please check back soon.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>© 2024 GLAUCOLens. Protect Your Vision Today.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
