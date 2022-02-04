import numpy as np
import cv2
import math
from scipy.ndimage.filters import generic_filter

image = cv2.imread('/home/thanh/Pictures/vegabond.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('/home/thanh/Pictures/edge_s1.jpg', gray)

x = gray.astype('float')
x_filt = generic_filter(x, np.std, size = 7) 
cv2.imwrite('/home/thanh/Pictures/edge_s2.jpg', x_filt)

x_filt[x_filt < 20] = 0
cv2.imwrite('/home/thanh/Pictures/edge_s3.jpg', x_filt)

maxv = np.max(x_filt)
print(maxv)

x_filt = x_filt * 2.5
cv2.imwrite('/home/thanh/Pictures/edge_s4.jpg', x_filt)
