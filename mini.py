import ad.poisk
from os import listdir
from tkinter import Tk, filedialog

import cv2

input("выберете директорию с фото (Enter)")

root = Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
folder = filedialog.askdirectory()
path = folder

for i in listdir(path):
    try:
        result = ad.poisk.chose_bear(path + "\\" + i)
        cv2.imwrite("results/"+i,result["img"])

        print(i, "   ---successfully")
    except Exception as e:
        print(e)

print("обработанные фото находятся в папке:  results")

input()



