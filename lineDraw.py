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

                    print(averageStartX)
                    averageStartX += line[0][0]
                    print(averageEndX)
                    averageEndX += line[0][2]
                    print(averageStartY)
                    averageStartY += line[0][1]
                    print(averageEndY)
                    averageEndY += line[0][3]

                    averageStartX = averageStartX.item()
                    print(averageStartX)
                    averageEndX = averageEndX.item()
                    print(averageEndX)
                    averageStartY = averageStartY.item()
                    print(averageStartY)
                    averageEndY = averageEndY.item()
                    print(averageEndY)

                    print(averageStartX)
                    averageStartX = averageStartX / 2
                    print(averageEndX)
                    averageEndX = averageEndX / 2
                    print(averageStartY)
                    averageStartY = averageStartY / 2
                    print(averageEndY)
                    averageEndY = averageEndY / 2

                    print(averageStartX)
                    averageStartX = int(averageStartX)
                    print(averageEndX)
                    averageEndX = int(averageEndX)
                    print(averageStartY)
                    averageStartY = int(averageStartY)
                    print(averageEndY)
                    averageEndY = int(averageEndY)

            cv2.line(frame, (averageStartX, averageStartY), (averageEndX, averageEndY), (0, 255, 0), 2)

        for parLines in parallels:
            for line in parLines:
                x1, y1, x2, y2 = line[0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    return frame
