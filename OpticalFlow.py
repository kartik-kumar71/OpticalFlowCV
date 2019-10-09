__author__ = "soskill"


import cv2
import numpy as np

cam = cv2.VideoCapture(0)

image = cam.read()[1]
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
old_frame = image
while True:
    _,frame = cam.read()
    new_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    diff_frame = cv2.absdiff(new_frame,old_frame)
    cv2.imshow("image",diff_frame)
    if cv2.waitKey(10) == ord('q'):
        break
    old_frame = new_frame
