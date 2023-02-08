import streamlit as st

#from utils.utils import (
    #upload_image, get_cropped_face,classify_image)

from utils.utils import (
    upload_images,
    upload_image,
    start_classification,
    load_model
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

    st.sidebar.markdown("[project repo](https://github.com/Basilt69/celebrities_classifier)")


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
        #image = upload_images()
        image = upload_image()
        if image:
            probability = start_classification(image, model, static=True)
            st.write(probability)


        #if image and st.button("Start classification"):
            #with st.spinner("Processing ..."):
                #get_cropped_face(image, model)

    #elif activity == "2.":
        #photo =


if __name__ == "__main__":
    main()