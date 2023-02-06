import streamlit as st

from utils.utils import (
    load_model, upload_image
)


def header():
    st.set_page_config(
        oage_title="Celebrities classifier",
        layput="wide",
    )

    st.title('Celebrities classifier')
    st.markdown("Pet-project on image classification")
    st.markdown("**Title:**Celebrities classifier with help of SVM")
    st.markdown("Prepared by Basil Tkachenko")

    st.sidebar.markdown("[prject repo](https://github.com/Basilt69/celebrities_classifier)")


def main():
    header()

    st.header("Celebrities classifier")
    activity = st.radio(
        "Please, choose your action:", (
            "1. Upload image.",
            "2. Photo"
        ),
        index=0
    )[:1]

    model = load_model()

    if activity == "1":
        image = upload_image()
        if image and st.button("Start classification"):
            with st.spinner("Processing ..."):
                get_cropped_face(image, model)

    elif activity == "2.":
        photo =
