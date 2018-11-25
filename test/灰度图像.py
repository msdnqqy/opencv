
"""
灰度图像
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage


def gray(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('gray-img',img)

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        gray(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break;