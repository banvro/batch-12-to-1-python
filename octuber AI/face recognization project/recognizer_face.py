import cv2 as cv
import numpy as np

people = ['elon musk', 'joker', 'kristina_pemenova']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread("Elon_Musk_Royal_Society.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

face_data = haar_cascade.detectMultiScale(gray_img, 1.1, 4)

for (x, y, w, h) in face_data:

    only_face = gray_img[y:y+h, x:x+h]

    indexnum, confidence = face_recognizer.predict(only_face)

    print("the confidence is : ", confidence, "and index numbe is : ", indexnum)

    cv.putText(img, str(people[indexnum]), (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

    cv.imshow("asd", img)

    cv.waitKey(0)
    


# # cv.imshow("unknown", img)

# # cv.waitKey(0)