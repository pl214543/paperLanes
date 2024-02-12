# NEED TO CITE CODE
# https://uark.libguides.com/CSCE/CitingCode
# https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
# cv2.line(image, start_point, end_point, color, thickness)
# have a programming plan and glossary + technical algorithm
# dodge and burn
# field of view
# maybe grayscale and then remove all darker colors (+ dodge and burn)
# https://www.geeksforgeeks.org/filter-color-with-opencv/
# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/ for capturing video and editing
# https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
# maybe what I can do is cut out a part, edit it, and put it back onto the frame
# https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
# https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

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

    lines = cv2.HoughLines(cropped, 1, num.pi/180, 150)

    final = drawing(lines, optimized)

    # https://www.geeksforgeeks.org/filter-color-with-opencv/
    # ranged = cv2.inRange(blurred, 0, 115)
    # result = cv2.bitwise_and(blurred, blurred, mask=ranged)

    # edges = cv2.Canny(result, 50, 150, apertureSize=3)

    # https://learnopencv.com/cropping-an-image-using-opencv/

    cv2.imshow('Frame', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# import detectLines
