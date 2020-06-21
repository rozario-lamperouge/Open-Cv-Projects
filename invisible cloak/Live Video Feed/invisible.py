import cv2
import numpy as np 
import time

cap = cv2.VideoCapture(1)

time.sleep(3)

bg = 0
count = 0

for i in range(30):
	ret, bg = cap.read()

while (cap.isOpened()):
	ret , img = cap.read()
	if not ret:
		break
	count += 1

	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	# generate mask to detect red color
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)

	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv, lower_red, upper_red)

	mask = mask1 + mask2

	# redifining my mask
	mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
	mask = cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=2)
	mask2 = cv2.bitwise_not(mask)

	#result
	res1 = cv2.bitwise_and(bg,bg,mask=mask)
	res2 = cv2.bitwise_and(img, img, mask=mask2)
	output = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow("Frame", output)
	k = cv2.waitKey(10)
	if k ==27:
		break