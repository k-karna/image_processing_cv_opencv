"""
OTSU'S METHOD determines an optimal global threshold value from the
image histogram. 

In OTSU's binarization, we pass <threshold>+cv2.THRESH_OTSU

"""

import cv2
import numpy as np
from sklearn.preprocessing import binarize

#load the image
image = cv2.imread("images/boat.jpg")
#converting image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original grayscale image", image)

#Binarize using thresholding
(T,binarized) = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Threshold valye with OTSU binarization: ", T)
cv2.imshow("Binarised: ",binarized)

#binarized using inverse thresholding
(Ti,binarized) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print("Threshold value with OTSU binarization:",Ti)
cv2.imshow("Binarised",binarized)
cv2.waitKey(0)