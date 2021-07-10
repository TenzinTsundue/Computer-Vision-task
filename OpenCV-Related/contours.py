# Contours - boundries of the object

import cv2 as cv
import numpy as np

img = cv.imread('photos/itachi.jpg')
# cv.imshow('Itachi', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)   # for edges
# cv.imshow('Canny', canny)

ret, threash = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)   # x<125-->0(black) or x>125-->255(white)
cv.imshow('Thresh', threash)

contours, hierarchies = cv.findContours(threash, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of contours: {len(contours)}')

# draw contours on a blank
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours image', blank)

cv.waitKey(0) 
