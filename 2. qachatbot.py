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
model = genai.GenerativeModel('gemini-pro')

# maintain the history
chat = model.start_chat(history=[])

# define a function to load Gemini pro vision
def get_gemini_response(question):
    # get the respose and stream it
    response = chat.send_message(question, stream=True)
    return response


# Intiate the Streamlit app 
st.set_page_config(page_title="Conversational Q & A Chatbot")

st.header("Conversational Q & A Chatbot")

# initialize the session state for the chat history if it doesn't exist  
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# get the input prompt from user
input=st.text_input("Input Question: ",key="input")

# submit button
submit=st.button("Submit")


## If ask question and submit button is clicked
if submit and input:
    response = get_gemini_response(input)
    # then add user query and response to the session chat history
    st.session_state['chat_history'].append(("You",input))

    # then display the current response
    st.subheader("The response is: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

# finally display the chat history
st.subheader("The Chat History is: ")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")