import google.generativeai as genai
import streamlit as st

st.title("My first chatbot!")
genai.configure(api_key = "AIzaSyAcz_oLvwwsceMy_zheGZREW-VUmN9Y4oU")
model = genai.GenerativeModel("gemini-2.5-pro")

user_prompt = st.text_input("Enter your question or prompt: ")
if st.button("submit"):
    response = model.generate_content(user_prompt)
    st.write(f"AI's response: {response.text}")
