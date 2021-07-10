# Resize and rescale image

import cv2 as cv

img = cv.imread('photos/itachi.jpg')

def rescaleFrame(frame, scale=0.75):
	# Images, Videos and Live videos
	width = int(frame.shape[1] * scale)   # shape[1] is width
	height = int(frame.shape[0] * scale)   # shape[0] is height
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

new_img = rescaleFrame(img, 0.5)

cv.imshow('Itachi', new_img)   # show the resized image
cv.waitKey(0)  

# For live video
def changeRes(width, height):
	# Live video
	capture.set(3, width)   # 3 for width
	capture.set(4, height)   # 4 for height

# reading video
capture = cv.VideoCapture('videos/itachi.mp4')   
while True:
	isTrue, frame = capture.read() # grab video frame by frame
	frame_resized = rescaleFrame(frame)

	cv.imshow('Video', frame)   # show the original video 
	cv.imshow('Video Resized', frame_resized)  # show the resized video

	if cv.waitKey(20) & 0xFF==ord('d'):  # if d is pressed 
		break

capture.release()
cv.distroyAllWindow()