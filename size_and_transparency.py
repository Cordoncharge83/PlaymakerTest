#importing the libraries
import cv2 as cv
import numpy as np

#Checking if the image size is 512x512 or not
def is_size_ok(image):
    return(image.shape[0] == image.shape[1] == 512)

# Check if image has 4 channels : RGBA
def isValidtransparency(img):    
    return img.shape[2]==4