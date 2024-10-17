# import cv2

# capture = cv2.VideoCapture("videos/979689-hd_1920_1080_30fps.mp4")

# while True:
#     isTrue, frame = capture.read()

#     cv2.imshow("my video", frame)

#     if cv2.waitKey(20) & 0xff == ord("q"):
#         break





import cv2

capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv2.imshow("my video", frame)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break