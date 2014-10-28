import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('checkerboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,3,0.05,10)
corners = np.int0(corners)


for i in corners:
    x,y = i.ravel()
    print x,y
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()