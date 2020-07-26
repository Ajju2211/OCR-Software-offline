import cv2
import numpy as np

originalImage = cv2.imread('original.jpeg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
blackAndWhiteImage=cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)
img_bw = 255*(cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')

se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
mask = cv2.morphologyEx(blackAndWhiteImage, cv2.MORPH_CLOSE, se1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)


mask = np.dstack([mask, mask, mask]) / 255

out = originalImage * mask
cv2.imshow('Output', out)
cv2.imwrite('output.jpeg', out)
out=cv2.imread("output.jpeg")
grayImage = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
blackAndWhiteImage=cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)
cv2.imshow('out2',blackAndWhiteImage)


