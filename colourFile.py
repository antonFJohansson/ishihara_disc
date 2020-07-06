# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:38:56 2020

@author: johaant
"""

### Store all colours here
import random

def convert_object_colour(col):
    
    """
    Convert the object colour to the correct binary digit
    """
    
    if col == 'black':
        return 0
    elif col == 'white':
        return 1
    else:
        'The allowed colours are white and black'


def get_colour(colour_type, foreground):
    
    """
    Function to retrieve colour schemes for the ishihara discs.
    Args:
        colour_type: Which colour scheme to use (String)
        foreground: If the current circle represents the object or not
    Returns:
        A random colour from the colour scheme.
    """
    

    red_green = {'Background': ['FFD006', 'EFBD89', 'CC725D', 'F1971C', 'EA9079'],
              'Object': ['A5AF70', '529465', 'C8C78F']}
    dark_green_red = {'Background': ['796D45', '544F36', 'AD954E', '79794B', 'B29651'],
              'Object': ['EE6434', 'D95135', 'FE8551', 'F97062', 'F2834C']}
    
    dark_blue_red = {'Background': ['96A38E', '555A56', '454A46', '97A38F', '6D756E'],
              'Object': ['D17E65', 'DC9F8C', 'B77B78', 'D7474E', '865862']}
    
    rgb_converter = lambda x: tuple(float(int(x[i:i+2], 16))/255 for i in (0, 2, 4))

    colour_dict = {'red-green': red_green, 'dark-green-red': dark_green_red, 'dark-blue-red': dark_blue_red}

    
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
    
    





