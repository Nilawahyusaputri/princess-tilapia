elif choice == "Learn About Glaucoma":
    st.markdown("<div class='main-header'>Learn About Glaucoma</div>", unsafe_allow_html=True)

    st.write("""
    Glaucoma is a group of eye diseases that damage the optic nerve, often caused by abnormally high pressure in the eye. 
    Left untreated, glaucoma can lead to irreversible blindness. Here's what you need to know:
    """)

    # Fakta menarik tentang glaukoma
    st.subheader("👁️ Fast Facts About Glaucoma")
    st.write("""
    - **Silent Thief of Sight**: Glaucoma often has no symptoms until significant vision loss occurs.
    - **Global Impact**: Over 70 million people worldwide are affected by glaucoma.
    - **Prevention**: Early detection is key to preventing vision loss.
    - **At Risk**: People over 60, those with a family history of glaucoma, and individuals with diabetes or high blood pressure.
    """)

    # Interaktif: Tes risiko
    st.subheader("🧐 Are You at Risk?")
    st.write("Answer these quick questions to learn about your glaucoma risk:")
    age = st.slider("Your Age", 10, 100, 30)
    family_history = st.selectbox("Do you have a family history of glaucoma?", ["No", "Yes"])
    diabetes = st.selectbox("Do you have diabetes?", ["No", "Yes"])
    high_bp = st.selectbox("Do you have high blood pressure?", ["No", "Yes"])

    if st.button("Check My Risk"):
        risk_score = 0
        if age > 60: risk_score += 2
        if family_history == "Yes": risk_score += 2
        if diabetes == "Yes": risk_score += 1
        if high_bp == "Yes": risk_score += 1

        if risk_score >= 4:
            st.error("High Risk: You should consult an eye specialist immediately.")
        elif risk_score >= 2:
            st.warning("Moderate Risk: Consider scheduling an eye check-up soon.")
        else:
            st.success("Low Risk: Keep up with routine eye check-ups.")

    # Edukasi mendalam
    st.subheader("📚 How to Protect Your Vision")
    st.write("""
    - **Routine Eye Exams**: Early detection through regular check-ups is crucial.
    - **Healthy Lifestyle**: Maintain a balanced diet, exercise regularly, and manage systemic health conditions like diabetes.
    - **Medication Adherence**: If diagnosed, follow prescribed treatments to control eye pressure.
    - **Awareness**: Share knowledge with friends and family about the importance of eye health.
    """)

    # Fakta unik tentang pengobatan dan inovasi teknologi
    st.subheader("🔬 Cutting-Edge Innovations in Glaucoma Care")
    st.write("""
    - **Laser Therapy**: Advanced laser treatments like SLT (Selective Laser Trabeculoplasty) are minimally invasive and effective.
    - **Smart Contact Lenses**: Emerging technology enables real-time monitoring of eye pressure.
    - **AI Diagnosis**: Artificial intelligence assists in early detection by analyzing retinal images with high accuracy.
    - **Gene Therapy**: Research is underway to develop gene-based solutions for hereditary glaucoma.
    """)

    # Inspirasi: Kisah Nyata
    st.subheader("💡 Inspiring Stories")
    st.write("""
    - *"I was diagnosed early, and it saved my vision."* - Maria, 45, a teacher who advocates for regular eye exams.
    - *"Technology gave me hope."* - James, 60, uses smart lenses to monitor his glaucoma daily.
    """)

    # Ajakan bertindak
    st.markdown("""
    <div style='background: #1f4e79; color: white; padding: 15px; text-align: center; border-radius: 10px;'>
    <h3>Protect Your Vision Today!</h3>
    <p>Schedule a comprehensive eye exam and spread the word about glaucoma prevention.</p>
    </div>
    """, unsafe_allow_html=True)
