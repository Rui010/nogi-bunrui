import os
import sys

import cv2
from scipy import ndimage

class DataArgumentation():
    def __init__(self, img_path):
        self.path = img_path
        self.filename = os.path.basename(img_path)
        self.dir = os.path.dirname(img_path)
        self.img = cv2.imread(img_path)
    
    def rotation(self, ang):
        img_rot = ndimage.rotate(self.img, ang)
        img_rot = cv2.resize(img_rot, (64,64))
        output = os.path.join(self.dir, "rot-" + str(ang) + "-" + self.filename)
        cv2.imwrite(output, img_rot)
        return True
    
    def threshold(self):
        img_thr = cv2.threshold(self.img, 100, 255, cv2.THRESH_TOZERO)[1]
        output = os.path.join(self.dir, "thr-" + self.filename)
        cv2.imwrite(output, img_thr)
        return True
    
    def filter(self):
        img_filter = cv2.GaussianBlur(self.img, (5, 5), 0)
        output = os.path.join(self.dir, "flt-" + self.filename)
        cv2.imwrite(output, img_filter)
        return True
    
    def __call__(self):
        self.rotation(10)
        self.threshold()
        self.filter()

if __name__ == "__main__":
    test = sys.argv[1]
    data_argumentation = DataArgumentation(test)
    data_argumentation()
