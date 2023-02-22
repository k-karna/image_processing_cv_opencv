'''
There's no special function in OpenCV for cropping. 
We use Numpy slicing to crop the image
'''

from __future__ import print_function
import cv2
import numpy as np

#load image
image_path = "images/zebra.jpg"
image = cv2.imread(image_path)
cv2.imshow("Original Image",image)

#crop the image to get only the face
croppedImage = image[0:250,0:200]
cv2.imshow("Cropped Image", croppedImage)
cv2.waitKey(0)