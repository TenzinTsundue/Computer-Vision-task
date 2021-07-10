# Reading images and video

# reading image
import cv2 as cv

img = cv.imread("photos/itachi.jpg")
cv.imshow('Itachi', img)  # name and the image 
cv.waitKey(0)  # wait for specific second 0=infinite

# reading video
import cv2 as cv

capture = cv.VideoCapture('videos/itachi.mp4')    # 0 for the webcam
while True:
	isTrue, frame = capture.read() # grab video frame by frame
	cv.imshow('Video', frame)
	if cv.waitKey(20) & 0xFF==ord('d'):  # if d is pressed 
		break
capture.release()
cv.distroyAllWindow()
