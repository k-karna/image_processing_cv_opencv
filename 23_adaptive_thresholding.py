"""
In this, the algorithm determines
the threshold for a pixel based in a smaill region around it.add()
"""

"""
AdaptiveThreshold function takes following arguements:
1. grayscale image
2. The maximum value
3. Method to calculate -> simple mean / Gaussian Mean
4. Binarization method -> Simple thresholding/inverse thresholding etc. 
5. Neighbourhood size to consider for calculating thresholds
6. A constant value that will be subtracted from threshold
"""


import cv2
import numpy as np

#load the image
image = cv2.imread("images/boat.jpg")
#convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Grayscale Image", image)

#Binarization using adptive threshodlign and simple mean

binarized = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
cv2.imshow("Binarized Image with Simple Mean",binarized)

#binarization using adaptive thresholding and Gaussian Mean
binarized = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,3)
cv2.imshow("Binarized Image with Gaussian Mean, and Inverse thresholding",binarized)
cv2.waitKey(0)