"""
A small portion of the window, K*K pixel
is taked called "sliding window"
or "convolutional kernel"
or "kernel"

=> Larger the kernel size, blurrier the image
"""
import cv2
from cv2 import blur
import numpy as np

#load the image
park = cv2.imread("images/nature.jpg")
cv2.imshow("Original Park Image", park)
cv2.waitKey(0)

#define the kernel
kernel = (3,3)
blurred3 = cv2.blur(park, kernel)
cv2.imshow("3x blurred Image", blurred3)
cv2.waitKey(0)

blurred5 = cv2.blur(park,(5,5))
cv2.imshow("5x blurred image", blurred5)
cv2.waitKey(0)

blurred7 = cv2.blur(park, (7,7))
cv2.imshow("7xblurred image",blurred7)
cv2.waitKey(0)