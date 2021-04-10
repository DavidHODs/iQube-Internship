import numpy as np
import cv2 as cv
import os

# pretrained cascade classifier
haarCascade = cv.CascadeClassifier('OpenCV\Codes\HaarFaceCascade.xml')

# loads the numpy arrayed features and labels from Faces Train.py
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

# reads the trained face recognizer in Faces Train.py
faceRecognizer = cv.face.LBPHFaceRecognizer_create()
faceRecognizer.read('faceTrained.yml')

# grabs all the subfolders in the train folder and append it to the list 'people'
people = []
for folder in os.listdir('OpenCV\Faces\Train'):
    people.append(folder)

# creates a validation variable
img = cv.imread(r'OpenCV\Faces\Val\Mindy Kaling\3.jpg')

# converts the vlidation image to gray color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# detects the face in the image
facesRect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# loops through the faces(s) in facesRect and grabs the region of interest
for (x, y, w, h) in facesRect:
    facesROI = gray[y:y+h, x:x+h]
    # predicts the lebel and outputs the confidence level
    label, confidence = faceRecognizer.predict(facesROI)
    print(f'Label: {people[label]} with a confidence of {confidence} %')
    # writes the label on the image
    cv.putText(img=img, text=str(people[label]), org=(
        20, 20), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(255, 255, 0), thickness=2)
    # draws a green rectangle around the face(s) in the image
    faceRecognition = cv.rectangle(img=img, pt1=(x, y), pt2=(
        x+w, y+h), color=(0, 255, 0), thickness=2)
    # saves the predicted image
    cv.imwrite(f'OpenCV\Results\{people[label]}.png', faceRecognition)

# displays the predicted image
cv.imshow(f'{people[label]}', img)

cv.waitKey(0)
