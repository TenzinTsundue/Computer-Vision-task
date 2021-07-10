# Image Transformation

import cv2 as cv
import numpy as np

img = cv.imread('photos/itachi.jpg')
# cv.imshow('Itachi', img)

# translation (shifting in x or y direction)
def translate(img, x, y):
	transMat = np.float32([[1,0,x], [0,1,y]])
	dimensions = (img.shape[1], img.shape[0])
	return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
# cv.imshow('translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):   # rotation is counter clockwise
	(height, width) = img.shape[:2]

	if rotPoint is None:
		rotPoint = (width//2, height//2)

	rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
	dimensions = (width, height)

	return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
# cv.imshow('Rotated_90', rotated)

#  Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # interpolation
# cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)   # veritical flip
# cv.imshow('Flipped', flip)

# 0 --> Vertical flip
# 1 --> horizontal flip
# -1 --> both flip

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0) 