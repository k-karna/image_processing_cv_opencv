"""
THRESHOLDING is a technique of Image Binaryzation
-> converting grayscale image into binary"""

"""
Simple Thresholding -> 1. Any value above threshold =>255 2. Any value below threshold =>0
Inverse Thresholding => 1. Any value above threshold => 0 2. Any value below threshold => 255

"""

import cv2
import numpy as np

#Load the image
image = cv2.imread("images/scanned_doc.jpg")

#convert the image to grayscale
image =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original grayscale image",image)

#binarize the image using threshold
(T, bin_im) = cv2.threshold(image,60,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Receipt",bin_im)

#binarize with inverse thresholding
(Ti,inv_bin) = cv2.threshold(image,60,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Binary Receipt", inv_bin)

cv2.waitKey()