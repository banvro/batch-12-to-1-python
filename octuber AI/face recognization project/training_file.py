import numpy as np
import cv2 as cv
import os

# maintain list of folders...


# people = []

# for i in os.listdir(r"C:\Users\17nru\OneDrive\Desktop\delete this"):
#     people.append(i)

# print(people)

people = ['elon musk', 'joker', 'kristina_pemenova']

DIR = r"C:\Users\17nru\OneDrive\Desktop\delete this"

features = []
lables = []

def train_model():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

            face_data = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in face_data:
                feature = gray[y:y+h, x:x+w]
                features.append(feature)
                lables.append(label)


train_model()

# print(len(features))
# print(len(lables))
features = np.array(features, dtype = 'object')
lables = np.array(lables)

# traing the model 

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, lables)

# yml 
face_recognizer.save("face_trained.yml")
