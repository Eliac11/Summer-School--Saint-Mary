import cv2
from os import listdir

for file_name in listdir("./changed/empty"):
    img = cv2.imread("./changed/empty/" + file_name)
    img = cv2.resize(img, (500, 500))
    cv2.imwrite("./changed/empty/" + file_name, img)

for file_name in listdir("./changed/withBears"):
    img = cv2.imread("./changed/withBears/" + file_name)
    img = cv2.resize(img, (500, 500))
    cv2.imwrite("./changed/withBears/" + file_name, img)
