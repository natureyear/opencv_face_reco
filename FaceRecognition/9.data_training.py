import os
import numpy as np
import cv2 as cv
from PIL import Image

def getImagesAndLabels(path):
    # Store each face
    faceSamples = []
    # Store id
    ids = []

    # Get all paths from content
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # Load haar face classifier
    face_detector = cv.CascadeClassifier(cv.data.haarcascades + '/haarcascade_frontalface_alt2.xml')

    for imagePath in imagePaths:
        # Skip files don't images
        if not imagePath.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        # Load img
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        # Recognize face
        faces = face_detector.detectMultiScale(img_numpy)

        # Extract id
        id = int(os.path.split(imagePath)[1].split('.')[0])

        # Iterate all face
        for (x, y, w, h) in faces:
            ids.append(id)
            faceSamples.append(img_numpy[y:y + h, x:x + w])

        print('id:', id)
        print('fs:', faceSamples)

    return faceSamples, ids

if __name__ == "__main__":
    # Image path
    imagePath = "./train_img/"
    facesSamples, ids = getImagesAndLabels(imagePath)
    # Load recognizer
    recognizer = cv.face.LBPHFaceRecognizer_create()
    # Training
    recognizer.train(facesSamples, np.array(ids))
    print('---------------')
    recognizer.write("./trainer/trainer.yml")

