import cv2
import numpy as np
from matplotlib import pyplot as plt 

#Read imaege & convert it to grayscale
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

#calculate histogram
hist = cv2.calcHist([image], [0], None, [256],[0,255])
#calcHist takes array, therefore we need to wrap image in array
#[0] denotes we want to calcuulate the histogram of the zeroth color channel
# None -> we do not want any masking
# 

#plot histogram
plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.show()
cv2.waitKey(0)