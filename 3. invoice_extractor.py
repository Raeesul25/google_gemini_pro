from dotenv import load_dotenv

# load the all environment variables from .env files
load_dotenv()

# import neccessary libraries 
import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai 

# configure API keys
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load the model 
model = genai.GenerativeModel('gemini-pro-vision')

# define a function to load Gemini pro vision
def get_gemini_response(input, image, prompt):
    # input: what gemini want to do 
    # prompt: what message i want 
    response = model.generate_content([input, image[0], prompt])
    return response.text

# define a function to do image processing
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Intiate the Streamlit app 
st.set_page_config(page_title="Multi Language Invoice Extractor")

st.header("Multi Language Invoice Extractor")
# image uploder
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# visual uploaded image
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# get the input prompt from user
input=st.text_input("Input Prompt: ",key="input")

# submit button
submit=st.button("Tell me about the image")

input_prompt = """
    You are an expert in understanding invoices.
    You will receive input images as invoices & you will have to answer questions based on the input image
"""

## If ask button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)