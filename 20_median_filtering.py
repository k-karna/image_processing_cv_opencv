'''
"Salt and Pepper Noise" => Contains random occurences of black and white pixels"
'''

"""
Median Blurring => A technique to reduce salt-pepper-noise
In median blurring, instead of central value of kernel,
it takes the median of the surrounding pixels. 
"""

import cv2
import numpy as np

#load the image
brainImage = cv2.imread("images/brain.jpg")
cv2.imshow("Original noisy image",brainImage)

#Median Filtering for noise reduction
blurredImage3 = cv2.medianBlur(brainImage,3)
cv2.imshow("Blurred brain by 3x",blurredImage3)

#Median Filtering for noise reduction with kernel 5
blur5 = cv2.medianBlur(brainImage,5)
cv2.imshow("Blurred brain by 5x",blur5)
cv2.waitKey(0)