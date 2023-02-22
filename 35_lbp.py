"""
Local Binary Patterns (LBP) ia a type of feature descriptor for image texture classification
It works as follows:
1. For every pixel in the image, we cmpare the pixel values of the surrounding pixels. If the value of the 
surrounding pixel is less than the central pixel, mark it to 0; otherwise 1. 
2. Starting from any of the neighbor's pixels and going in any direction, we assemble 
the sequence of 0s and 1s to make an 8-bit binary number. 
3. For each pixel in the image, we repeat the previous step to obtain the pixel values based on the neighbours' pixel 
4. Weh all pixels are done, we arrange the pixel values in an LBP array 
5. Finally, we calculate a histogram over the LBP array. This histogram is taken as an LBP feature vector. 

"""

import cv2 
import numpy as np 
from skimage import feature as sk 
from matplotlib import pyplot as plt 

image = cv2.imread("images/elon.jpg")
image = cv2.resize(image, (int(image.shape[0]/5),int(image.shape[1]/5)))
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#calculate Histogram of original image and plot it 
originalHist = cv2.calcHist(image, [0], None, [256],[0,256])

plt.figure()
plt.title("Histogram of Original Image")
plt.plot(originalHist, color='r')

#calculate LBP image and histogram over the LBP, then plot the histogram 
radius = 3 
points = 3*8
#LBP calculation 
lbp = sk.local_binary_pattern(image, points, radius, method='default')
lbpHist, _ = np.histogram(lbp,density=True, bins=256, range=(0,256))

plt.figure()
plt.title("Histogram of LBP Image")
plt.plot(lbpHist, color='g')
plt.show()

#showing the original and LBP images
cv2.imshow("Original image",image)
cv2.imshow("LBP Image",lbp)
cv2.waitKey(0)