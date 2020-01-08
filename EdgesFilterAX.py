#pip3 install opencv-python
#pip3 install matplotlib

import cv2
import matplotlib.pyplot as plt

im = cv2.imread('input-image2.jpg')
edges = cv2.Canny(im,100,300)

plt.imshow(edges)
plt.show()
