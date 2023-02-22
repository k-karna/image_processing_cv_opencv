import cv2 
import numpy as np
from matplotlib import pyplot as plt 

#read a color image
image = cv2.imread("images/nature.jpg")
cv2.imshow("Original Image", image)

colors = ("blue","green","red")
#calculate histogram
for i, color in enumerate(colors):
    hist = cv2.calcHist([image],[i], None, [32],[0,256])
    #plot the histogram
    plt.plot(hist,color=color)

plt.title("RGB Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.show()
cv2.waitKey(0)