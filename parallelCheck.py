import cv2
import numpy as num
import math

def findAngle(line):

    x1, y1, x2, y2 = line[0]

    slope = (x2 - x1) / float(y2 - y1)

    num.arctan(slope)

    return slope

def subAngles(angle1, angle2):

    newAngle = angle2 - angle1

    finalAngle = newAngle

    if newAngle < 0:
        finalAngle = num.abs(finalAngle)

    return finalAngle

def findParallels(lines, frame):
    parallels = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j: continue

            angle1 = findAngle(lines[i])

            angle2 = findAngle(lines[j])

            difference = subAngles(angle1, angle2)

            if 0 <= difference <= 3:
                # You've found a parallel line!
                parallels.append([lines[i], lines[j]])

    return parallels
