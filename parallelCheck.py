# import required libraries
import cv2
import numpy as num
import math

# function to find angle of a line in order for parallel comparisons
def findAngle(line):

    # unpacks the start and end points
    x1, y1, x2, y2 = line[0]

    # gets the slope of the line
    slope = (x2 - x1) / float(y2 - y1)

    # gets the arc tan of the slope for angle
    angle = num.arctan(slope)

    # returns the angle
    return angle

# function to get the difference of the angles
def subAngles(angle1, angle2):

    # difference
    newAngle = angle2 - angle1

    # in case absolute value isn't needed
    finalAngle = newAngle

    # checks if it is less than 0
    if newAngle < 0:

        # if it is, the absolute value is recieved
        finalAngle = num.abs(finalAngle)

    # return the absolute value of the difference
    return finalAngle

# function finds and saves parallel lines
def findParallels(lines):

    # makes the list that will store the parallel lines
    parallels = []

    # iterates through the lines
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j: continue

            # gets the angle of the first line
            angle1 = findAngle(lines[i])

            # gets the angle of the second line
            angle2 = findAngle(lines[j])

            # gets the difference of the angles
            difference = subAngles(angle1, angle2)

            # approximates the parallels because it won't be perfect
            if 0 <= difference <= 2:

                # the parallel lines will be appended
                parallels.append([lines[i], lines[j]])

    # returns the list of parallel lines
    return parallels
