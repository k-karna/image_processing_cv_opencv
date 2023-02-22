"""
Histogram Of Oriented Gradients(HOG) describe the structural shape and 
appearance of an object in am image. HOG computes the occurrences of
gradient orientation in localized portions of the image. 

HOG works in 5 stages:
1. Global Image Normalization to reduce the influence of illumination effects with any of the following methods: 
    a. gamma - by applying log(p) to pixel value p
    b. square root normalization - square root of p
    c - variance normalization - First, we compute the mean(u) and standard deviation(sd)
        the Tp = (p-u)/sd

2. Compute the gradient image in x and y:
    If the gradients in the X directions are Gx and gradients in Y direction are Gy, 
    the gradient magnitude
        |G|  =  

"""
import cv2 
import numpy as np 
from skimage import feature as sk 

image = cv2.imread("images/elon.jpg")
#resizing
image = cv2.resize(image,(int(image.shape[0]/3),int(image.shape[1]/3)))

#HOG calculation
(HOG, hogImage) = sk.hog(image, orientations=9, pixels_per_cell=(8,8),cells_per_block=(2,2),
visualize=True,transform_sqrt=True,block_norm="L2-Hys",feature_vector=True, multichannel=True)

# orientation: The number of orientation bins. default 9
# pixels_per_cell : number of pixel in each cell as a tuple. Default (8,8)
# cells_per_block number of cells in ech block, as a tuple Default (3,3)
# block_norm : block normalization method L1, L1-sqrt, L2, L2-Hys
# visualize : If TRUE. returns HOG image
# transform_sqrt : apply power law compression to normalize the image before processing 
# feature_vector : If TRUE returns the output data as a feature vector 
# multichannel : If TRUE indicates input image contains multichannels  

print("image dimension: ", image.shape)
print("Feature vector dimension: ", HOG.shape)

#showing the original and HOG images
cv2.imshow("Original Image", image)
cv2.imshow("HOG Image", hogImage)
cv2.waitKey(0)