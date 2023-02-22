"""
Contours are curves joining continous points of the same intensity 
It is usef for object identification, face detection, recognition. 

We need these steps:
1. Convert the image to grayscale
2. Binarize the image by any of the thresholding methods. 
3. Apply canny edge detection
4. Use findContours() method to find all the contours 
5. Use drawContourS() to draw if needed. 

"""

import cv2
import numpy as np

image = cv2.imread("images/sudoku.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Blurred Image", image)

#Binarize the image
(T, binarized) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("Binarized Image",binarized)

#Canny function for edge detection
canny = cv2.Canny(binarized, 0, 255)
cv2.imshow("Canny Edge", canny)

(contours, hierarchy) = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.RET_EXTERNAL retrieves out most contours only. 
#cv2.RET_LIST retrieves all contours
# cv2. RET_COMP and cv2.RET_TREE retrieves hierarchical contours

#cv2.CHAIN_APPROX_SIMPLE removes the redundant points and compresses the contour
#saves memory
#cv2.CHAIN_APPROX_NONE stores all points of the contour - more memory

print("Number of contours determined are", format(len(contours)))

copiedImage = image.copy()
cv2.drawContours(copiedImage, contours, -1,(0,255,0),2)
# Third argument is index of contour to be drawn
# to draw first contour, pass 0
# to draw second contour, pass 1
# to draw all contours, pass -1

#fourth arguement is color
#fifth is thickness
cv2.imshow("Contours",copiedImage)
cv2.waitKey(0)