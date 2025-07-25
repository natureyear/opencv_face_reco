import cv2 as cv

def face_recongnition(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_rec = cv.CascadeClassifier('/Users/hh/anaconda3/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face = face_rec.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    # cv.imwrite("output_recognized.png", image)
    cv.imshow('Face Recognition',image)
    while True:
        if cv.waitKey(0) & 0xFF == ord('q'):
            print('Quit...')
            break
    cv.destroyWindow("Face Recognition")


# Read img
image = cv.imread("./imgs/pearson_grade.png")
if image is None:
    print("Load Error...")
    exit()
else:
    print("Load Success...")

face_recongnition(image)
