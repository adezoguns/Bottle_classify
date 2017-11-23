import cv2
import time
import sys

capture = cv2.VideoCapture('/home/ogunleye/Desktop/vid1.mp4')
count=20000
capture.set(cv2.CAP_PROP_POS_MSEC, count) 
success,frame = capture.read()

while success:

	capture.set(cv2.CAP_PROP_POS_MSEC, count) 
	success,frame = capture.read() 
	cv2.imwrite("/home/ogunleye/Desktop/frame1/frame%d.jpg" %count, frame)   
	#cv2.imshow("frame%d" %count,frame)
	#cv2.waitKey()           
	count+=10000
	#cap.set(cv2.CAP_PROP_POS_MSEC, count) 
	#success,frame = capture.read() 


capture.release()	
