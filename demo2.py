from detect import detect
import cv2 
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# img = cv2.imread('data4.jpg')
# text = pytesseract.image_to_string(img)
# print(text)
# def loop():
#     detect("last.pt",)

# # loop()


im2, contours, hierarchy = cv2.findContours('img4.JPG',cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#contour with the largest area is possibly the plate
max_area = 0
max_cnt = None
for cnt in contours:
    area = cv2.contourArea(cnt)
    if(area > max_area):
        max_area = area 
        max_cnt = cnt

min_rect = cv2.minAreaRect(max_cnt)
(x,y,w,h,angle) = min_rect

#rotate
M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1.0)
rotated_plate = cv2.warpAffine('img4.JPG', M, (w,h))