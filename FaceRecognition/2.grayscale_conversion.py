import cv2 as cv

# Read img
image = cv.imread("./imgs/face1.png")

if image is None:
    print("Load Error...")
    exit()
else:
    print("Load Success...")

# GrayScale
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Show img
cv.imshow("Face1", image)
cv.imwrite("./imgs/face1_grey.png", image)
cv.waitKey(0)

cv.destroyWindow("Face1")