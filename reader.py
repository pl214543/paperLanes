import cv2
import numpy as num

def rectangle(frame):

    height, width = frame.shape[:2]

    topleftx = width * 0.175
    topleftx = int(topleftx)
    toplefty = height * 0.725
    toplefty = int(toplefty)
    bottomrightx = width * 0.85
    bottomrightx = int(bottomrightx)
    bottomrighty = height * 0.25
    bottomrighty = int(bottomrighty)

    rectangled = cv2.rectangle(frame, (topleftx, toplefty), (bottomrightx, bottomrighty), 255, 3)

    return rectangled

def crop(frame):

    # https://www.tutorialspoint.com/how-to-mask-an-image-in-opencv-python

    height, width = frame.shape[:2]

    topleftx = width * 0.175
    topleftx = int(topleftx)
    toplefty = height * 0.725
    toplefty = int(toplefty)
    bottomrightx = width * 0.85
    bottomrightx = int(bottomrightx)
    bottomrighty = height * 0.25
    bottomrighty = int(bottomrighty)

    mask = num.zeros(frame.shape[:2], num.uint8)
    mask[toplefty:bottomrighty, topleftx:bottomrightx] = 255

    cropped = cv2.bitwise_and(frame, frame, mask)

    return cropped
