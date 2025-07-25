import cv2 as cv

# By mac
cap = cv.VideoCapture(1)

num = 1

while cap.isOpened():
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    key = cv.waitKey(1)

    # Use camera to save
    if key == ord('s'):
        cv.imwrite("./imgs/" + str(num) + ".jpg", frame)
        print("Save success...")
        print("------------------")
        num += 1
    elif key == ord(' '):
        break

# Release
cap.release()
cv.destroyWindow("frame")