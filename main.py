from canny import CannyEdgeDetector
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from scipy import signal

img = cv2.imread('example_inputs/kid.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
borders = CannyEdgeDetector(img=img_rgb, gaussian_size=11, sigma=2.5, min_threshold=10, max_threshold=25)

plt.imshow(borders, cmap='gray')
plt.show()

cv2.imwrite('example_outputs/kid_borders.jpg', borders)