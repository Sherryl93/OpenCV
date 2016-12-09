
import numpy as np
import cv2
import os

imagePath='F:/MMSL/XMLBoundingBox/shuttle_bus_recording/frameOut_canon20151027_CPEV(birdView)/JPEGImages'
dataFiles_image=[(x[2]) for x in os.walk(imagePath)]
dataFiles_image=dataFiles_image[0]
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('F:/MMSL/XMLBoundingBox/shuttle_bus_recording/frameOut_canon20151027_CPEV(birdView)/output_square_degree90_LBP_7090.avi',fourcc, 30.0, (720,480))

#output_path='F:/MMSL/XMLBoundingBox/shuttle_bus_recording/frameOut_canon20151027_CPEV(birdView)/pos_res_ver'
#stopLine_cascade=cv2.CascadeClassifier('F:/MMSL/Adaboost/large_stopline/Train_Cascade_2/cascade.xml')
stopLine_cascade=cv2.CascadeClassifier('F:/MMSL/XMLBoundingBox/shuttle_bus_recording/frameOut_canon20151027_CPEV(birdView)/cascade_square_degree90_LBP.xml')

dir_im_results='F:/MMSL/XMLBoundingBox/shuttle_bus_recording/frameOut_canon20151027_CPEV(birdView)/Results_degree90_LBP_7090/'
i=0
for i in range(0,len(dataFiles_image)):
	#flag=1 ## flag for cropped image per frame
	imageName=imagePath+'/'+dataFiles_image[i]
	im_name=dataFiles_image[i]
	im_name=im_name[1:len(im_name)-4]
	img=cv2.imread(imageName)
	#stopLine_res=stopLine_cascade.detectMultiScale(img,1.1, 3, 0, (84, 84), (88, 88))
	stopLine_res=stopLine_cascade.detectMultiScale(img,1.1, 3, 0,(70, 70), (90, 90))
	#stopLine_res=stopLine_cascade.detectMultiScale(img,1.1, 3, 0,(150,70),(300,140))
	if len(stopLine_res):
		for(x,y,w,h) in stopLine_res:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.imwrite(dir_im_results+dataFiles_image[i],img)
	out.write(img)
	cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
	i+=1
# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
