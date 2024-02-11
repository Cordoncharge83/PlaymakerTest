#importing the libraries
import cv2 as cv
import numpy as np



def detectCircle(img):
    #Use a copy to keep the original image intact
    img_copy = img.copy()
    # Convert to grayscale. 
    gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY) 

    # Blur using 3 * 3 kernel. 
    gray_blurred = cv.blur(gray, (3, 3)) 

    # Apply Hough transform on the blurred image. 
    detected_circles = cv.HoughCircles(gray_blurred, 
				    cv.HOUGH_GRADIENT, 1, 20, param1 = 50, 
			    param2 = 30, minRadius = 100, maxRadius = 256) 

    # Draw circles that are detected. 
    if detected_circles is not None: 
  
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
  
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            if (a==b==256) : 
                # Draw the circumference of the circle. 
                cv.circle(img_copy, (a, b), r, (0, 255, 0), 2) 
        cv.imwrite("circle.png", img_copy)
        '''
        cv.imshow("Detected Circle", img_copy)  #For testing purposes
        cv.imshow('original', img) 
        cv.waitKey(0)
        ''' 
        return np.uint16(np.around(detected_circles)) #to round the pixel values

#Function used to verify is a pixel is inside a given circle or not
def isPixelInsideCircle(x, y, circle):
    x_center = circle[0][0][0]
    y_center = circle[0][0][1]
    radius = circle[0][0][2]
    return (x - x_center)**2 + (y - y_center)**2 <= radius**2

#Function used to crop a circle from an image and make the outer pixels transparent
def define_circle(im):
    height, width, _ = im.shape
    radius = (512 // 2)-10
    center = (height // 2, width // 2)
    for x in range(width):
        for y in range(height):
            if np.linalg.norm((x - center[0], y - center[1])) > radius:
                im[y, x] = [255,255,255,0]
    return im

#Apply the previous function onto the picture and save the new result
def reshape(im,input_path):  
    im = cv.cvtColor(im, cv.COLOR_RGB2RGBA)
    final = define_circle(im)
    x = input_path.split('.')
    final_name = 'final'+x[0]+'.png'
    cv.imwrite(final_name, final)
    '''
    cv.imshow('image2', final) # For testing purposes
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''
    return im