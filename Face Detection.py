import cv2 as cv

# Displays a sample of a single person pic with full BGR color
img = cv.imread('OpenCV\Photos\lady.jpg')
cv.imshow('Person', img)

# To detect faces, opencv does not take note of colors, rather it considers the edges found
# in the pics. The test pic is first converted to a gray tone.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# Imports the opencv face cascade algorithm
haarCascade = cv.CascadeClassifier('OpenCV\Codes\Haar_Face_Cascade.xml')

facesRect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found: {len(facesRect)}')  # Number of faces found is 1

# Grabs the coordinate of the detected face and draws a green rectangle around it
for (x, y, w, h) in facesRect:
    detectedFace = cv.rectangle(
        img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv.imwrite('OpenCV\Results\detectedFace.png', detectedFace)

detectedFace = cv.imshow('Detected Face', img)

# saves image
gray = cv.imwrite('OpenCV\Results\gray.png', gray)

# Displays a sample of a multiple faces pic with full BGR color
images = cv.imread('OpenCV\Photos\group 2.jpg')
cv.imshow('Multiple Faces', images)

grayFaces = cv.cvtColor(images, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Faces', grayFaces)

multipleFacesRect = haarCascade.detectMultiScale(
    grayFaces, scaleFactor=1.1, minNeighbors=6)

# Number of faces originally found was 7 instead of 5 when minNeighbors arguement was set
# to 3. Increasing it to 6 stopped opencv from classifying stomach as a face.
print(f'Number of faces found: {len(multipleFacesRect)}')

for (x, y, w, h) in multipleFacesRect:
    multipleFaces = cv.rectangle(
        images, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv.imwrite('OpenCV\Results\multipleFaces.png', multipleFaces)

grayFaces = cv.imwrite('OpenCV\Results\grayFaces.png', grayFaces)

# Opencv still detects part of neck + mouth as a face
cv.imshow('Detected Multiple Faces', images)


complexImage = cv.imread('OpenCV\Photos\group 1.jpg')

cv.imshow('Complex Images', complexImage)

grayComplexFaces = cv.cvtColor(complexImage, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Faces', grayComplexFaces)

multipleComplexFacesRect = haarCascade.detectMultiScale(
    grayComplexFaces, scaleFactor=1.1, minNeighbors=1)

# Number of faces originally found was 6 when minNeighbors arguement was set to 6. 14 when it
# was 3 and 14 when it's 1. Not all faces are detected as some faces are not perpendicular to
# the camera and some people wore accessories like glasses and hat.
# Reducing the minNeighbors value makes opencv more exposed to noise.
print(f'Number of faces found: {len(multipleComplexFacesRect)}')

for (x, y, w, h) in multipleComplexFacesRect:
    complexFaces = cv.rectangle(
        complexImage, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv.imwrite('OpenCV\Results\complexFaces.png', complexFaces)

grayComplexFaces = cv.imwrite(
    'OpenCV\Results\grayComplexFaces.png', grayComplexFaces)
cv.imshow('Detected Complex Multiple Faces', complexImage)

cv.waitKey(0)
