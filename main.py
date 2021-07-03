import cv2
import numpy as np
import time

capture_img=cv2.VideoCapture(0)
time.sleep(3)
for i in range(30):
    ret,background=capture_img.read()

background=np.flip(background,axis=1)

capture_img=cv2.VideoCapture(0)

while(capture_img.isOpened()):
    return_val,img=capture_img.read()
    if return_val:
        img=np.flip(img,axis=1)

        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        lower_red=np.array([0,120,70])
        upper_red=np.array([10,255,255])
        mask1=cv2.inRange(hsv, lower_red, upper_red)

        lower_red=np.array([170,120,70])
        upper_red=np.array([180,255,255])
        mask2=cv2.inRange(hsv,lower_red, upper_red)

        mask1+=mask2
        kernel=np.ones((5,5),np.uint8)
        mask=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernel)
        
        img[np.where(mask==255)]=background[np.where(mask==255)]

        cv2.imshow("Harry Potter's Magic Cloack", img)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
capture_img.release()
cv2.destroyAllWindows()
