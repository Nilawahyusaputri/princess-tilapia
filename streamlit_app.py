import streamlit as st

# Tambahkan CSS untuk memperindah desain
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f7f9fc, #ffffff);
        font-family: 'Arial', sans-serif;
    }
    .header {
        font-size: 2.8rem;
        font-weight: bold;
        color: #3c4a6b;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader {
        font-size: 1.2rem;
        color: #5a5a5a;
        text-align: center;
        margin-bottom: 40px;
    }
    .card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 10px;
        text-align: center;
        font-size: 1.1rem;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        padding: 20px;
    }
    .cta {
        background-color: #3c4a6b;
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 8px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 20px;
        cursor: pointer;
    }
    .cta:hover {
        background-color: #556896;
    }
    .footer {
        font-size: 0.9rem;
        text-align: center;
        color: #7a7a7a;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Fungsi utama aplikasi
def main():
    # Terapkan CSS
    apply_custom_css()
    
    # Header utama
    st.markdown("<div class='header'>Transforming Lives, Restoring Your Health</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>We provide the finest care and amenities for our patients, ensuring their well-being is always our top priority.</div>", unsafe_allow_html=True)
    
    # Bagian kartu layanan
    st.markdown("### 🏥 Our Services")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='card'>General Checkup</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='card'>Eye Surgery</div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='card'>Laser Treatment</div>", unsafe_allow_html=True)
        col4, col5, col6 = st.columns(3)
        with col4:
            st.markdown("<div class='card'>Cataract Consultation</div>", unsafe_allow_html=True)
        with col5:
            st.markdown("<div class='card'>Pediatric Ophthalmology</div>", unsafe_allow_html=True)
        with col6:
            st.markdown("<div class='card'>Glaucoma Detection</div>", unsafe_allow_html=True)
    
    # Statistik kesehatan
    st.markdown("### 📊 Key Statistics")
    st.markdown("""
    <div class="grid-container">
        <div class="card">500+ Successful Surgeries</div>
        <div class="card">99% Patient Satisfaction</div>
        <div class="card">10+ Years of Experience</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Ajakan bertindak
    st.markdown("<div class='cta'>Schedule Your Appointment Today!</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("<div class='footer'>© 2024 Retina Vision Hub. Designed with care for your vision.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

