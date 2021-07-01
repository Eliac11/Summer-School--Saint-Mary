import cv2
from os import listdir
import numpy as np


def chose_bear(path):
    """
    пинимает путь к фото
    возвращает словарь с картинкой(img), есть медведь или нет(bearis), координаты медведя на картинке(xy)

    """

    img = cv2.imread(path)
    orig = img.copy()
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
                maxd += [[y,x,1]]
    
    for i in maxd:
        for j in maxd:
            if i != j:
                d = ((i[0]-j[0])**2+(i[0]-j[0])**2)**0.5 or 1
                if d < 5:
                    i[2] += 1/d
    
    #
    print(maxd)
    #

    #lutsh = max(maxd,key=lambda i: i[2])
    lutsh = maxd[0]
    for i in maxd:
        if i[2] > 5 and i[2] < 9:
            if lutsh[2] < i[2]:
                lutsh = i
    
    lutsh[0] = int(lutsh[0]/750*orig.shape[1])
    lutsh[1] = int(lutsh[1]/750*orig.shape[0])

    #
    print(lutsh)
    #

    if lutsh[2] > 5:
        cv2.rectangle(orig, (lutsh[0]-30, lutsh[1]-30),(lutsh[0]+30, lutsh[1]+30),(0,0,255), 4)
        bis = True
    else:
        bis = False

    return {"img":orig,"bearis":bis,"xy":(lutsh[0],lutsh[1])}

if __name__ == "__main__":

    result = chose_bear("ad/TESTIMAGES/withBears/" + "image_1.JPG")
    cv2.imwrite('1.JPG',result["img"])
    cv2.imshow("1",result["img"])
    cv2.waitKey(0)