from dotenv import load_dotenv

# load the all environment variables from .env files
load_dotenv()

# import neccessary libraries 
import streamlit as st 
import os 
import google.generativeai as genai 

# configure API keys
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load the model for chatbot
model = genai.GenerativeModel('gemini-pro')

# define a function to load Gemini pro vision
def get_gemini_response(question):
    # get the respose and stream it
    response = model.generate_content(question)
    return response.text


# Intiate the Streamlit app 
st.set_page_config(page_title="LLM Application - Gemini Pro")

st.header("LLM Application - Gemini Pro")

# get the input prompt from user
input=st.text_input("Input Question: ",key="input")

# submit button
submit=st.button("Submit")


## whn submit button is clicked
if submit and input:
    response = get_gemini_response(input)
    
    # then display the current response
    st.subheader("The response is: ")
    st.write(response)
        