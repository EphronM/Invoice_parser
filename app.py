import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
from src.vision import get_gemini_response
from utils.helper import input_image_setup, input_prompt, button_queries




#   Initialize our streamlit app
st.set_page_config(page_title="Invoice Parser")

st.header("Invoice Extraction 📚")

# Function to load the demo invoice
def load_demo_invoice():
    demo_invoice_path = "assets/demo_invoice.jpeg"  # Specify the path to your demo invoice image
    with open(demo_invoice_path, "rb") as file:
        demo_invoice_bytes = file.read()
    return demo_invoice_bytes


# Uploading image file from Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


image=""  

# Add empty space with Markdown
st.markdown("---") 
# Define columns for layout
columns = st.columns(len(button_queries))

# Iterate over button queries and create buttons
for idx, (button_text, query) in enumerate(button_queries.items()):
    button = columns[idx].button(button_text)
    if button:
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, query)
            st.subheader(f"{button_text} Response:")
            st.write(response)
        except FileNotFoundError:
            st.subheader("Invoice not uploaded!!")


# Add empty space with Markdown
st.markdown("---") 

input=st.text_input("Input Prompt: ",key="input")


submit=st.button("Tell me about the image")
if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


# Process the uploaded file
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)