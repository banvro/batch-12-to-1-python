import cv2
import numpy as np

img = np.zeros((550, 550), dtype="uint8")


rectanggle = cv2.rectangle(img.copy(), (30, 30), (500, 500), 255, -1)
cirl = cv2.circle(img.copy(), (260, 260), 260, 255, -1)


cv2.imshow("Sd", rectanggle)
cv2.imshow("asd", cirl)
#  bitwise_or
biwise_And = cv2.bitwise_and(rectanggle, cirl)
cv2.imshow("d", biwise_And)
cv2.waitKey(0)