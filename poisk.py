import cv2
from os import listdir
import numpy as np

img = cv2.imread("ad\TESTIMAGES\withBears\\" + "_2016-04-25 11-06-03_2568_L.JPG")

img = cv2.resize(img, (750, 750))

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype("float32")
(h, s, v) = cv2.split(imghsv)
s = s * 5.4
s = np.clip(s, 0, 255)
imghsv = cv2.merge([h, s, v])
imgBGR = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)
result = np.uint8(np.clip((-0.5 * imgBGR + 100), 0, 255))

maxd = []

for x in range(0,750):
    for y in range(0,750):

        if result[x,y,0] > result[x,y,1] + 30 and result[x,y,0] > result[x,y,2] +30 :
            img[x,y,0] = 255
            img[x,y,1] = 0
            img[x,y,2] = 0
            
            maxd += [[y,x,1]]

for i in maxd:
    for j in maxd:
        if i != j:
            d = ((i[0]-j[0])**2+(i[0]-j[0])**2)**0.5 or 1
            if d < 5:
                i[2] += 1/d


print(maxd)
lutsh = max(maxd,key=lambda i: i[2])


cv2.rectangle(img, (lutsh[0]-10, lutsh[1]-10),(lutsh[0]+10, lutsh[1]+10),(0,0,255), 1)


cv2.imshow("1",img)
cv2.waitKey(0)