
##########################################################################################################
## Objective: Classify using Adaboost Cascade Classifier in real time        				##
## Input: Images/frames; cascade.xml                                                                    ##
## Output: Video with contain detected object                                                           ##
##########################################################################################################
import numpy as np
import cv2
import os

imagePath='../../' #Folder contain Images
dataFiles_image=[(x[2]) for x in os.walk(imagePath)]
dataFiles_image=dataFiles_image[0]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../output.avi',fourcc, 30.0, (720,480))

cascade=cv2.CascadeClassifier('../cascade.xml')

dir_im_results='../..'
i=0
for i in range(0,len(dataFiles_image)):
	imageName=imagePath+'/'+dataFiles_image[i]
	im_name=dataFiles_image[i]
	im_name=im_name[1:len(im_name)-4]
	img=cv2.imread(imageName)
	cascade_results=cascade.detectMultiScale(img,1.1, 3, 0,(70, 70), (90, 90))
	if len(cascade_results):
		for(x,y,w,h) in cascade_results:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	out.write(img)
	cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
	i+=1
	
# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
