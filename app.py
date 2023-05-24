import os
import streamlit as st
from langchain.llms import OpenAI

# App
st.title("Youtube GPT Creator")
promt = st.text_input("Plug in your promt here")

# Llms - Get predictions from a language model
# High temperature means the model will take
# more risks i.e. output more random
llm = OpenAI(temperature=0.9)

# Show response
if promt:
    response = llm(promt)
    st.write(response)
