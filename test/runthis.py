
"""
综合启动类
"""
url=r'http://192.168.1.9:8080/?action=stream'
import cv2 as cv
import numpy as np;


def run(functionref=None):
    if __name__=='__main__':
    cap=cv.VideoCapture(url)
    while True:
        s,f=cap.read()

        if functionref is not None:
            functionref(f)
            if cv.waitKey(5)==27:
                cap.release()
                cv.destroyAllWindows()
                break;

