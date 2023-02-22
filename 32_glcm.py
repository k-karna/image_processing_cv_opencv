"""
Gray-Level Co-occurence Matrix(GLCM) is the distribution of 
simlutaneously occuring pixels values with a given offset. An offset is the position(distance and direction) of
adjacent pixels. 
GLCM provides information on spatial relationships over an image. 

"""


import cv2 
import skimage.feature as sk #OpenCV doesn't directly offer function to calculate GLCM
import numpy as np 

#Read an image from the dist and convert it into grayscale 
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Calculate GLCM of the grayscale image
glcm = sk.greycomatrix(image,[2],[0,np.pi/2])

# greycomatrix(image, distance, angles, levels, symmetric, normed)
# distances: List of pixel-pair distance offsets 
# angles : List of angles between the pair of pixels. Angle should be in radian, not degree 
# levels : (optional) meant for 16-bit pixel values
# symmetric: (optional) takes Boolean Value. TRUE means the output matrix will be symmetric
# normed : (optional) takes Boolean value. TRUE means the each output matrix in normalized by diving with total number of accumulated co-occurence

print(glcm)