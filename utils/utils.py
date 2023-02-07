import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests, jsonify, joblib, json

import glob
import pafy
import cv2
import os
import base64

from PIL import Image, UnidentifiedImageError

import pywt


FILE_TYPES = ["png", "bmp", "jpg", "jpeg"]

__class_name_to_number = {}
__class_number_to_name = {}

__model = None


def uploader(file, type_="foto"):
    show_file = st.empty()
    if not file:
        show_file.info("possible extensions:" + ",".join(FILE_TYPES))
        return False
    return file


def get_image(user_img):
    img=None
    if user_img is not False:
        try:
            img = Image.open(user_img)
        except UnidentifiedImageError:
            st.error("Uppss...Something went wrong...")
            st.stop()

    st.image(img, width=600)

    return img


def upload_image():
    user_img = uploader(st.file_uploader("Please, upload your file.", type=FILE_TYPES))

    return get_image(user_img)


def get_cropped_face(image):
    face_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_eye.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped_faces = []

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    return cropped_faces


def classify_image(image):

    imgs = get_cropped_face(image)

    result = []
    for img in imgs:
        scalled_raw_img = cv2.resize(img, (32,32))
        img_har = pywt.w2d(img, 'db1', 5)
        scalled_img_har = cv2.resize(img_har, (32,32))
        combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1), scalled_img_har.reshape(32*32,1)))

        len_image_array = 32*32*3 + 32*32

        final = combined_img.reshape(1, len_image_array).astype(float)

        result.append({
            'class': class_number_to_name(__model.predict(final)[0]),
            'class_probability': np.around(__model.predict_proba(final)*100,2).tolist()[0],
            'class_dictionary': __class_name_to_number
        })

    return result

def class_number_to_name(class_num):
    return __class_number_to_name[class_num]


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __class_name_to_number
    global __class_number_to_name

    with open("./artifacts/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open('./artifacts/saved_model.pkl', 'rb') as f:
            __model = joblib.load(f)
    print("loading saved artifacts...done")







