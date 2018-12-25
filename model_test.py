import os, sys
import cv2
import numpy as np
import configparser
import matplotlib.pyplot as plt
from keras.models import load_model

inifile = configparser.ConfigParser()
inifile.read("./config.ini", "UTF-8")
MEMBER = inifile.get('settings', 'dirs').split(",")

MODEL_PATH = "./model/model.h5"
CASCADE_FILE = "./model/haarcascade_frontalface_alt.xml"

def detect_face(test_jpg):
    image = cv2.imread(test_jpg)
    cascade = cv2.CascadeClassifier(CASCADE_FILE)
    face_list = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(45,45))
    if len(face_list) > 0:
        for rect in face_list:
            x,y,width,height = rect
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (255,0,0), thickness=3)
            _img = image[rect[1]:rect[1]+rect[3], rect[0]: rect[0]+rect[2]]
            _img = cv2.resize(_img, dsize=(64,64))
            _img = np.expand_dims(_img, axis=0)
            name = classify_face(_img)
            cv2.putText(image, name,(x,y+height+20), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
    else:
        print('no face')
    return image

def classify_face(img):
    print(model.predict(img))
    return MEMBER[np.argmax(model.predict(img))]

if __name__ == "__main__":
    model = load_model(MODEL_PATH)
    test_img = sys.argv[1]
    class_face = detect_face(test_img)

    plt.imshow(class_face)
    plt.show()
