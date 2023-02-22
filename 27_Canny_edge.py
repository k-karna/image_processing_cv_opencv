"""
Canny Edge Detection is most popular. 
It is three step process:
1. Blur the image to reduce noise
2. Compute Sobel gradients in X and Y direction to suppress the edges where
nonmaximan is calculated
3. Determine whether a pixel in "Edge-like" or not by applying
hysteresis thresholding. 


However, cv2.canny() function encapsulates all these steps
"""

import cv2
import numpy as np

#load an image
image = cv2.imread("images/sudoku.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Blurred Image",image)

#Canny edge detection
canny = cv2.Canny(image, 50,170)
cv2.imshow("Canny Edges", canny)
cv2.waitKey(0)