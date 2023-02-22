from __future__ import print_function
import cv2
import numpy

image_path = "images/marsrover.jpg"

#Read image from its path
image = cv2.imread(image_path)

#Access pixel at (0,0) location

(b, g, r) = image[0,0]
print("Blue, Green and Red values at (0,0): ",format((b,g,r)))

#Manipulate pixels and show modified image
image[0:100, 0:100] = (128,0,0)
cv2.imshow("Modified Image: ",image)
cv2.waitKey()