
"""
角点检测,比较耗费时间
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage
import time


def canny(img):
    cv.imshow('img',img)
    canny_img=cv.Canny(cv.cvtColor(img,cv.COLOR_RGB2GRAY),200,300)
    cv.imshow('canny-img',canny_img)
    return canny_img

    

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        canny(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break