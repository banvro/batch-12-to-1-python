import cv2


def frame_resizing(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    demession = (width, height)
    resized_frame = cv2.resize(frame, demession, interpolation = cv2.INTER_AREA)
    
    return resized_frame

img = cv2.imread("images/pexels-pixabay-45201.jpg")

print(img.shape)
cv2.imshow("my Cat", img)


xyz = frame_resizing(img, scale = 0.10)
cv2.imshow("my new", xyz)

cv2.waitKey(0)