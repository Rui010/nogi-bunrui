import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

in_jpg = "./karin/1.jpg"
out_jpg = "./test.jpg"

plt.show(plt.imshow(np.asarray(Image.open(in_jpg))))

image_gs = cv2.imread(in_jpg)

cascade = cv2.CascadeClassifier("")

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100,100))

if len(face_list) > 0:
    for rect in face_list:
        image_gs = image_gs[rect[1]:rect[1]+rect[3], rect[0]: rect[0]+rect[2]]
else:
    print("no face")

cv2.imwrite(out_jpg, image_gs)

plt.show(plt.imshow(np.asarray(Image.open(out_jpg))))