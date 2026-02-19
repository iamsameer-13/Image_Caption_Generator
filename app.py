import streamlit as st
from PIL import Image
from model import generate_caption

st.title("🖼️ Image Caption Generator (BLIP Model)")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=500)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate_caption(image)
        st.success("Caption: " + caption)
