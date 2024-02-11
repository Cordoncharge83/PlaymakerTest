#importing the libraries
import cv2 as cv
import numpy as np

#Check if the happy pixels ratio is acceptable or not (more details in the readme file)
def is_happy(im, threshold = 400, happy_ratio = 0.65):
    width,height,_ = im.shape
    total_pixels = width*height
    happy_pixels = 0
    for i in range(width):
        for j in range(height):
            s = sum (im[i,j][k] for k in range(2))
            if s > threshold:
                happy_pixels += 1
    if happy_pixels == 0 :
        return False            
    return((total_pixels/happy_pixels) > happy_ratio)     

#Multiply the picture's saturation by the adjust value in order to make the colors more vibrant
def happier(imagei,adjust = 1.3):
    imghsv = cv.cvtColor(imagei, cv.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv.split(imghsv)
    print(s)
    s = s*adjust
    s = np.clip(s,0,255)
    imghsv = cv.merge([h,s,v])
    imgrgb = cv.cvtColor(imghsv.astype("uint8"), cv.COLOR_HSV2BGR)
    return imgrgb
