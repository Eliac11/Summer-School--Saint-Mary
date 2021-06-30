import cv2
from os import listdir

img = cv2.imread("./changed/withBears/" + "_2016-05-12 14-20-10_2145_2R.JPG")

maxd = []

for x in range(0,750):
    for y in range(0,750):

        if img[x,y,0] > img[x,y,1] + 20 and img[x,y,0] > img[x,y,2] +20 :
            img[x,y,0] = 255
            img[x,y,1] = 0
            img[x,y,2] = 0
            
            maxd += [(y,x)]

#x = int(dM10 / dArea)
#y = int(dM01 / dArea)

lastxy = (-100,-100)
for i in maxd:
    if ((i[0]-lastxy[0])**2+(i[0]-lastxy[0])**2)**0.5 > 5:
        cv2.rectangle(img, (i[0]-10, i[1]-10),(i[0]+10, i[1]+10),(0,0,255), 1)
        lastxy = i

cv2.imshow("1",img)
cv2.waitKey(0)