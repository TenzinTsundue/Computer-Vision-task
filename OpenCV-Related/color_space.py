# Colour Space
# OpenCV use BGR image

import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread('photos/bhagsu.jpg')
# cv.imshow('Bhagsu', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Bhagsu_gray', gray)

# BGR to HSV(Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('Bhagsu_hsv', hsv)

# BGR to L*a *b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Bhagsu_lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('Bhagsu_rgb', rgb)

# plt.imshow(rgb)
# plt.show()

# All conversion can be converted back to BGR

cv.waitKey(0)