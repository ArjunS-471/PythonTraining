import streamlit as st

st.title("User input demo")
#st.title("_Streamlit_is :blue[cool] :sunglasses:")

#st.text("enter the user name: ")
username = st.text_input("Username:")
st.write("Input username is", username)

password = st.text_input("Password:")
st.write("Input username is", password)
