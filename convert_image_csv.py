import os
import numpy as np
import pandas as pd
import cv2
from PIL import Image
import configparser

# 設定ファイルに取り込むディレクトリを記載
# ディレクトリ名順に正解ラベルを0からふる
inifile = configparser.ConfigParser()
inifile.read("./config.ini", "UTF-8")
DIRS = inifile.get('settings', 'dirs').split(",")
DATA_DIR = "data"

H = 64
W = 64
# jpgをCSV
def convert_train_image(img):
    _img = cv2.imread(img)
    _img = cv2.resize(_img, (H, W))
    print(type(_img), _img.shape)
    return _img

# One-hot vector
def convert_teach_data(list):
    pass

def save_npy(output_file, ndarray_data):
    np.save(os.path.join(DATA_DIR, output_file))
    return True

print(convert_train_image("test.jpg"))

# if __name__ == "__main__":
#     X = []
#     t = []
#     for img in os.listdir(os.path.join(DIRS[0], "face")):
#         img_arr = [Image.open(img)]
#         print(img_arr)
#         print(img_arr.shape())
#         X.append(img_arr)
#         t.append(0)
#     X = X.astype('float32')
#     X = X / 255
#     # Y = np_utils.to_categorical(Y, 10)
#     print(X)
#     print(Y)
