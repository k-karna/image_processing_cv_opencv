import cv2
from matplotlib import image
import numpy as np

natureImage = cv2.imread("images/nature.jpg")

#split the image into component colors

(b,g,r) = cv2.split(natureImage)

#show the blue image
cv2.imshow("Blue image",b)
#show the green image
cv2.imshow("Green image",g)
#show the red image
cv2.imshow("Red Image",r)

cv2.waitKey(0)