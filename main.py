# import required libraries
import cv2
import numpy as num
import math
from reader import rectangle, crop
from optimization import optimize
from lineDraw import drawing

video = cv2.VideoCapture(0)

def checkVideo(video):
    if video.isOpened():
        print("Video will not open.")

checkVideo(video)

# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
while True:
    booleanReady, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    optimized = optimize(grey)
    rectangled = rectangle(frame)
    cropped = crop(optimized)

    lines = cv2.HoughLines(cropped, 1, num.pi/180, 200)

    final = drawing(lines, optimized)

    cv2.imshow('Frame', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
