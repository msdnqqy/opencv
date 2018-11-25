import cv2 as cv
import numpy as np;

cap_index=0

cap=cv.VideoCapture(cap_index)
cap.set(3,1280)
cap.set(4,480)
# cap.set(3,2560)
# cap.set(4,720)

i=0
while i<1000:
    s,f=cap.read()
    cv.imshow('1',f)
    cv.waitKey(20)
    i+=1

cap.release()
cv.destroyAllWindows()