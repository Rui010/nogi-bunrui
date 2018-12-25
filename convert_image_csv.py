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
TRAIN_DIR = "face"

H = 64
W = 64
# jpgをCSV RGBの3チャネル
def convert_train_image(img):
    _img = cv2.imread(img)
    _img = cv2.resize(_img, (H, W))
    return _img

# One-hot vector
def convert_teach_data(vector):
    n_labels = len(np.unique(vector))
    return np.eye(n_labels)[vector]

def save_npy(output_file, ndarray_data):
    np.save(os.path.join(DATA_DIR, output_file + ".npy"), ndarray_data)
    return True

def num_face_files(dirs, path):
    num = 0
    for dir in dirs:
        num += len(os.listdir(os.path.join("images", dir, path)))
    return num

if __name__ == "__main__":
    n = num_face_files(DIRS, TRAIN_DIR)
    X = np.zeros((n, H, W, 3))
    t = []
    temp = 0
    for i, dir_img in enumerate(DIRS):
        files = os.listdir(os.path.join("images", dir_img, TRAIN_DIR))
        # _X = np.zeros((len(files), H, W, 3))
        _t = []
        for j, img in enumerate(files):
            f = os.path.join("images", dir_img, TRAIN_DIR, img)
            X[temp + j] = convert_train_image(f)
            print(X[temp + j])
            _t.append(i)
        temp += len(files)
        t.extend(_t)
    X = X.astype('float32') / 255
    # X = X.astype('float32')
    t = convert_teach_data(t)
    save_npy("x_train", X)
    save_npy("t_train", t)
