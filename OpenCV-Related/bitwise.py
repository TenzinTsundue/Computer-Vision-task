# BITWISE operator in openCV
# AND OR XOR NOT

import cv2 as cv
import numpy as np

blank = np.zeros((400,800), dtype='uint8')

circle_left = cv.circle(blank.copy(), (280,200), 180, 255, -1)
circle_right = cv.circle(blank.copy(), (520,200), 180, 255, -1)

cv.imshow('Circle left', circle_left)
cv.imshow('Circle right', circle_right)

# bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(circle_left, circle_right)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non-intersecting and Intersecting
bitwise_or = cv.bitwise_or(circle_left, circle_right)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting 
bitwise_xor = cv.bitwise_xor(circle_left, circle_right)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(circle_left)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)
