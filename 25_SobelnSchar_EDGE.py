"""
EDGE DETECTION involves a set of methods to find points
in an image where the brightness of pixels changes

Two Method: 1. Finding gradients 2. Canny Edge Detection
"""
import cv2
import numpy as np

#load an image
image  = cv2.imread("images/sudoku.png")
cv2.imshow("Original Image",image)
#converting image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#bilateral filtering
image = cv2.bilateralFilter(image,5,50,50)
cv2.imshow("Blurred image",image)

#Sobel gradient detection

sobelx =cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
#transition from black-to-white is considered positive slope
#transition form white-to-black is considered negative slope
# 8 bit unsigned integer cannot hold negative number
# Therefore, 64-bit Float, so that we wont lose gradients when 
# the transition happen from white-to-black

#If we want to calculate gradients in the X direction, we use 1
# fourth arguement - whether to calculate gradients in Y direction,
# 1 means 'YES' 0 means 'NO'
# ksize means kernel size i.e., of 5x5

sobelx = np.uint8(np.absolute(sobelx))
#This simply takes the absolute value of the gradients and converts then backk
#to 8-bit unsigned integers. 
sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
sobely = np.uint8(np.absolute(sobely))

cv2.imshow("Sobel X",sobelx)
cv2.imshow("Sobel Y",sobely)

#Schar gradient detection by passing ksize = -1, to Sobel function
scharx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=-1)
scharx = np.uint8(np.absolute(scharx))
schary = cv2.Sobel(image,cv2.CV_64F,0,1,ksize =-1)
schary = np.uint8(np.absolute(schary))
cv2.imshow("Schar X",scharx)
cv2.imshow("Schar Y:",schary)

cv2.waitKey(0)