# Opencv
    # read --< img, video
    # resizing, reslaing..
    # shapes
    # puttext



import cv2  # BGR

my_image = cv2.imread("nature-photography-at-its-best-1200x569.jpeg")
cv2.imshow("Origanl Image", my_image)

# convert image to gray
gry_img = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gry_img)

# convert image to HSV
hsv_img = cv2.cvtColor(my_image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)

# blur the image 
blur_img = cv2.GaussianBlur(my_image, (7, 7), cv2.BORDER_DEFAULT)
cv2.imshow("Blur Image", blur_img)

# get_edges
edges = cv2.Canny(blur_img, 200, 200)
cv2.imshow("Edges Image", edges)

cv2.waitKey(0)