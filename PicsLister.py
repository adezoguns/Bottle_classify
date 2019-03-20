import os
import cv2
import shutil
from random import randint
import random

arr=[]
arr1=[]
def getpics(path):

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
		if '.jpg' in pic or '.jpeg' in pic:
			arr.append(pic)
			img=cv2.imread(mypath+'/'+pic)	
			cv2.imwrite(path+"/myPath/"+pic, img) 

def change_jpeg_to_jpg(path):

	'''This code changes .jpeg to .jpg and put it in a directory
	called myPath'''

	mypath=path
	count=0
	if os.path.isdir(path+"/myPath")==False:
                os.mkdir(path+"/myPath")
	else:
		 shutil.rmtree(path+"/myPath")
		 os.mkdir(path+"/myPath")
	file_arr=os.listdir(mypath)
	for pic in file_arr:
		if '.jpg' in pic or '.jpeg' in pic:
			arr.append(pic)
			img=cv2.imread(mypath+'/'+pic)
			#img=cv2.resize(img,(300,300))	
			cv2.imwrite(path+"/myPath/Bottle%d" %count, img)
			count=count+1 


def cut_some_pics(path, numb):

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

def rand_rearrange_pics(path):
	'''This function creates a folder myRandPath and randomly rearrange
	the pics in the folder in the folder'''
	
	mypath=path
	count=0
	if os.path.isdir(mypath+"/myRandPath")==False:
                os.mkdir(mypath+"/myRandPath")
	else:
		 shutil.rmtree(mypath+"/myRandPath")
		 os.mkdir(mypath+"/myRandPath")
	file_arr=os.listdir(mypath)
	random.shuffle(file_arr)
	for pic in file_arr:
		if '.jpg' in pic:
			arr.append(pic)
	random.shuffle(arr)
	for pic in arr:
		img=cv2.imread(mypath+'/'+pic)
		cv2.imwrite(path+"/myRandPath/%d.jpg" %count, img)
		count=count+1

def split_pics_to_test_train(path, percent):
	'''This function creates a folder myTestPath and myTrainPath and put the test and train
	split into the myTestPath and myTrainPath. Percent is the amount of the test dataset to 
	train dataset'''
	
	mypath=path
	count=0
	per=percent/100.0
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
	for pic in file_arr:
		if '.jpg' in pic:
			arr.append(pic)
	random.shuffle(arr)
	file_size=(len(arr))*per
	print file_size, len(arr)
	for pic in arr:
		img=cv2.imread(mypath+'/'+pic)
		if count<=file_size:	
			cv2.imwrite(path+"/myTestPath/"+pic, img)
		else:
				cv2.imwrite(path+"/myTrainPath/"+pic, img)
		count=count+1

if __name__=="__main__":
	#get_pics('/home/deola/Bottle_classify/RGB_Boy')
	#cut_some_pics('/home/deola/Bottle_classify/RGB_Boy', 10)
	rand_rearrange_pics('/home/deola/Bottle_classify/RGB_Boy')
	#split_pics_to_test_train('/home/deola/Bottle_classify/RGB_Boy', 50)
