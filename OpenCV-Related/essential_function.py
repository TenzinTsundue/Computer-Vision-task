# Essential Function

import cv2 as cv

img = cv.imread('photos/itachi.jpg')
cv.imshow('Itachi', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Itachi_gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)   # 3,3 is kernel size(width and height of filter mask) to create blur image
# cv.imshow('Itachi_blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# Dilating the image
dilated= cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('DIlated', dilated)

# Eroding the image (opposite of dilation)
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500)) # interpolation
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]   # using image slicing
cv.imshow("Cropped", cropped)

cv.waitKey(0)