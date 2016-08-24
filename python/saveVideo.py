#To Capture Video using webcam and save it in MP4 format with python and Open CV
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width=cap.get(3)
height=cap.get(4)

out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,180)
        # write the flipped frame
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
