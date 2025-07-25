import cv2 as cv

# Read img
image = cv.imread("./imgs/face1.png")

if image is None:
    print("Load Error...")
    exit()
else:
    print("Load Success...")


# Modify size
resized_img = cv.resize(image, (200, 200))

# Show img
cv.imshow("Face1_resized", resized_img)

print(image.shape)
print(resized_img.shape)

key = cv.waitKey(0)
if key == ord('q'):
    print('Quitting...')
    cv.destroyWindow("Face1")