## Function to crop the center of Images
import numpy as np
import cv2

def centeredCrop(img):
	height =  np.size(img,0)
	width =  np.size(img,1)
  
  ##set new Width and Height size:
	new_width= (int)(0.15*width) 
	new_height=(int)(0.15*height)

	left = np.ceil((width - new_width)/2.)
	top = np.ceil((height - new_height)/2.)
	right = width - np.floor((width - new_width)/2.)
	bottom = height - np.floor((height - new_height)/2.)
	cImg = img[top:bottom, left:right]
	return cImg
	
Image=cv2.imread("Image.jpg")
cropCenter=centeredCrop(Image)
cv2.imshow('ImageWindow',cropCenter)
cv2.waitKey(0)
cv2.destroyAllWindows()
