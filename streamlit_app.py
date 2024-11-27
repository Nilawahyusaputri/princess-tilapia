import streamlit as st
from PIL import Image, ImageEnhance, ImageDraw, ImageFilter

# Fungsi untuk gaya visual
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background: #f0f4f8; /* Warna latar belakang lembut */
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        font-size: 3rem;
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

# Fungsi untuk menghasilkan simulasi glaucoma
def generate_glaucoma_simulation(image, severity):
    if severity == 0:
        return image  # Gambar asli tanpa efek
    else:
        # Terapkan blur sesuai tingkat keparahan
        blur_amount = severity / 10  # Skala blur
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_amount))

        # Tambahkan efek lingkaran gelap di tepi untuk simulasi glaucoma
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        width, height = image.size
        center = (width // 2, height // 2)
        max_radius = min(center)

        for i in range(severity):
            draw.ellipse(
                [center[0] - max_radius + i * 5, center[1] - max_radius + i * 5, 
                 center[0] + max_radius - i * 5, center[1] + max_radius - i * 5],
                outline=(0, 0, 0, int(5 * (100 - severity))),
                width=5
            )

        final_image = Image.alpha_composite(blurred_image.convert("RGBA"), overlay)
        return final_image.convert("RGB")

# Aplikasi utama
def main():
    # Terapkan CSS
    apply_custom_css()
    
    # Header utama
    st.markdown("<div class='main-header'>GLAUCOLens</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>See the World Clearly, Detect Glaucoma Early</div>", unsafe_allow_html=True)

    # Menu
    menu = ["Home", "Vision Simulator", "Detection"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.subheader("👁️👁️ About GLAUCOLens")
        st.write("""
        Welcome to **GLAUCOLens**, a platform dedicated to raising awareness about glaucoma 
        and helping users detect the disease early through image-based analysis.
        
        Why it matters:
        - Glaucoma is a leading cause of irreversible blindness.
        - Early detection can slow down or prevent vision loss.
        
        Explore our features:
        - Vision Simulator: Visualize the impact of glaucoma on vision.
        - Detection: Upload retina images to analyze glaucoma risks.
        """)
        st.image("https://via.placeholder.com/800x400.png?text=Glaucoma+Detection", 
                 caption="Join us in preventing glaucoma blindness.", use_column_width=True)

    elif choice == "Vision Simulator":
        st.subheader("🔍 Vision Simulator")
        st.write("Adjust the slider to simulate how glaucoma affects vision.")
        severity = st.slider("Select Glaucoma Severity Level", 0, 100, 25)
        
        # Load dan tampilkan gambar
        default_image = Image.open("vision_sample.jpg")  # Gambar contoh
        simulated_image = generate_glaucoma_simulation(default_image, severity)
        
        st.write("### Simulation Result")
        st.image(simulated_image, caption=f"Glaucoma Severity Level: {severity}%", use_column_width=True)

    elif choice == "Detection":
        st.markdown("<div class='main-header' style='font-size: 1.5rem;'>Glaucoma Detection</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='info-box'>
        Could you upload a picture of the inside of your eye (fundus)? 
        It's the photo that shows the retina and blood vessels.
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Upload Fundus Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Fundus Image", use_column_width=True)
            st.success("Image uploaded successfully! Analysis results will be displayed below.")
        else:
            st.info("Please upload an image to proceed.")

        if st.button("Analyze Fundus"):
            st.warning("Analysis model integration is in progress. Please check back soon.")

    st.markdown("<div class='footer'>© 2024 GLAUCOLens. Protect Your Vision Today.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
