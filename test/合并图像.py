
"""
合并两个双目摄像头的图像
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage


def add(img):
    
    np_img=np.array(img)
    np_img2=np_img[:,640:1280]
    np_img1=np_img[:,0:640]

    np_img_add=np_img1+np_img2
    cv.imshow('np_img_add',np_img_add)
    cv.imshow('img',img)

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        add(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break;