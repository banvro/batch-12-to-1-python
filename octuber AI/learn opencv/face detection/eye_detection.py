# import cv2

# myImg = cv2.imread("xDTRYSD5_66bs_1024.jpg")

# # convert image to gray
# grayimg = cv2.cvtColor(myImg, cv2.COLOR_BGR2GRAY)

# # eye_decter = cv2.CascadeClassifier("detect_eye.xml")

# eye_decter = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# eyes = eye_decter.detectMultiScale(grayimg, scaleFactor = 1.1, minNeighbors = 10, minSize = (100, 100))

# print(eyes)

# for (x, y, w, h) in eyes:
#     cv2.rectangle(myImg, (x, y), (x+w, y+h), (255, 0, 0), 2)


# cv2.imshow("Girl Eyes", myImg)

# cv2.waitKey(0)








# import cv2

# myImg = cv2.imread("humans.jpg")

# # convert image to gray
# grayimg = cv2.cvtColor(myImg, cv2.COLOR_BGR2GRAY)

# # eye_decter = cv2.CascadeClassifier("detect_eye.xml")

# eye_decter = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# eyes = eye_decter.detectMultiScale(grayimg, scaleFactor = 1.1, minNeighbors = 10, minSize = (30, 30))

# print(eyes)

# for (x, y, w, h) in eyes:
#     cv2.rectangle(myImg, (x, y), (x+w, y+h), (255, 0, 0), 2)


# cv2.imshow("Girl Eyes", myImg)

# cv2.waitKey(0)


import cv2
import numpy as np

black_box = np.zeros((500, 500), dtype = "uint8")

# start_row, end_row
cv2.rectangle(black_box, (20, 200), (34, 45), (255, 255, 255), 3)

cv2.imshow("black boc", black_box)

cv2.waitKey(0)