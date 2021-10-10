import numpy as np
import cv2 as cv
import sys

img = cv.imread("C:/github/hyunjoon-soonki/images/256_smile_gray.jpg", cv.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Could not read 256_smile_gray.jpg.")
print(img)

rowSize1, colSize1 = img.shape
print("rowSize:%d colSize:%d" % (rowSize1, colSize1))
print("size : %d" % (img.size))
print(img.dtype)
cv.imshow("256_smile_gray", img)
k = cv.waitKey(0)

imgOut = np.zeros((rowSize1//2, colSize1//2), dtype=np.uint8)

for i in range(rowSize1//2):
    for j in range(colSize1//2):
        imgOut[i,j] = img[i,j]

dst = cv.resize(img, dsize=(128, 128), interpolation=cv.INTER_AREA)
cv.imshow("dst1",dst)           
k = cv.waitKey(0)

