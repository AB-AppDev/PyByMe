# Face Recognise

import cv2
from PyProjects import bulkface

Detect = cv2.CascadeClassifier("C:\\Users\\abhis\\Pictures\\Py\\haarcascade_frontalface_default.xml")

i_img = cv2.VideoCapture("C:\\Users\\abhis\\Pictures\\Py\\yog1.jpg")

res, img = i_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = Detect.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

imgS = cv2.resize(img, (460, 540))

cv2.imshow("Abhi Image", imgS)
cv2.waitKey(0)
i_img.release()
cv2.destroyAllWindows()

bulkface.play()
