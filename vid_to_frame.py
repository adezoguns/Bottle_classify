import cv2
import time
import sys

capture = cv2.VideoCapture('/media/deola/SERECO/Data_set_for_Alcohol/ZOOM0040.MOV')
count=200
capture.set(cv2.CAP_PROP_POS_MSEC, count) 
success,frame = capture.read()

while success:
	'''This program helps to
			 convert videos to frames'''
	
	cv2.imwrite("/home/deola/Bottle_classify/Alcohol_dataset/Ricard/R8/R8%d.jpg" %count, frame)   
	#cv2.imshow("frame%d" %count,frame)
	#cv2.waitKey()           
	count+=200
	capture.set(cv2.CAP_PROP_POS_MSEC, count) 
	success,frame = capture.read() 


capture.release()	
