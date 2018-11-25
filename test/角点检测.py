
"""
角点检测,比较耗费时间
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;
from scipy import  ndimage
import time

i=0

def cornerHarris(img):
    img_copy=img.copy()
    a=time.time()
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_harris=cv.cornerHarris(img,2,23,0.04)
    b=time.time()
    img_copy[img_harris>0.01*img_harris.max()]=[0,0,255]

    cv.imshow('img-harris',img_harris)
    cv.imshow('img',img_copy)
    
    print('处理速率：{0}帧/s'.format(round(1/(b-a),1)))
    

if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()
        cornerHarris(f)
        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break