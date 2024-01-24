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

# load the model for chatbot
model = genai.GenerativeModel('gemini-pro-vision')

# define a function to load Gemini pro vision
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    
    return response.text


# Intiate the Streamlit app 
st.set_page_config(page_title="LLM Application - Gemini Pro")

st.header("LLM Application - Gemini Pro")

# image uploder
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# visual uploaded image
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# get the input prompt from user
input=st.text_input("Input: ",key="input")

# submit button
submit=st.button("Submit")

## when submit button is clicked
if submit:
    response = get_gemini_response(input, image)
    
    # then display the current response
    st.subheader("The response is: ")
    st.write(response)
        