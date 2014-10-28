import cv2 # imports the openCV library
import numpy as np

img = cv2.imread('img5.jpg')  # Read the image 
rows,cols,ch = img.shape

checkerboard = img[64:330,875:1182]

cv2.imwrite('checkerboard.jpg',checkerboard)
