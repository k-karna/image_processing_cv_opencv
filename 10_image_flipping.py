from __future__ import print_function
import cv2
import numpy as np

#load image
image_path = "images/zebra.jpg"
image = cv2.imread(image_path)

#flip horizontally
flippedhorizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally, ", flippedhorizontally)
cv2.waitKey(-1)

#flip vertically
flippedVertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flippedVertically)
cv2.waitKey(-1)

#flip horizontally and then vertically
flippedHV = cv2.flip(image, -1)
cv2.imshow("Flipped H and then Vert.",flippedHV)
cv2.waitKey(-1)

# 0 means VERTICAL flip
# 1 means HORIZONTAL flip
# -1 means first flip horizontally and then vertically