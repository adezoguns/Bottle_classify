import os
import cv2
import shutil
from random import randint

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
	'''This function creates a flolder myRandPath and randomly rearrange
	the pics in the folder in the folder'''
	
	mypath=path
	if os.path.isdir(path+"/myRandPath")==False:
                os.mkdir(path+"/myRandPath")
	else:
		 shutil.rmtree(path+"/myRandPath")
		 os.mkdir(path+"/myRandPath")
	file_arr=os.listdir(mypath)
	for pic in file_arr:
		if '.jpg' in pic:
			arr.append(pic)
			img=cv2.imread(mypath+'/'+pic)
			num=randint(0, len(file_arr))	
			cv2.imwrite(path+"/myRandPath/%d.jpg" %num, img)


if __name__=="__main__":
	#Getpics('/home/deola/Bottle_classify/RGB_Boy')
	#Cutsomepics('/home/deola/Bottle_classify/RGB_Boy', 10)
	Randrearrangepics('/home/deola/Bottle_classify/RGB_Boy')
	
