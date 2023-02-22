from __future__ import print_function
import cv2
import numpy as np

#load image
image_path = "images/zebra.jpg"

image = cv2.imread(image_path)
#get the image share which returns height, weight, width,
#and channels as a tuple. Calculate the aspect ratio. 

(h, w) = image.shape[:2]
aspect = w / h

#lets resize the image to decrease height by half of the
#original image. 
height = int(0.5 * h)
width = int(height * aspect)

#New Image dimension as a tuple
dimension = (height, width)
resizedImage = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Image", resizedImage)

#resize using x and y factors

resizedWithFactors = cv2.resize(image,None, fx=1.2, fy = 1.2,interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized with factors",resizedWithFactors)
cv2.waitKey(0)

