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
    
    if shift_key == ord('w'):
        img=np.roll(img, -1, axis = 0)
    elif shift_key == ord('s'):
        img=np.roll(img, 1, axis = 0)
    elif shift_key == ord('a'):
        img=np.roll(img, -1, axis = 1)
    elif shift_key == ord('d'):
        img=np.roll(img, 1, axis = 1)
    return img


def manipulate_object(object_path):

    image = Image.open(object_path)
    #image = image.convert('1')
    max_disp = max(image.size) if max(image.size) < 600 else 600
    
    ## Reshape it to a square shape
    if image.size[0] != image.size[1]:
    
        image = image.resize((max_disp, max_disp), Image.ANTIALIAS)
    
    img = np.asarray(image).astype(float)
    
    #img = np.zeros((int(max_disp), int(max_disp)))
    new_img = np.copy(img)
    
    while True:
        #new_img = np.copy(img)
        new_img = cv2.circle(new_img, (int(max_disp/2), int(max_disp/2)), int(0.45*max_disp), (1,0,0), thickness=2, lineType=8, shift=0)
        cv2.imshow('Image', new_img)
        #print('aaaa')
        key_press = cv2.waitKey(0)
        
        if key_press == ord('r'):
            img = np.rot90(img)
            new_img = np.copy(img)
        elif key_press in [ord('w'), ord('a'), ord('s'), ord('d')]:
            img = shift_image(key_press, img)
            new_img = np.copy(img)
        else:
            break
    cv2.destroyAllWindows()
    
    return img

## I can just try and save down the image here first
## And then create my ishihara disc to see that it all works





    
cv2.destroyAllWindows() # destroys the window showing image







