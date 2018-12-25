import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import configparser
import tensorflow as tf
from keras.models import load_model
from keras.backend import tensorflow_backend as backend
from PIL import Image

# 設定ファイルに取り込むディレクトリを記載
inifile = configparser.ConfigParser()
inifile.read("./config.ini", "UTF-8")
DIRS = inifile.get('settings', 'dirs').split(",")

MODEL_PATH = "./model/model.h5"
CASCADE_FILE = "./model/haarcascade_frontalface_alt.xml"

class TrimFace():
    def __init__(self):
        pass

    def __call__(self, in_jpg, out_jpg):
        image = cv2.imread(in_jpg)
        cascade = cv2.CascadeClassifier(CASCADE_FILE)
        face_list = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(60,60))
        if len(face_list) > 0:
            for rect in face_list:
                _img = image[rect[1]:rect[1]+rect[3], rect[0]: rect[0]+rect[2]]
                _img = cv2.resize(_img, dsize=(64,64))
                cv2.imwrite(out_jpg, _img)
            return True
        else:
            return False

    def classify_face(self, img):
        backend.clear_session()
        model = load_model(MODEL_PATH)
        global graph
        graph = tf.get_default_graph()
        with graph.as_default():
            _img = cv2.imread(img)
            _img = cv2.resize(_img, dsize=(64,64))
            _img = np.expand_dims(_img, axis=0)
            return DIRS[np.argmax(model.predict(_img))]

if __name__ == "__main__":
    trim_face = TrimFace()
    for dir in DIRS:
        print("Progress..." + dir)
        files = os.listdir(dir)
        ind = 1
        for f in files:
            path = os.path.join(dir,"face")
            if not os.path.exists(path):
                os.mkdir(path)
            if trim_face(os.path.join(dir,f), os.path.join(dir,"face", str(ind) + ".jpg")):
                ind += 1
                print("%d ％" % ((ind / len(files))*100))
