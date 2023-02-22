"""
Side effects of Averaging Filtering, 
GAussian Filtering, & Median Filtering is we
lose the edges in the image

Bilateral Blurring preserves it, by taking two
Gaussian distributions to perform the calculation. 
"""

"""
First Gaussian function considers the spatial neighbours(pixels in x & y space)
Second Gaussian function considers the pixel intensity of the neighbuoring pixels. 

This results: only those pixels that are of similar intesity to the cenrtal pixel are
considered for blurring, leaving EDGES INTACT. 

=> It is slower than rest of blurring, however superior. 
"""

import cv2

#load a noisy image
n_im = cv2.imread("images/park.jpg")
cv2.imshow("Original Image",n_im)

#Bilateral Filter with kernel 5
filter5 = cv2.bilateralFilter(n_im,5,150,50)
cv2.imshow("Blurred image by 5x",filter5)

#Bilateral Filter with kernel 7
filter7 = cv2.bilateralFilter(n_im,7,160,60)
cv2.imshow("Blurred image by 7x",filter7)

cv2.waitKey(0)