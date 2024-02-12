import cv2
import numpy as np

def optimize(frame):
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    canny = cv2.Canny(blurred, 50, 150, 3)

    return canny
