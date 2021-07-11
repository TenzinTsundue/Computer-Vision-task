# Masking
import cv2 as cv
import numpy as np

img = cv.imread('photos/itachi.jpg')
cv.imshow('Itachi', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image',blank)

mask = cv.rectangle(blank, (220,180), (520,250), 255, -1)
cv.imshow('mask rectangle', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0) 
