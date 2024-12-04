import requests
import streamlit as st

st.title("Weather Info")
#st.title("_Streamlit_is :blue[cool] :sunglasses:")

#st.text("enter the user name: ")
latitude = st.text_input("Latitude:")
st.write("Input username is", latitude)

longitude = st.text_input("Longitude:")
st.write("Input username is", longitude)


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude" : latitude,
    "longitude" : longitude,
    "current_weather" : "true"
}

response = requests.get(url, params)
print(response)
print(response.json()['current_weather'])

st.text(response.json()['current_weather']['temperature'])