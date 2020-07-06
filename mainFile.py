# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:50:46 2020

@author: johaant
"""


from ishiharaDiscFile import create_ishihara_disc, plot_ishihara_disc
from objectContainmentFile import check_object_containment
from displayObjectFile import manipulate_object
from colourFile import convert_object_colour


## Final resolution of the image
PIXEL_SCALE = 1000
## Num circles in the given disc
num_circles = 720

## Save name of the final image
save_name = 'final_ishihara_disc.png'
## Path to the binary image with the object
object_path = 'my_object.png'
## The colour of the object (black/white)
object_colour = 'black'
## Colour scheme, the ones possible are
##      red-green , dark-green-red and dark-blue-red
colour_scheme = 'red-green'

## Convert colour to binary digit
object_colour = convert_object_colour(object_colour)
## Create Ishihara disc
x_pos, y_pos, rad = create_ishihara_disc(num_circles = num_circles)
## Obtain binary object image
object_img = manipulate_object(object_path, object_colour = object_colour)
## Obtain which circles should represent the object
object_circles = check_object_containment(x_pos, y_pos, object_img,
                                          object_colour = object_colour)
## Plot and save the Ishihara_disc
plot_ishihara_disc(x_pos, y_pos, rad, object_circles, colour_scheme, save_name = save_name)









