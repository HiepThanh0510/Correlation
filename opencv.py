import numpy as np 
import cv2 as cv

#load image in grayscale mode
image = cv.imread('/home/thanh/Pictures/vegabond.jpg', 0)

#create kernel 
kernel = np.ones((5, 5), np.float32) / 25.0

#compute mean for each pixel 
dst = cv.filter2D(image, cv.CV_8U, kernel)

#show image
cv.imshow('image', image)
cv.imshow('dst', dst)

#wait
cv.waitKey(0)
cv.destroyAllWindows()