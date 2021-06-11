import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import pymongo


def crop(xmin,ymin,w,h,img):
    # vid = cv2.VideoCapture(0)
    # img = cv2.imread("main_7.jpg")
    # crop_img = img[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    # get resolution and coordinates
# height, width = image.shape[:-1]
    xmax = xmin + w
    ymax = ymin + h

    # fetch roi
    # if (xmin  >= 0) and (ymin >= 0) and (xmax < w) and (ymax < h):
        # print("IN IF")
    roi = img[ymin:ymax, xmin:xmax]
    # cv2.imshow("cropped", roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    answer = ocr(roi)
    return answer

def ocr(cropimg):

    # cv2.imshow("",cropimg)
    gray = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(gray.shape, np.uint8)
    if(location is not None):
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(cropimg, cropimg, mask=mask)
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]
        reader = easyocr.Reader(['th'])
        result = reader.readtext(cropped_image)
        if(len(result) == 3):
            answer = result[0][1] + result[2][1] + result[1][1] 
            print("**************")
            print(answer)
            print("**************")
            return answer
    return "NO LICENSE PLATE"
    
