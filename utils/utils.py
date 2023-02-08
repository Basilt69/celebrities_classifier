import streamlit as st

from streamlit_cropper import st_cropper
from PIL import Image

FILE_TYPES = ["png", "bmp", "jpg", "jpeg"]


def upload_images():
    uploaded_file = st.file_uploader("Choose your photo", accept_multiple_files=False, type=FILE_TYPES)
    realtime_update = st.checkbox(label="Realtime update", value=True)
    aspect_choice = st.radio(label="Выберите Соотношение Сторон:", options=["1:1", "16:9", "4:3", "2:3", "Свободное"])
    aspect_dict = {
        "1:1": (1, 1),
        "16:9": (16, 9),
        "4:3": (4, 3),
        "2:3": (2, 3),
        "Free": None
    }
    box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
    aspect_ratio = aspect_dict[aspect_choice]
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    if uploaded_file:
        img = Image.open(uploaded_file)
        if not realtime_update:
            st.write("Double click to open")
        cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

        st.write("Preview")
        _ = cropped_img.thumbnail((640, 640))
        st.image(cropped_img)


def upload_image():
    user_img = uploader(st.file_uploader("Upload your image:", type=FILE_TYPES))

    return get_image(user_img)


def uploader(file, type="foto"):
    show_file = st.empty()
    if not file:
        show_file.info("allowed file types:" + ",".join(FILE_TYPES))
        return False
    return file


def get_image(user_img):
    img = None
    if user_img is not False:
        img = Image.open(user_img)

    st.image(img, width=600)

    return img










