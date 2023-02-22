from __future__ import print_function 
import cv2
import numpy as np

#load image
image_path = "images/zebra.jpg"
image = cv2.imread(image_path)
(h,w) = image.shape[:2]

#define translation matrix
center = (h//2, w//2)
angle = -45 #negative value rotate image clockwise, positive value rotate image anti-clockwise
scale = 1.0 #size of the image in comparison with origianl image, 1.0 means same size

rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)
#getRotationMatrix2D takes 1) a tuple representing point from where rotation should take place,
#  2) The angle of rotation
# 3) Resizing scale value 

#rotate the image

rotatedImage = cv2.warpAffine(image,rotationMatrix,(image.shape[1],image.shape[0]))

cv2.imshow("Rotated Image: ", rotatedImage)
cv2.waitKey(0)