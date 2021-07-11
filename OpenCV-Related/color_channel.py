# Split and merge color channal

import cv2 as cv
import numpy as np

img = cv.imread('photos/bhagsu.jpg')
cv.imshow('Bhagsu', img)

blank = np.zeros(img.shape[:2], dtype='uint8')   #for first two value and dtype is for image

b,g,r = cv.split(img)   # will split into blue green and red

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,b,blank])
red = cv.merge([blank,blank,b])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merge', merged)

cv.waitKey(0)