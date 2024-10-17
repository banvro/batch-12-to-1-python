import cv2

def frame_resizing(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    demession = (width, height)
    resized_frame = cv2.resize(frame, demession, interpolation = cv2.INTER_AREA)
    
    return resized_frame


capture = cv2.VideoCapture("videos/979689-hd_1920_1080_30fps.mp4")
while True:
    isTrue, frame = capture.read()

    cv2.imshow("my video", frame)

    new_frame = frame_resizing(frame)
    cv2.imshow("ressized video", new_frame)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break