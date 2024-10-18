# intro 
# how to load/show images in opencv
# how to read vides in opencv.
# how to start and read camr..
# frames rescaling/ resize

import cv2

img = cv2.imread("images/cat.jpeg")

cv2.imshow("this is my cat image", img)

cv2.waitKey(0)
