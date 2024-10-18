import numpy as np 
import cv2

box = np.zeros((500, 500, 3), dtype = 'uint8')

# box[ : ] = 226, 255, 5
# [start_row : end_row, start_col, end_col]
# box[100:300, 100:300] = 226, 255, 5

box[50:400, 300:400] = 226, 255, 5

cv2.imshow("black box", box)
cv2.waitKey(0)