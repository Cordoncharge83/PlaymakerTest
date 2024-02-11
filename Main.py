#importing the libraries
import cv2 as cv
import numpy as np

#importing the modules
import size_and_transparency as st
import shape
import happy as h
    
    
def applier():
    #loading the image source 
    input_path = input('What is the source picture ? ' )

    #reading the image with OpenCv
    im = cv.imread(input_path, cv.IMREAD_UNCHANGED)
        # Check if image is loaded fine
    if im is None:
        print ('Error opening image!')
        return -1
    
    #Applying the size check, and resizing in case size is not valid :
    if st.is_size_ok(im) == False :
        im = cv.resize(im, (512,512))
    print("picture size ok !")

    HEIGHT,WIDTH = 512,512
    
    #Applying the transparency check, and adding one in case is not valid : 
    if not st.isValidtransparency(im):
        im = cv.cvtColor(im, cv.COLOR_RGB2RGBA)
    print('image pixels have ', im.shape[2], ' channels')
    

    #Reshaping the image so that it fits the requirement
    im = shape.reshape(im,input_path)
    
    #Detecting the image shape (circle with the outside pixels being transparent)
    circle = shape.detectCircle(im)

    #Going through the image pixels and checking for non-transparent ones
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if not shape.isPixelInsideCircle(x, y, circle):
                # Check alhpa channel for transparency
                if im[y,x][3] != 0:
                    print('Non transparent pixel outside circle image detected: ('+str(x)+','+str(y)+')')
                    return -3
    print('All non-transparent pixels are within the circle ')
    
    #Checking if the colors are "happy" (threshold is set to 400 and ratio to 65%)
    #If the colors are not "happy" enough, the picture's saturation would get bumped up by 30%
    if h.is_happy(im) == False:
        print("Picture needs more happiness")
    while (h.is_happy(im) == False):
        im = h.happier(im)
        h.is_happy(im)
    
    #Show the final picture
    cv.imshow('final_image', im)
    cv.waitKey(0)
    cv.destroyAllWindows()
        
    
def checker():
    #loading the image source 
    input_path = input('What is the source picture ?' )

    #reading the image with OpenCv
    im = cv.imread(input_path, cv.IMREAD_UNCHANGED)
    # Check if image is loaded fine
    if im is None:
        print ('Error opening image!')
        return -1
    
    #Applying the size check
    if st.is_size_ok(im) == False :
        print("invalid picture size !")
        return -2

    HEIGHT,WIDTH = 512,512
    
    #Applying the transparency check, and adding one in case is not valid : 
    if not st.isValidtransparency(im):
        im = cv.cvtColor(im, cv.COLOR_RGB2RGBA)
    print('image pixels have ', im.shape[2], ' channels')
    
    
    #Detecting the image shape (circle with the outside pixels being transparent)
    circle = shape.detectCircle(im)
    
    #Going through the image pixels and checking for non-transparent ones
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if not shape.isPixelInsideCircle(x, y, circle):
                # Check alhpa channel for transparency
                if im[y,x][3] != 0:
                    print('Non transparent pixel outside circle image detected: ('+str(x)+','+str(y)+')')
                    return -3
    print('All non-transparent pixels are within the circle ')
    
    
    #Checking if the colors are "happy" (threshold is set to 400 and ratio to 65%)
    if h.is_happy(im):
        print("Picture colors give a happy feeling")
    else :
        print("Picture needs more happiness")
        return -4
    
    #Show the final picture
    cv.imshow('final_image', im)
    cv.waitKey(0)
    cv.destroyAllWindows()


#applier()
checker()

'''
# To Check the correct format (PNG), we can import magic and add the following code 
if (magic.from_file(filename).split()[0]!='PNG'):
    print('File must be a PNG.')
    print('File is: '+magic.from_file(filename))
    return -1
    '''