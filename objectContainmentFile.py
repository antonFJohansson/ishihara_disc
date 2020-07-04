# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:04:18 2020

@author: johaant
"""
from numpy import asarray
from PIL import Image

class contained_pixel():
     
    def __init__(self, object_path, object_colour):

        image = Image.open(object_path)
        image = image.convert('1')
        self.max_side = max(image.size)
        self.valid_pos = lambda x: int(x) if x < self.max_side else self.max_side - 1
        ## Reshape it to a square shape
        if image.size[0] != image.size[1]:
        
            image = image.resize((self.max_side, self.max_side), Image.ANTIALIAS)
            
        ## Convert to numpy array
        self.img = asarray(image)
        self.object_colour = object_colour
    
    def check_pixel_containment(self, x, y):
        curr_x, curr_y = self.max_side*x, self.max_side*y
        pixel_x, pixel_y = round(curr_x), round(curr_y)
        pixel_x, pixel_y = self.valid_pos(pixel_x), self.valid_pos(pixel_y)
        
        pixel_store = []
        surr_pixels = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        for x_step, y_step in surr_pixels:
            new_pixel_x = pixel_x + x_step
            new_pixel_y = pixel_y + y_step
            new_pixel_x, new_pixel_y = self.valid_pos(new_pixel_x), self.valid_pos(new_pixel_y)
            pixel_store.append(self.img[new_pixel_x, new_pixel_y] == self.object_colour)
        
        return all(pixel_store)


def check_object_containment(x_pos, y_pos, object_path, object_colour = 0):
    
    object_prop = contained_pixel(object_path, object_colour)
    
    
    object_circle_store = asarray(x_pos.shape[0]*[-1.])
    
    for iii in range(x_pos.shape[0]):
        curr_x = x_pos[iii]
        curr_y = y_pos[iii]
        
        ## Check if all pixels around the given one are inside the object

        circle_contained = object_prop.check_pixel_containment(curr_x, curr_y)   
        object_circle_store[iii] = circle_contained
    return object_circle_store
    
        
        
    
    
    
    
    
    