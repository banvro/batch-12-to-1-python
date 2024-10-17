import cv2

img = cv2.imread("images/pexels-pixabay-45201.jpg")

cv2.imshow("my Cat", img)

xyz = cv2.resize(img, (500, 500), interpolation = cv2.INTER_AREA)

cv2.imshow("eeee", xyz)

cv2.waitKey(0)