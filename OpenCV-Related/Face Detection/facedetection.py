# Face Detection 
# Using Haarcascades

import cv2 as cv

img = cv.imread('photos/oda.jpg')
cv.imshow('Oda', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

# read haarcascades
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=7)   # returns a list of rectangele co-or

print(f'Nuber of faces found : {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
	cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)

