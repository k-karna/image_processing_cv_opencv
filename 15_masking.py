import cv2
import numpy as np

#load an image
nature = cv2.imread("images/nature.jpg")
cv2.imshow("Original Image", nature)

#create a rectangular mask
maskImage = cv2.rectangle(np.zeros(nature.shape[:2], 
dtype="uint8"), (50,50),(int(nature.shape[1])-50, 
int(nature.shape[0]/2)-50),(255,255,255),-1)

cv2.imshow("Mask Image", maskImage)
cv2.waitKey(0)

#using bitwise_and operation perform masking. 
#
masked = cv2.bitwise_and(nature, nature,maskImage)
cv2.waitKey(0)