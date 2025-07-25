import cv2 as cv

def face_recongnition(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_rec = cv.CascadeClassifier('/Users/hh/anaconda3/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face = face_rec.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    # cv.imwrite("output_recognized.png", image)
    return image

# Capture camera
cap = cv.VideoCapture(1)
while True:
    flag, frame = cap.read()
    if not flag:
        break
    result_frame = face_recongnition(frame)
    cv.imshow("Face Recognition", result_frame)
    # Detect input if is 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()