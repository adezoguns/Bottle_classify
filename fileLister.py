import os
import cv2

arr=[]

def Getpics(path):
	mypath=path
	if os.path.isdir(path+"/Mypath")==False:
		os.mkdir(path+"/Mypath")
	file_arr=os.listdir(mypath)
	for pic in file_arr:
		if '.jpg' in pic:
			arr.append(pic)
			img=cv2.imread(mypath+'/'+pic)	
			cv2.imwrite(path+"/Mypath/"+pic, img) 

if __name__=="__main__":
	Getpics('/home/deola/Bottle_classify/RGB_Boy')
