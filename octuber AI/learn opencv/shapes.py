import cv2
import numpy as np

img = np.zeros((500, 500), dtype = 'uint8')

# cv2.rectangle(img, [50,100], [300, 300], (255, 34, 5), 5)
cv2.rectangle(img, [50,100], [300, 300], (255, 34, 5), cv2.FILLED)

cv2.circle(img, [300, 300], 100, (255, 34, 5), cv2.FILLED)

cv2.line(img, [10, 10], [400, 400], (255, 255, 0), 10)

cv2.imshow("title", img)

cv2.waitKey(0)