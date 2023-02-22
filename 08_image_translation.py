from __future__ import print_function
import cv2
import numpy as np

#load image
image_path = "images/soccer_in_green.jpg"
image = cv2.imread(image_path)

#Define translation matrix
#translation matrix defines the direction and amount of movement
translationMatrix = np.float32([[1,0,50],[0,1,60]])

#Move the image
#warpAffine is the function that actually does the movement
movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
cv2.imshow("Moved Image", movedImage)
cv2.waitKey(0)