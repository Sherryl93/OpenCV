#To Capture Video using webcam and save it in MP4 format with python and Open CV
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width=cap.get(3)
height=cap.get(4)
width=int(width)
height=int(height)


out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (width,height))
##If no module VideoWriter_fourcc found use this instead:
#out = cv2.VideoWriter('output.mp4',cv2.cv.CV_FOURCC(*'MP4V'), 30.0, (width,height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  #to exit the loop by pressing key "q"
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
