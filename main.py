import streamlit as st

#from utils.utils import (
    #upload_image, get_cropped_face,classify_image)

from utils.utils import (
    upload_images
)


def header():
    st.set_page_config(
        page_title="Celebrities classifier",
        layout="wide",
    )

    st.title('Celebrities classifier')
    st.markdown("Pet-project on image classification")
    st.markdown("**Title:** Celebrities classifier with help of SVM")
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

    #model = classify_image()

    if activity == "1":
        image = upload_images()
        st.write(image)
        #if image and st.button("Start classification"):
            #with st.spinner("Processing ..."):
                #get_cropped_face(image, model)

    #elif activity == "2.":
        #photo =


if __name__ == "__main__":
    main()