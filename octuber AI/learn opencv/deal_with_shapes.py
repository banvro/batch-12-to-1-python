import numpy as np
import cv2

blank_img = np.zeros((500, 500), dtype='uint8')

reactange = cv2.rectangle(blank_img.copy(), (40, 40), (460, 460), (255, 255, 255), -1)

circle = cv2.circle(blank_img.copy(), (250, 250), 240, (255, 255, 255), -1)

cv2.imshow("rectange image", reactange)
cv2.imshow("circle image", circle)

# bitwise_and

bitwise_and = cv2.bitwise_and(reactange, circle)
cv2.imshow("combined image", bitwise_and)

# bitwise_or

x = cv2.bitwise_or(reactange, circle)
cv2.imshow("bitwise_or", x)

# bitwise_xor

y = cv2.bitwise_xor(reactange, circle)
cv2.imshow("bitwise_xor", y)

cv2.waitKey(0)


# face detection   1000
# face recognize