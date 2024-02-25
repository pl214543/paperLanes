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

        parallels = findParallels(lines)

        print(parallels)

        if len(parallels) != 0:
            for parLines in parallels:
                print(parLines)
                for line in parLines:
                    print(line[0][0])
                    averageStartX += line[0][0]
                    averageEndX += line[0][2]
                    averageStartY += line[0][1]
                    averageEndY += line[0][3]

                averageStartX = averageStartX.item()
                averageEndX = averageEndX.item()
                averageStartY = averageStartY.item()
                averageEndY = averageEndY.item()

                averageStartX = averageStartX / 2
                averageEndX = averageEndX / 2
                averageStartY = averageStartY / 2
                averageEndY = averageEndY / 2

                averageStartX = int(averageStartX)
                averageEndX = int(averageEndX)
                averageStartY = int(averageStartY)
                averageEndY = int(averageEndY)

                cv2.line(frame, (averageStartX, averageStartY), (averageEndX, averageEndY), (0, 255, 0), 2)

        for parLines in parallels:
            for line in parLines:
                x1, y1, x2, y2 = line[0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    return frame

    # cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
