import cv2
import numpy as np

#load an image
image = cv2.imread("images/sudoku.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image =cv2.bilateralFilter(image, 5, 50, 50)
cv2.imshow("Blurred Image", image)

#laplacian function for edge detection
laplace = cv2.Laplacian(image, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))

cv2.imshow("Laplacian Edges",laplace)
cv2.waitKey(0)