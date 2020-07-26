import cv2
import numpy as np
import os
import sys

 
if __name__ == '__main__' :
 
    
    im = cv2.imread("original.jpeg")
     
    # Select ROI
    r = cv2.selectROI(im)
     
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    #frame=imCrop.get_frame()
    cv2.imwrite("cropped.jpeg",imCrop)
  
 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    os.system("python ocrOriginalPrev.py")
    sys.exit(0)
   # cv2.waitKey(0)
   # fromCenter = False
   # r = cv2.selectROI("Image", im, fromCenter)
   # showCrosshair = False
   # fromCenter = False
   # r = cv2.selectROI("Image", im, fromCenter, showCrosshair)
   # rects = []
   # fromCenter = false
  # Select multiple rectangles
   # selectROI("Image", im, rects, fromCenter)
