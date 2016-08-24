#To save Video in MP4 format using Open CV
import numpy as np
import cv2

cap = cv2.VideoCapture(2)
width=cap.get(3)
height=cap.get(4)
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (640,480))
frame_counter=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame_counter+=1
        frame = cv2.flip(frame,180)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
