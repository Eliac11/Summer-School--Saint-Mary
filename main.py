"""
modulo 1 -- change a photo
"""

from os import listdir
from os.path import abspath
import cv2
import numpy as np

# for file_name in listdir("./workDirectory"):
img = cv2.imread("1.JPG")
cv2.imshow("1",img)

#b, g, r = (np.array(a, int) for a in cv2.split(img))
#g = np.zeros(b.shape, np.int64)
#r = np.zeros(b.shape, np.int64)
#yellowBGR = cv2.merge([b, g, r])
#cv2.imwrite("yellow.jpg", yellowBGR)

#final = cv2.medianBlur(img, 3)
#cv2.imshow("1",final)


#ориг
cv2.imshow("1",img)

# меняю насыщеность
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
(h, s, v) = cv2.split(imghsv)
s = s*5
s = np.clip(s,0,255)
imghsv = cv2.merge([h,s,v])

#перевод обратно в BGR
imgBGR = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
cv2.imshow("2",imgBGR)

# Меняю контрасность  (хотя на самом деле так себе получается надо подогнать еще эти 2 числа -0.5 и 100)
imgkon = np.uint8(np.clip((-0.5 * imgBGR + 100), 0, 255))
cv2.imshow("3",imgkon)

cv2.waitKey(0)
"""
modulo 2 -- through neuralNetwork
"""
