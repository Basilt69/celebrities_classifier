import streamlit as st


def upload_images():
    uploaded_file = st.file_uploader("Choose your photo", accept_multiple_files=False)
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)








