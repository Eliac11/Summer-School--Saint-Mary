"""
modulo 1 -- change a photo
"""

from os import listdir
from os.path import abspath
import cv2
import numpy as np

# for file_name in listdir("./workDirectory"):
img = cv2.imread("./workDirectory/image_20.JPG")
b, g, r = (np.array(a, int) for a in cv2.split(img))
g = np.zeros(b.shape, np.int64)
r = np.zeros(b.shape, np.int64)
yellowBGR = cv2.merge([b, g, r])
cv2.imwrite("yellow.jpg", yellowBGR)


"""
modulo 2 -- through neuralNetwork
"""
