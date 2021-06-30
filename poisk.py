import cv2
from os import listdir

img = cv2.imread("./changed/withBears/" + "2016-05-13 10-16-57_0024_1L.JPG")

imgmoment = img.copy()

maxd = (0,0)

for x in range(0,750):
    for y in range(0,750):

        if img[x,y,0] > img[x,y,1] + 20 and img[x,y,0] > img[x,y,2] +20 :
            imgmoment[x,y,0] = 255
            imgmoment[x,y,1] = 0
            imgmoment[x,y,2] = 0

            maxd = (x,y)
cv2.imshow("2",imgmoment)
imgmoment = cv2.cvtColor(imgmoment, cv2.COLOR_BGR2HSV )

imgmoment = cv2.inRange(imgmoment, (220,0,0), (240,100,100))
moments = cv2.moments(imgmoment, 1)

print(moments.items())
dM01 = moments['m01']
dM10 = moments['m10']
dArea = moments['m00']


#x = int(dM10 / dArea)
#y = int(dM01 / dArea)
cv2.rectangle(img, (maxd[0]-5, maxd[1]-5),(maxd[0]+5, maxd[1]+5),(0,0,255), 1)
cv2.rectangle(img, (maxd[0]-5, maxd[1]-5),(maxd[0]+5, maxd[1]+5),(0,0,255), 1)

cv2.imshow("1",img)
cv2.waitKey(0)