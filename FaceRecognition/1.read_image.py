import cv2 as cv

# Read img
image = cv.imread("./imgs/face1.png")

if image is None:
    print("Load Error...")
    exit()
else:
    print("Load Success...")
# Show img
cv.imshow("Face1", image)

cv.waitKey(0)

cv.destroyWindow("Face1")
