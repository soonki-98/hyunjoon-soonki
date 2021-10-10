import numpy as np
import cv2 as cv
import sys

img1 = cv.imread("C:/github/hyunjoon-soonki/images/256_pattern_gray.jpg", cv.IMREAD_GRAYSCALE)
if img1 is None:
    sys.exit("Could not read 256_pattern_gray.jpg.")
print(img1)

rowSize, colSize = img1.shape
print("rowSize:%d colSize:%d" % (rowSize, colSize))
print("size : %d" % (img1.size))
print(img1.dtype)

img2 = cv.imread("C:/github/hyunjoon-soonki/images/256_smile_gray.jpg", cv.IMREAD_GRAYSCALE)
if img2 is None:
    sys.exit("Could not read 256_patt256_smile_gray.jpg.")
print(img2)

cv.imshow("256_pattern_gray", img1)
cv.imshow("256_smile_gray", img2)
k = cv.waitKey(0)

#imgadd = img1 + img2
alpha = 0.5 #합성에 사용할 알파 값
imgadd = cv.addWeighted(img1, alpha, img2, (1-alpha), 0)
cv.imshow("add",imgadd)
k = cv.waitKey(0)