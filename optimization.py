import cv2
import numpy as np

def optimize(frame):
    blurred = cv2.GaussianBlur(frame, (1, 1), 0)
    canny = cv2.Canny(blurred, 100, 200)

    return canny
