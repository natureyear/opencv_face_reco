import cv2 as cv

# Read img
image = cv.imread("./imgs/face1.png")

if image is None:
    print("Load Error...")
    exit()
else:
    print("Load Success...")

# Rectangle
# Coordinate
x, y, w, h = 100, 100, 200, 200
cv.rectangle(image, (x,y), (x + w, y + h), (0, 0, 255), 3)

# Circle
cv.circle(image, (x + 100, y + 100), 100, (0, 255, 0), -1)
cv.imshow("image", image)
cv.waitKey(0)
cv.destroyWindow("Face1")