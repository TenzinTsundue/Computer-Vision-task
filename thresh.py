# Thresholding
# Simple and Adaptive thresholding

import cv2 as cv

img = cv.imread('photos/bhagsu.jpg')
cv.imshow('Bhagsu', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Simple Threasholding (manually set thershold value)
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# print(threshold)   # will show the 100 as the threshold value
cv.imshow('Simple Thresholded', thresh)

# inverse threshold image
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Thresholded', thresh_inv)

# Adaptive Thresholding (computer find the optimal threshold value)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.
	THRESH_BINARY, 11, 3)   # Kernal size 11, C value 3 
cv.imshow("Adaptive Thresholded", adaptive_thresh)

cv.waitKey(0)



