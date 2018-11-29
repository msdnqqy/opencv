
"""
合并两个双目摄像头的图像
然后用canny寻找物体轮廓
实验结果：
优点：单canny容易遗漏的 相加后的图片可以更好的找出来
缺点：产生了大量的椒盐噪声
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage
from canny边缘检测 import *
from 合并图像 import *

def canny1(img):
    canny_img=cv.Canny(img,200,300)
    return canny_img

def doCouner(img):
    img_canny=canny(img)
    img_add=add(img)
    img_add_canny=canny1(img_add)
    cv.imshow('canny_add_img',img_add_canny)

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        doCouner(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break;