# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:18:25 2020

@author: johaant
"""

import cv2
import numpy as np
from PIL import Image
import time

def shift_image(shift_key, img):
    """
    Function to shift the object with the w,a,s,d keys.
    """
    
    if shift_key == ord('w'):
        img=np.roll(img, -1, axis = 0)
    elif shift_key == ord('s'):
        img=np.roll(img, 1, axis = 0)
    elif shift_key == ord('a'):
        img=np.roll(img, -1, axis = 1)
    elif shift_key == ord('d'):
        img=np.roll(img, 1, axis = 1)
    return img

def change_size(size_key, img, max_disp, object_colour):
    """
    Function to increase or decrease the size of the object.
    """
    
    curr_obj_size = img.shape[0]
    if size_key == ord('i'):
        new_img = cv2.resize(img, (curr_obj_size + 1, curr_obj_size + 1), Image.ANTIALIAS)
    else:
        new_img = cv2.resize(img, (curr_obj_size - 1, curr_obj_size - 1), Image.ANTIALIAS)
        
    ## We always want the image to be 600x600
    if new_img.shape[0] > max_disp:
        new_img = new_img[0:max_disp, 0:max_disp]
    elif new_img.shape[0] < max_disp:
        ## If the image is greyscale or not
        if len(new_img.shape) > 2:
            
            if object_colour == 1:
                b_img = np.zeros((max_disp, max_disp, new_img.shape[2]))
            else:
                ## Mutliply with the max if white is given as 1 or 255
                b_img = np.ones((max_disp, max_disp, new_img.shape[2]))*np.max(new_img)
            #b_img = np.zeros((max_disp, max_disp, new_img.shape[2]))
            b_img[0:new_img.shape[0],0:new_img.shape[0],:] = new_img
        else:
            
            if object_colour == 1:
                b_img = np.zeros((max_disp, max_disp))
            else:
                ## Mutliply with the max if white is given as 1 or 255
                b_img = np.ones((max_disp, max_disp))*np.max(new_img)
            b_img[0:new_img.shape[0],0:new_img.shape[0]] = new_img
        new_img = b_img
    return new_img
        
def manipulate_object(object_path, object_colour, max_disp = 600):

    """
    Function to manipulate the object before creating the ishihara disc
    Args:
        object_path: The path to the object image
        max_disp: The size of the display image.
    Returns:
        img: Numpy array with the transformed object
    """    

    ## Load the object
    image = Image.open(object_path)
    #image = image.convert('1')
    #image = image.convert('RGBA')

    ## Resize image
    #print(image.size)
    #cv2.imshow('Image', image)
    image = image.resize((max_disp, max_disp), Image.ANTIALIAS)
    img = np.asarray(image).astype(float)
    
    #img = np.zeros((int(max_disp), int(max_disp)))
    ## Need two images, one to manipulate and one to display
    new_img = np.copy(img)
    
    help_string = """
            Press:
                r: Rotate the object.
                w,a,s,d: Translate the object.
                i,o: Increase (i) or decrease (o) the size of the object.
                q: Finish.
                Other: Display help.
            """
    
    print(help_string)
    ## Loop while manioulations are performed
    while True:
        #new_img = np.copy(img)
        ## Create a representation of the ishihara disc
        new_img = cv2.circle(new_img, (int(max_disp/2), int(max_disp/2)), int(0.45*max_disp), (1,0,0), thickness=2, lineType=8, shift=0)
        cv2.imshow('Display image', new_img)

        key_press = cv2.waitKey(0)
        
        ## Rotate the object
        if key_press == ord('r'):
            img = np.rot90(img)
            new_img = np.copy(img)
        ## Translate the object
        elif key_press in [ord('w'), ord('a'), ord('s'), ord('d')]:
            img = shift_image(key_press, img)
            new_img = np.copy(img)
        ## Increase/decrease the size of the object
        elif key_press in [ord('i'), ord('o')]:
            img = change_size(key_press, img, max_disp, object_colour)
            new_img = np.copy(img)
        elif key_press == ord('q'):
            break
        else:
            print(help_string)
    cv2.destroyAllWindows()
    
    return img







