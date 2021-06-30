"""
modulo 1 -- change a photo
"""

from os import listdir
from os.path import abspath
import cv2
import numpy as np
from PIL import Image


def change_contrast(file_name):
    img = cv2.imread("./workDirectory/" + file_name)
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv2.split(imghsv)
    s = s * 5.4
    s = np.clip(s, 0, 255)
    imghsv = cv2.merge([h, s, v])
    imgBGR = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
    result = np.uint8(np.clip((-0.5 * imgBGR + 100), 0, 255))
    result = cv2.resize(result, (1000, 1000))
    cv2.imwrite("./changed/" + file_name, result)


for file_name in listdir("./workDirectory"):
    if file_name != "":

        print(f"\rProceed: {listdir('./workDirectory').index(file_name) / len(listdir('./workDirectory')) * 100}%", end="")
        change_contrast(file_name)

"""
modulo 2 -- through neuralNetwork
"""


