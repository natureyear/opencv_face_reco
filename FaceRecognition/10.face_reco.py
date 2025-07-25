import cv2
import cv2 as cv
import os
import urllib
import urllib.request

# Load training dataset file
recogizer = cv.face.LBPHFaceRecognizer_create()
# Load data
recogizer.read('./trainer/trainer.yml')
# name
names = []

# Alert global variable
warningtime = 0

# md5 code
def md5(str):
    print()
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def warning():
    print("Warning! This")

def name():
    global names
    dataset_path = './train_img'
    names = sorted([d for d in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, d))])

# Recognize
def face_recognize_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, cv.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.circle(img, (x + w // 2, y + h // 2), 5, (0, 255, 0), 1)

        ids, confidence = recogizer.predict(gray[y:y+h, x:x+w])

        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
                warning()
                warningtime = 0
            cv.putText(img, 'unknown', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        else:
            cv.putText(img, str(names[ids-1]), (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

# Main
name()
cap = cv.VideoCapture(1)

while True:
    flag, frame = cap.read()
    if not flag:
        break

    # Modify frame
    face_recognize_demo(frame)

    cv.imshow('img', frame)  # SHow the modified frame
    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # Q or ESC
        break

cap.release()
cv.destroyAllWindows()
