
"""
轮廓检测
找出轮廓
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;

def getContours(img):
    ret,thresh=cv.threshold(cv.cvtColor(img,cv.COLOR_RGB2GRAY),57,155,0)
    image,contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    color=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    img=cv.drawContours(img,contours,-1,(0,255,0),2)
    cv.imshow('contours',img)

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        getContours(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break;