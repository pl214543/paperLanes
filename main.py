# import required libraries
import cv2
import numpy as num
import math

# import functions
from reader import rectangle, crop
from optimization import optimize
from lineDraw import drawing

# video capture
video = cv2.VideoCapture(0)

# check if the video is opened
def checkVideo(video):
    if video.isOpened():
        print("Video will not open.")

checkVideo(video)

while True:
    booleanReady, frame = video.read()

    # grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # uses the functions from the other files to optimize, make a rectangle, and crop
    optimized = optimize(grey)
    rectangled = rectangle(frame)
    cropped = crop(optimized)

    # detect the lines
    lines = cv2.HoughLines(cropped, 1, num.pi/180, 200)

    # draw the final lines
    final = drawing(optimized, lines)

    cv2.imshow('Frame', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
