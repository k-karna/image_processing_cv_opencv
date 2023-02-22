import cv2
from cv2 import resize
import numpy as np

image_path1 = "images/cat1.jpg"
image_path2 = "images/cat2.jpg"

image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

#resize the two images of same dimension for being abler to substaction

resizedImage1 = cv2.resize(image1,(int(400*image1.shape[1]/image1.shape[0]),400),interpolation=cv2.INTER_AREA)
resizedImage2 = cv2.resize(image2,(int(400*image2.shape[1]/image2.shape[0]),400),interpolation=cv2.INTER_AREA)

cv2.imshow("Cat 1", resizedImage1)
cv2.imshow("Cat 2", resizedImage2)

#Substract image 1 from 2
sub = cv2.subtract(resizedImage2,resizedImage1)
cv2.imshow("Diff Cat 1 from Cat 2",sub)
cv2.waitKey(0)

#substract image 2 from 1
sub_image = cv2.subtract(resizedImage1, resizedImage2)
cv2.imshow("Diff Cat 2 from Cat 1", sub_image)
cv2.waitKey(0)

#Numpy Substraction Cat 2 from Cat 1
subs_im = resizedImage2 - resizedImage1
cv2.imshow("Numpy Substracted Image", subs_im)

#A constant substraction
subs_img = resizedImage1 - 50
cv2.imshow("Constant substracted from Cat 1", subs_img)
cv2.waitKey(0)
