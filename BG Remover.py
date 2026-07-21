import streamlit as st
import os
from PIL import Image
from rembg import remove

st.title("Ai Background Remover")

uploaded_file = st.file_uploader("Upload an Image.")

if uploaded_file:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing Background........"):
            result_image = remove(img)

        st.subheader("BackGround Removed..")
        st.image(result_image)
