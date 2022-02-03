#Median
import numpy as np
import cv2

image_1 = cv2.imread('/home/thanh/Pictures/image_noise.jpg')
image_2 = cv2.medianBlur(image_1, 5) #kernel 5x5

#show images
cv2.imshow('image_1', image_1)
cv2.imshow('image_2', image_2)

#wait 
cv2.waitKey(0)
cv2.destroyAllWindows()
