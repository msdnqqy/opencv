"""
对图像的数据进行平方，拉大图像像素之间的差距
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;

class LargePx(object):
    def __init__(self,L=2):
        self.L=L
    
    def doLarge(self,img):
        img_large=img*2
        px_max=np.max(img_large)
        img_large=img_large/px_max
        img_large*=255
        img_large=img_large.astype(np.uint8)
        img_large[img_large<1]=1
        img_large[img_large>255]=255
        # img_large[:,:]=1
        return img_large

# class Corner(object):
    # def getCorner_canny(self,img):


if __name__=='__main__':
    cap=cv.VideoCapture(url)
    # LP=LargePx(2)
    LP=LargePx(1)
    while True:
        s,f=cap.read()
        f_gray=cv.cvtColor(f,cv.COLOR_RGB2GRAY)
        img_large=LP.doLarge(f_gray.copy())
        f_gray_cannay=cv.Canny(f_gray.copy(),200,300)
        f_gray_large_canny=cv.Canny(img_large,200,300)

        cv.imshow('f_gray',f_gray)
        cv.imshow('img_large',img_large)
        cv.imshow('f_gray_cannay',f_gray_cannay)
        cv.imshow('f_gray_large_canny',f_gray_large_canny)

        if cv.waitKey(5)==27:
            cap.release()
            cv.destroyAllWindows()
            break;

