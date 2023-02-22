from __future__ import print_function
import cv2
import numpy as np
'''
There are two methods for adding images
1. SATURATED OPERATION (trimming) - In this operation, 230+30 = 255 
2. MODULO OPERATION - It performs, (230 +30) % 256 => 4
'''

'''
OpenCV -> saturated operation
Numpy -> modulo operation
'''

'''
cv2.weighted function works on the following formula: 
Result_Image = alpha * image_1 + beta * image_2 + Y

where, alpha = weight of image_1
        beta = weight of image_2
        Y = some constant
'''



image_path1 = "images/zebra.jpg"
image_path2 = "images/nature.jpg"

image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

#resize the two image to make them of same size before addition
resizedImage1 = cv2.resize(image1, (300,300), interpolation=cv2.INTER_AREA)
resizedImage2 = cv2.resize(image2, (300,300), interpolation=cv2.INTER_AREA)

#this is a simple addition of two images
resultant = cv2.add(resizedImage1, resizedImage2)

#Display these images to see the difference
cv2.imshow("Resized 1", resizedImage1)
cv2.waitKey(0)

cv2.imshow("Resized 2",resizedImage2)
cv2.waitKey(0)

#Resultant  Image with simple addition
cv2.imshow("Rsultant Image", resultant)
cv2.waitKey(0)

#this is the weighted addition of the two images
weightedImage = cv2.addWeighted(resizedImage1,0.7, resizedImage2,0.3,0)
cv2.imshow("Wegihted Image", weightedImage)
cv2.waitKey(0)

imageEnhanced = 255*resizedImage1
cv2.imshow("Enhanced Image", imageEnhanced)
cv2.waitKey(0)

arrayImage = resizedImage1 + resizedImage2
cv2.imshow("Array Image", arrayImage)
cv2.waitKey(0)