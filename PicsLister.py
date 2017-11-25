import os
import cv2
import shutil
from random import randint
import random

arr=[]
arr1=[]
def Getpics(path):

	'''This code creates a directory and puts all the images with .jpg 
	extension into a directory into a director named Mypath'''

	mypath=path
	if os.path.isdir(path+"/myPath")==False:
                os.mkdir(path+"/myPath")
	else:
		 shutil.rmtree(path+"/myPath")
		 os.mkdir(path+"/myPath")
	file_arr=os.listdir(mypath)
	for pic in file_arr:
		if '.jpg' in pic:
			arr.append(pic)
			img=cv2.imread(mypath+'/'+pic)	
			cv2.imwrite(path+"/myPath/"+pic, img) 

def Cutsomepics(path, numb):

	'''This function removes closely simillar pictures that are generated
	side by side. The arg 'numb' can be use to determine the amount
	of pictures removed before jumping to the next one. The new picutres
	are now inserted into a new folder called myReduPath '''
	
	count=0
	mypath=path
	if os.path.isdir(path+"/myReduPath")==False:
                os.mkdir(path+"/myReduPath")
	else:
		 shutil.rmtree(path+"/myReduPath")
		 os.mkdir(path+"/myReduPath")
	file_arr=os.listdir(mypath)
	for pic in file_arr:
		count=count+1
		if '.jpg' in pic:
			if count%numb == 0:
				arr1.append(pic)
				img=cv2.imread(mypath+'/'+pic)	
				cv2.imwrite(path+"/myReduPath/"+pic, img) 

def Randrearrangepics(path):
	'''This function creates a folder myRandPath and randomly rearrange
	the pics in the folder in the folder'''
	
	mypath=path
	count=0
	if os.path.isdir(path+"/myRandPath")==False:
                os.mkdir(path+"/myRandPath")
	else:
		 shutil.rmtree(path+"/myRandPath")
		 os.mkdir(path+"/myRandPath")
	file_arr=os.listdir(mypath)
	random.shuffle(file_arr)
	for pic in file_arr:
		if '.jpg' in pic:
			img=cv2.imread(mypath+'/'+pic)
			cv2.imwrite(path+"/myRandPath/%d.jpg" %count, img)
			count=count+1

def Splitpicstotesttrain(path, percent):
	'''This function creates a folder myTestPath and myTrainPath and put the test and train
	split into the myTestPath and myTrainPath. Percent is the amount of the test dataset to 
	train dataset'''
	
	mypath=path
	count=0
	per=percent/100.0
	print per
	if os.path.isdir(path+"/myTestPath")==False and os.path.isdir(path+"/myTrainPath")==False:
                os.mkdir(path+"/myTestPath")
		os.mkdir(path+"/myTrainPath")
	else:
		shutil.rmtree(path+"/myTestPath")
		shutil.rmtree(path+"/myTrainPath")
		os.mkdir(path+"/myTestPath")
		os.mkdir(path+"/myTrainPath")
	file_arr=os.listdir(mypath)
	random.shuffle(file_arr)
	file_size=(len(file_arr))*per
	for pic in file_arr:
		if '.jpg' in pic:
			img=cv2.imread(mypath+'/'+pic)
			if count<=file_size:	
				cv2.imwrite(path+"/myTestPath/"+pic, img)
			else:
				cv2.imwrite(path+"/myTrainPath/"+pic, img)
		count=count+1

if __name__=="__main__":
	#Getpics('/home/deola/Bottle_classify/RGB_Boy')
	#Cutsomepics('/home/deola/Bottle_classify/RGB_Boy', 10)
	#Randrearrangepics('/home/deola/Bottle_classify/RGB_Boy')
	Splitpicstotesttrain('/home/deola/Bottle_classify/RGB_Boy', 10)
