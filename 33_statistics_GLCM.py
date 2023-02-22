"""
GLCM is used to calculate below discussed statistics

CONTRAST:       Measures the local variations in the GLCM
CORRELATION:    Measure the joint probability occurence of the specified pixel pairs 
ENERGY:         Provides the sum of squared elements in the GLCM. Also, known as uniformity or the sngularr second momment. 
#HOMOGENITY:    Measures the closeness of the distribution of elements in the GLCM to the GLCM diagonal 


"""

import cv2 
import skimage.feature as sk 
import numpy as np 

#to suppress warning messages:
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#read an image from the disk and convert it into grayscale 
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#calculate GLCM of the grayscale image
glcm = sk.greycomatrix(image,[2],[0,np.pi/2])

#calculate Contrast
contrast = sk.greycoprops(glcm)
print("Contrast: ",contrast)

#calculate 'dissimilarity'
dissimmilarity = sk.greycoprops(glcm,prop='dissimilarity')
print("Dissimilarity: ",dissimmilarity)

#calculate 'homogenity'
homogenity = sk.greycoprops(glcm, prop='homogeneity')
print("Homogeneity", homogenity)

#calculate 'ASM'
asm = sk.greycoprops(glcm, prop='ASM')
print("ASM: ",asm)

#calculate 'energy'
energy = sk.greycoprops(glcm, prop='energy')
print("Energy: ", energy)

#calculate 'correlation'
correlation = sk.greycoprops(glcm, prop='correlation')
print("Correlation: ",correlation)