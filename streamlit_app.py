import streamlit as st
from datetime import date

# Fungsi untuk gaya visual
def apply_custom_css():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #c9d6ff, #e2e2e2); /* Warna biru lembut */
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #f0f4f8; /* Warna abu-abu terang */
    }
    .header {
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
        margin-bottom: 20px;
    }
    .button-div {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .image-container {
        text-align: center;
        margin-top: 20px;
    }
    .stButton>button {
        background: #1f4e79; /* Warna biru tua */
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

# Aplikasi utama
def main():
    # Terapkan CSS
    apply_custom_css()
    
    # Header utama
    st.markdown("<div class='header'>Welcome to Retina Vision Hub 🌟</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Explore, Learn, and Protect Your Vision</div>", unsafe_allow_html=True)

    # Simulasi fitur interaktif
    menu = ["Home", "Vision Simulator", "Eye Health Quiz", "Schedule Checkup"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.subheader("✨ About This App ✨")
        st.write("""
        Welcome to Retina Vision Hub! This interactive platform is designed to raise awareness about glaucoma and eye health.
        Explore our features:
        - Vision Simulator: Experience what glaucoma looks like.
        - Eye Health Quiz: Test your knowledge about eye health.
        - Schedule Checkup: Plan your next visit to an eye specialist.
        """)
        st.write("💡 Stay curious and protect your vision!")

        # Gambar Placeholder untuk galeri retina
        st.image("https://via.placeholder.com/800x400.png?text=Retina+Art+Gallery", 
                 caption="Explore the Retina Art Gallery", use_column_width=True)

    elif choice == "Vision Simulator":
        st.subheader("🔍 Vision Simulator")
        st.write("Adjust the slider to simulate the effects of glaucoma on vision.")
        severity = st.slider("Select Glaucoma Severity", 0, 100, 25)
        
        st.write("### Simulation Result")
        if severity < 30:
            st.image("https://via.placeholder.com/400x200.png?text=Normal+Vision")
        elif severity < 70:
            st.image("https://via.placeholder.com/400x200.png?text=Mild+Glaucoma")
        else:
            st.image("https://via.placeholder.com/400x200.png?text=Severe+Glaucoma")
        
    elif choice == "Eye Health Quiz":
        st.subheader("🎯 Eye Health Quiz")
        st.write("Test your knowledge about eye health and learn more!")

        question = "Is glaucoma curable?"
        options = ["Yes", "No"]
        answer = st.radio("Q1: " + question, options)

        if answer:
            if answer == "No":
                st.success("Correct! Glaucoma can be managed but not cured.")
            else:
                st.error("Incorrect! Glaucoma can't be cured, but early detection helps in management.")

    elif choice == "Schedule Checkup":
        st.subheader("📅 Schedule Your Checkup")
        name = st.text_input("Enter Your Name")
        age = st.slider("Select Your Age", 0, 100, 25)
        date_selected = st.date_input("Select a Date for Your Checkup", date.today())
        
        if st.button("Schedule Appointment"):
            st.success(f"Appointment scheduled for {name} on {date_selected}.")
    
    # Footer aplikasi
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #6c757d; font-size: 0.9rem;'>
    © 2024 Retina Vision Hub. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
