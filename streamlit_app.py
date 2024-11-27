import streamlit as st

# Fungsi untuk gaya visual
def apply_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');
    body {
        background: linear-gradient(135deg, #f9f7f7, #dbe2ef);
        font-family: 'Raleway', sans-serif;
    }
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #112d4e;
        text-align: center;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 1.3rem;
        color: #3f72af;
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-section {
        background: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .info-box {
        background: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.1);
        font-size: 1rem;
        color: #495057;
        text-align: center;
        margin: 20px 0;
    }
    .detection-header {
        font-size: 1.8rem; /* Perkecil ukuran */
        font-weight: bold;
        color: #112d4e;
        text-align: center;
        margin-bottom: 10px;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #6c757d;
        margin-top: 50px;
    }
    .stButton>button {
        background: #3f72af;
        color: white;
        font-size: 1rem;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background: #2b6ca3;
    }
    </style>
    """, unsafe_allow_html=True)

# Aplikasi utama
def main():
    # Terapkan CSS
    apply_custom_css()
    
    # Header utama
    st.markdown("<div class='main-header'>GLAUCOLens</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>See the World Clearly, Detect Glaucoma Early</div>", unsafe_allow_html=True)

    # Menu navigasi
    menu = ["Home", "Vision Simulator", "Detection"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.subheader("👁️ About GLAUCOLens")
        st.write("""
        Welcome to **GLAUCOLens**, your trusted platform for early detection of glaucoma. 
        Our mission is to empower individuals to take proactive steps in preserving their vision through advanced technology.
        
        **Why choose GLAUCOLens?**
        - **Easy-to-use platform**: Upload retina images and get results in minutes.
        - **Awareness tools**: Visualize how glaucoma affects vision using our Vision Simulator.
        - **Scientific accuracy**: Built on cutting-edge medical imaging and machine learning.
        
        Glaucoma is one of the leading causes of irreversible blindness, but early detection can save your vision. Let’s take action together to protect your eyes.
        """)
        st.image("https://via.placeholder.com/800x400.png?text=GLAUCOLens+-+Protect+Your+Vision", 
                 caption="Join GLAUCOLens in preserving vision for a lifetime.", use_column_width=True)

    elif choice == "Vision Simulator":
        st.subheader("🔍 Vision Simulator")
        st.write("Adjust the slider to simulate how glaucoma affects vision.")

        # Slider untuk menentukan tingkat keparahan glaucoma
        severity = st.slider("Select Glaucoma Severity Level", 0, 100, 25)

        # Tampilan simulasi berdasarkan tingkat keparahan
        st.write("### Simulation Result")
        if severity < 30:
            st.image("https://via.placeholder.com/400x300.png?text=Normal+Vision", 
                     caption="Normal Vision (No Glaucoma)", use_column_width=True)
        elif severity < 70:
            st.image("https://via.placeholder.com/400x300.png?text=Mild+Glaucoma", 
                     caption="Mild Glaucoma", use_column_width=True)
        else:
            st.image("https://via.placeholder.com/400x300.png?text=Severe+Glaucoma", 
                     caption="Severe Glaucoma", use_column_width=True)

        st.write("""
        **Explanation:**
        - Normal Vision: Clear, with no signs of damage.
        - Mild Glaucoma: Partial peripheral vision loss.
        - Severe Glaucoma: Significant vision impairment in the central and peripheral fields.
        """)

    elif choice == "Detection":
        # Perkecil header
        st.markdown("<div class='detection-header'>Glaucoma Detection</div>", unsafe_allow_html=True)
        
        # Teks informasi dalam kotak putih
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
    st.markdown("<div class='footer'>© 2024 GLAUCOLens. Let’s Protect Your Vision Together.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
