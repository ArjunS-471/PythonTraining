import streamlit as st

st.title("Calculator Demo")
#st.title("_Streamlit_is :blue[cool] :sunglasses:")

numa = 0
numb = 0

operation = ''

option = st.selectbox(
    "Select your numerical operation",
    ("Add", "Subtract", "Multiply", "Divide"),
)

st.write("You selected:", option)

#st.text("enter the user name: ")
numa = st.text_input("Number A:")
st.write("1st number is", numa)

numb = st.text_input("Number B:")
st.write("2nd number is", numb)

if(option == "Add"):
    result = int(numa) + int(numb)
    st.text(result)

if(option == "Subtract"):
    result = int(numa) - int(numb)
    st.text(result)

if(option == "Multiply"):
    result = int(numa) * int(numb)
    st.text(result)

if(option == "Divide"):
    result = int(numa) / int(numb)
    st.text(result)