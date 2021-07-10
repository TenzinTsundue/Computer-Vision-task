# Drawing shpaes and putting text

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # crate a blank image, 3 for number of colour channal RGB
# cv.imshow('Blank', blank)

# paint the image with certain colour
blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,0,255), thickness=cv.FILLED)   # origin form the top left, -1 for filled
# cv.imshow('Rectangel', blank)

# draw a circle
cv.circle(blank, (250,250), 100, (255,0,0), thickness=3)
# cv.imshow('Circle', blank)

# draw a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)   # shape[1] is width and shape[0] is height
# cv.imshow('Line', blank)

# write text
cv.putText(blank, 'Hello World!!!', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)