import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests, jsonify
import tempfile
import keras
import glob
import pafy
import cv2
import os

from PIL import Image, UnidentifiedImageError
from streamlit_cropper import st_cropper
from urlib.parse import urlparse
from skimage import transform
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
from matplotlib.patches import Rectangle, Circle
from random import choice, randint
from io import BytesIO
from numpy import asarray

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


