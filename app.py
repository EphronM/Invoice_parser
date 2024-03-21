import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
from src.vision import get_gemini_response
from utils.helper import input_image_setup, input_prompt




#   Initialize our streamlit app
st.set_page_config(page_title="Invoice Parser")

st.header("Invoice Extraction 📚")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""  

input=st.text_input("Input Prompt: ",key="input")



submit=st.button("Tell me about the image")
if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)




if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)