import cv2

cap = cv2.VideoCapture(0)

while True:
    is_True, myImg = cap.read()



    # convert image to gray
    grayimg = cv2.cvtColor(myImg, cv2.COLOR_BGR2GRAY)

    # eye_decter = cv2.CascadeClassifier("detect_eye.xml")

    eye_decter = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    eyes = eye_decter.detectMultiScale(grayimg, scaleFactor = 1.1, minNeighbors = 10, minSize = (30, 30))

    print(eyes)

    for (x, y, w, h) in eyes:
        cv2.rectangle(myImg, (x, y), (x+w, y+h), (255, 0, 0), 2)


    cv2.imshow("Girl Eyes", myImg)

    if cv2.waitKey(20) & 0xff == ord('s'):
        break



remember whatever we do with images also work with videos or live camera....
