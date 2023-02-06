import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests, jsonify, joblib

import glob
import pafy
import cv2
import os
import base64

from PIL import Image, UnidentifiedImageError

from PyWavelets import w2d


FILE_TYPES = ["png", "bmp", "jpg", "jpeg"]


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




