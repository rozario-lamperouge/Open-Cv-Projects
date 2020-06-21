import cv2
import numpy as np 
import time

img = cv2.imread("rms.png",-1)
bg = cv2.imread("rm.png",-1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask1+mask2

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
mask = cv2.dilate(mask,np.ones((3,3),np.uint8),iterations = 1)
mask2 = cv2.bitwise_not(mask)

res1 = cv2.bitwise_and(bg,bg,mask=mask)
res2 = cv2.bitwise_and(img,img, mask=mask2)
final_output = cv2.addWeighted(res1,1,res2,1,0)

cv2.imshow("mask",final_output)

cv2.waitKey(0)
cv2.destroyAllWindows()