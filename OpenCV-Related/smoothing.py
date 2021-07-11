# Blurring Techinques

import cv2 as cv

img = cv.imread('photos/bhagsu.jpg')
cv.imshow('Bhagsu', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (retain the edges of the image)
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral )

cv.waitKey(0)