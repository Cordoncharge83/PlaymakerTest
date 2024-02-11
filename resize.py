import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

input_path = 'raid.jpg'
im = cv.imread(input_path)
print('Image Width is',im.shape[1])
print('Image Height is',im.shape[0])
im = cv.resize(im, (512,512))
im = cv.cvtColor(im, cv.COLOR_RGB2RGBA)
def define_circle(imagei):
    height, width, _ = imagei.shape
    radius = (512 // 2)-10
    center = (height // 2, width // 2)
    for x in range(width):
        for y in range(height):
            if np.linalg.norm((x - center[0], y - center[1])) > radius:
                imagei[y, x] = [255,255,255,0]
    return imagei

final = define_circle(im)
x = input_path.split('.')
final_name = 'final'+x[0]+'.png'
cv.imwrite(final_name, final)
cv.imshow('image',im)
cv.imshow('image2', final)
cv.waitKey(0)
cv.destroyAllWindows()


def happier(imagei,adjust = 1.5):
    imghsv = cv.cvtColor(imagei, cv.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv.split(imghsv)
    print(s)
    s = s*adjust
    s = np.clip(s,0,255)
    imghsv = cv.merge([h,s,v])
    imgrgb = cv.cvtColor(imghsv.astype("uint8"), cv.COLOR_HSV2BGR)
    return imgrgb

finalf = happier(final)
cv.imshow('image2', finalf)
cv.waitKey(0)
cv.destroyAllWindows()