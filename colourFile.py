# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:38:56 2020

@author: johaant
"""

### Store all colours here
import random

def get_colour(colour_type, foreground):
    

    red_green = {'Background': ['FFD006', 'EFBD89', 'CC725D', 'F1971C', 'EA9079'],
              'Object': ['A5AF70', '529465', 'C8C78F']}
    
    rgb_converter = lambda x: tuple(float(int(x[i:i+2], 16))/255 for i in (0, 2, 4))

    colour_dict = {'red-green': red_green}

    
    colours = colour_dict[colour_type]
    
    if foreground == False:
        num_col = len(colours['Object'])
        new_colour = colours['Object'][random.randint(0,num_col-1)]
        new_colour = rgb_converter(new_colour)
        return new_colour
    else:
        num_col = len(colours['Background'])
        new_colour = colours['Background'][random.randint(0,num_col-1)]
        new_colour = rgb_converter(new_colour)
        return new_colour
    
    





