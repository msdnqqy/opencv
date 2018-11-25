"""
高通滤波
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage

def dealgaotong(img):
    blur_img=cv.GaussianBlur(img,(9,9),0)
    g_img=img-blur_img
    cv.imshow('blur-img',blur_img)
    cv.imshow('g-img',g_img)


if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        dealgaotong(f)
        if cv.waitKey(10)==27:
            cap.release()
            cv.destroyAllWindows()
            break;
