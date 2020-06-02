import cv2, glob


def play():
    ging = glob.glob("C:\\Users\\abhis\\Pictures\\Py\\*.jpg")
    Detect = cv2.CascadeClassifier("C:\\Users\\abhis\\Pictures\\Py\\haarcascade_frontalface_default.xml")

    for timg in ging:
        img = cv2.imread(timg)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = Detect.detectMultiScale(gray, 1.20, 5)

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

        imgS = cv2.resize(img, (960, 540))

        cv2.imshow("FACER", imgS)

        cv2.waitKey(1000)
        cv2.destroyAllWindows()
