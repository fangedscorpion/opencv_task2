import cv2 # imports the openCV library
import numpy as np
from matplotlib import pyplot as plt # Imports the plotting 

Y_MAX = 540 # Global size of the output image
X_MAX = 960

img = cv2.imread('img5.jpg') 
rows,cols,ch = img.shape

pts1 = np.float32([[1030,202],[3226,269],[1236,2233],[3425,1825]])
pts2 = np.float32([[0,0],[X_MAX,0],[0,Y_MAX],[X_MAX,Y_MAX]]) # This warps to the new position maxed at the 

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(X_MAX,Y_MAX))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv2.imwrite('rotated_and_cropped_image_chas_frick.jpg',dst)