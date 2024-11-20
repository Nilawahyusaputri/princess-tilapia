import streamlit as st
from PIL import Image

# Streamlit UI
st.title("Glaucoma Detection System")
st.write("Upload an image of the retina to check for glaucoma.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Show the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")
    
    # You can add some other information here, for example:
    st.subheader("What is Glaucoma?")
    st.write("""
        Glaucoma is a group of eye diseases that can damage the optic nerve and lead to vision loss or blindness. 
        It is often associated with increased pressure in the eye. Early detection through retina imaging can help in managing the disease.
    """)
    
    # Instructions or next steps
    st.subheader("Next Steps")
    st.write("""
        If you suspect you have glaucoma, please consult a healthcare professional for further diagnosis and treatment options.
    """)
