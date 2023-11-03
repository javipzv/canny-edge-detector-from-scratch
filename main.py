from canny import CannyEdgeDetector
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from scipy import signal

img = cv2.imread('example_inputs/persona.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
borders = CannyEdgeDetector(img=img_rgb, gaussian_size=9, sigma=2, min_threshold=40, max_threshold=60)

plt.imshow(borders, cmap='gray')
plt.show()