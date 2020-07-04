# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:50:27 2020

@author: johaant
"""

import math
import random
from numpy import array, argmin, sqrt
from colourFile import get_colour

def create_ishihara_disc(num_circles = 720, disc_size = 0.42,
                         max_circle_rad = 0.02, min_circle_rad = 0.005,
                         circle_spacing = 0.004):
    
    """
    Function to create the x,y coordinates and the radii for the circles in the ishihara disc
    Args:
        num_circles: The amount of circles.
        disc_size: The size of the ishihara disc
        max_circle_rad: The maximum radius of the circles
        min_circle_rad: Minimum radius of circle
        circle_spacing: The spacing between circles
    """
    
    ## Constants for the image
    WIDTH = 1
    HEIGHT = 1
    
    ## Adjust radius for given height and width
    max_rad = HEIGHT*max_circle_rad
    min_rad = HEIGHT*min_circle_rad
    max_circle = HEIGHT*disc_size 
        
    ##Store x,y and radius of disc
    store_circle_x = array(num_circles*[0.0])
    store_circle_y = array(num_circles*[0.0])
    store_rad = array(num_circles*[0.0])

    num_drawn_circles = 0
    
    ## loop until all circles have been created
    while num_drawn_circles < num_circles:
        
        ## Randomize position of circle
        new_pos_angle = random.random()*math.pi*2
        new_pos_rad = random.random()*max_circle
        new_circle_pos_x = new_pos_rad*math.cos(new_pos_angle) + WIDTH/2
        new_circle_pos_y = new_pos_rad*math.sin(new_pos_angle) + HEIGHT/2
        
        ## If first circle, add it
        if num_drawn_circles == 0:
            new_circle_rad = random.random()*(max_rad - min_rad) + min_rad
            store_circle_x[num_drawn_circles] = new_circle_pos_x
            store_circle_y[num_drawn_circles] = new_circle_pos_y
            store_rad[num_drawn_circles] = new_circle_rad
            num_drawn_circles = num_drawn_circles + 1

        ## For following circles, see that they do not overlap
        else:
            
            ## Calc distance
            dist_x = (store_circle_x[0:num_drawn_circles] - new_circle_pos_x)**2
            dist_y = (store_circle_y[0:num_drawn_circles] - new_circle_pos_y)**2
            min_dist = min(sqrt(dist_x + dist_y) - store_rad[0:num_drawn_circles])
            
            min_dist = 0 if min_dist < 0 else min_dist
            
            
            curr_max_rad = min(max_rad - circle_spacing, min_dist - circle_spacing)
            
            ## Is the circle large enough?
            ## If so store it
            if not curr_max_rad < min_rad:
                new_circle_rad = curr_max_rad
            
                store_circle_x[num_drawn_circles] = new_circle_pos_x
                store_circle_y[num_drawn_circles] = new_circle_pos_y
                store_rad[num_drawn_circles] = new_circle_rad
                num_drawn_circles = num_drawn_circles + 1

            
    return store_circle_x, store_circle_y, store_rad

import cairo
def plot_ishihara_disc(store_circle_x, store_circle_y, store_rad,
                       object_circles, save_name = 'ishihara_disc.png',
                       PIXEL_SCALE = 1000):
    
    
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             PIXEL_SCALE,
                             PIXEL_SCALE)
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE, PIXEL_SCALE)
    ctx.rectangle(0, 0, PIXEL_SCALE, PIXEL_SCALE)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()
            
    for iii in range(store_circle_x.shape[0]):
        ctx.arc(store_circle_x[iii], store_circle_y[iii], store_rad[iii], 0, math.pi*2)
        ctx.close_path()
        if object_circles[iii] == 1:
            new_colour = get_colour('red-green', foreground = False)
            ctx.set_source_rgb(*new_colour)
            ctx.fill()
            
        else:
            new_colour = get_colour('red-green', foreground = True)
            ctx.set_source_rgb(*new_colour)
            ctx.fill()
            
    
    

    surface.write_to_png(save_name)

    







    
