import streamlit as st
import requests

st.title("View API Results")

url = st.text_input("Input API URL:", "")

if st.button("Send a GET request"):
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()  
            
            try:
                result = response.json()
                st.success("Request Success!")
                st.json(result)  
            except ValueError:
                st.warning("Cannot process JSON data")
                st.text(response.text)  

        except requests.exceptions.RequestException as e:
            st.error(f"Request Failure: {e}")
    else:
        st.warning("Enter URL!")
