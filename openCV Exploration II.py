import cv2 as cv
import numpy as np

# code to read and display images
img = cv.imread('OpenCV\Photos\cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# code to display videos from pc webcam
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

# function to change resolution of videos


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
    capture.set(10, 100)

# function to rescale and resize images


def rescaleFrame(frame, scale=7):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# code to display videos
capture = cv.VideoCapture('OpenCV\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()
    frameResized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frameResized)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows

# code to draw blank images
blank = np.zeros((500, 500, 3), dtype='uint8')
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# code to draw various shapes and write text on images
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)
cv.circle(blank, (blank.shape[1]//2,
                  blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)
cv.line(blank, (100, 250),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)
cv.putText(blank, 'Hello World', (225, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)

# codes to change color tone, detect edges, blur images, dilate, erode and resize pics

img = cv.imread('OpenCV\Photos\park.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cannyEdges = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', cannyEdges)

dilated = cv.dilate(cannyEdges, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# saves images
blur = cv.imwrite('OpenCV\Results\.blur.png', blur)
cannyEdges = cv.imwrite('OpenCV\Results\cannyEdges.png', cannyEdges)
dilated = cv.imwrite('OpenCV\Results\dilated.png', dilated)
eroded = cv.imwrite('OpenCV\Results\eroded.png', eroded)
resized = cv.imwrite('OpenCV\Results\.resized.png', resized)
cropped = cv.imwrite('OpenCV\Results\cropped.png', cropped)

cv.waitKey(0)

img = cv.imread('OpenCV\Photos\park.jpg')
cv.imshow('Park', img)

# funtion to translate and warp images


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translate = translate(img, -100, -100)
cv.imshow('Translated', translate)
translate = cv.imwrite('OpenCV\Results\.translate.png', translate)

# function to rotate images


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
rotated = cv.imwrite('OpenCV\Results\.rotated.png', rotated)


cv.waitKey(0)

img = cv.imread('OpenCV\Photos\cats.jpg')
cv.imshow('Cats', img)

# codes to change color tone, detect edges, blur images, dilate, thresh and find contoursqq
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

IIcanny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', IIcanny)
IIcanny = cv.imwrite('OpenCV\Results\IIcannyEdges.png', IIcanny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
threshedPic = cv.imwrite('OpenCV\Results\.threshedPic.png', thresh)

contours, hierachies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} Contours found')

cv.waitKey(0)

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# codes to carry out bitwise operations, mask images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('BitWise', bitwise_and)
bitAnd = cv.imwrite('OpenCV\Results\.bitAnd.png', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)
bitOr = cv.imwrite('OpenCV\Results\.bitOr.png', bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)
bitXor = cv.imwrite('OpenCV\Results\.bitXor.png', bitwise_xor)

bitwise_not = cv.bitwise_not(rectangle)
bitNot = cv.imwrite('OpenCV\Results\.bitNot.png', bitwise_not)
cv.imshow('Rectangle NOT', bitwise_not)

cv.waitKey(0)

img = cv.imread('OpenCV\Photos\cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)
mask = cv.imwrite('OpenCV\Results\mask.png', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)
masked = cv.imwrite('OpenCV\Results\masked.png', masked)

cv.waitKey(0)
