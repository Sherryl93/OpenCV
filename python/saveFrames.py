## To save as frame as pictures from Video capture by webcam
import cv2

cap = cv2.VideoCapture(0)

frame_counter=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv2.imwrite("frame%02d.jpg"%frame_counter,frame)
        frame_counter+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
