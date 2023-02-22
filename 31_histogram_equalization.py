import cv2
import numpy as np
from matplotlib import pyplot as plt 

#Read an image and convert it into grayscale
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Origianal Image",image)

#calculate histogram
hist = cv2.calcHist([image],[0],None, [256],[0,255])

#plot histogram
plt.title("Grayscale Histogram of Original Image")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.show()

equalizedImage = cv2.equalizeHist(image)
cv2.imshow("Equalized Image", equalizedImage)

#calculate the histogram of the original image
histEqualized = cv2.calcHist([equalizedImage],[0],None,[256],[0,255])
plt.title("Grayscale Histogram of Equalized Image")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(histEqualized)
plt.show()
cv2.waitKey(0)