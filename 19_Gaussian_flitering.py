"""
Guassian kernel takes
1. height
2. width
3. standard deviation in X and Y directions
"""
'''
1. If only 'sigmaX' is specified, 'sigmaY' is taken as same as 'sigmaX'
2. If both are taken as zero, the standard deviations are calculated from the kernel size
3. cv2.getGaussianKernel(), atucalculate S.D. 
'''

import cv2
import numpy as np

#load the image
park = cv2.imread("images/park.jpg")
cv2.imshow("Original Image", park)
cv2.waitKey(0)

#Gaussian blurring with 3x3 kernel and 0 for sd to calculate from kernel
GaussianFiltered = cv2.GaussianBlur(park,(5,5),0)
cv2.imshow("Gaussian Blurred Image", GaussianFiltered)
cv2.waitKey(0)