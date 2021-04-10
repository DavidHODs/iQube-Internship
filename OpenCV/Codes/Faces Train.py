import os
import cv2 as cv
import numpy as np

# pretrained cascade classifier
haarCascade = cv.CascadeClassifier('OpenCV\Codes\HaarFaceCascade.xml')

directory = 'OpenCV\Faces\Train'
people = []

# features(images) and labels(identities) make up the training set
features = []
labels = []

# grabs all the subfolders in the train folder and append it to the list 'people'
for folder in os.listdir('OpenCV\Faces\Train'):
    people.append(folder)

print(people)

# function to loop through the train folder, grab resources for the training set and detect faces


def createTrain():
    for person in people:
        path = os.path.join(directory, person)
        label = people.index(person)

        for img in os.listdir(path):
            imgPath = os.path.join(path, img)

            # reads the images, converts them to gray color and detect the position of faces
            imgArray = cv.imread(imgPath)
            gray = cv.cvtColor(imgArray, cv.COLOR_BGR2GRAY)

            facesRect = haarCascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)
            # loops through all the faces in facesRect and cuts out the region of intersest (face)
            for (x, y, w, h) in facesRect:
                facesROI = gray[y:y+h, x:x+w]
                features.append(facesROI)
            # labels contain numeric identities not text. Mapping will be done to establish the link between numeric
            # id and atual identity.
                labels.append(label)


createTrain()

# confirms if the amount of features and labels grabbed corresponds
print(f'Length of the features: {len(features)}')
print(f'Length of the labels: {len(labels)}')

# converts the features and labels into a numpy array
features = np.array(features, dtype=object)
labels = np.array(labels)

# saves the numpy arrayed features and labels list
np.save('features.npy', features)
np.save('labels.npy', labels)

# the numpy arrayed features and labels are used to train a face recognizer

# instantiates the face recognizer
faceRecognizer = cv.face.LBPHFaceRecognizer_create()
faceRecognizer.train(features, labels)

print('******Training Done******')

# saves the trained model
faceRecognizer.save('faceTrained.yml')
