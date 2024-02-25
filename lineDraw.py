# import required libraries
import cv2
import numpy as num
from parallelCheck import findParallels

# function for drawing the straight lines
def drawing(frame, lines):

    averageStartX = 0
    averageStartY = 0
    averageEndX = 0
    averageEndY = 0

    # checks if anything is in the list of lines (do any lines exist) so no errors appear
    if lines is not None:

        parallels = findParallels(lines, frame)

        if len(parallels) != 0:
            for parLines in parallels:
                for line in parLines:
                    averageStartX += line[0][0]
                    averageEndX += line[0][2]
                    averageStartY += line[0][1]
                    averageEndY += line[0][3]

            averageStartX = averageStartX.item()
            averageEndX = averageEndX.item()
            averageStartY = averageStartY.item()
            averageEndY = averageEndY.item()

            averageStartX = averageStartX / int(len(parallels))
            averageEndX = averageEndX / int(len(parallels))
            averageStartY = averageStartY / int(len(parallels))
            averageEndY = averageEndY / int(len(parallels))

            averageStartX = int(averageStartX)
            averageEndX = int(averageEndX)
            averageStartY = int(averageStartY)
            averageEndY = int(averageEndY)

            print("\n\n\n\n\n" + str(averageStartX) + "\n\n\n\n\n")

            cv2.line(frame, (averageStartX, averageStartY), (averageEndX, averageEndY), (0, 255, 0), 2)

        for parLines in parallels:
            pass

    return frame

    # cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


    # returns the frame with lines drawn
    return frame
