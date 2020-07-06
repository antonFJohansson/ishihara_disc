# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:50:46 2020

@author: johaant
"""


from ishiharaDiscFile import create_ishihara_disc, plot_ishihara_disc
from objectContainmentFile import check_object_containment
from displayObjectFile import manipulate_object
from colourFile import convert_object_colour

WIDTH = 1
HEIGHT = 1
PIXEL_SCALE = 1000
num_circles = 720
save_name = 'test_light_2.png'
object_path = 'shrek_2.png'
object_colour = 'black'
colour_scheme = 'red-green'
object_colour = convert_object_colour(object_colour)


x_pos, y_pos, rad = create_ishihara_disc(num_circles = num_circles)
object_img = manipulate_object(object_path, object_colour = object_colour)
object_circles = check_object_containment(x_pos, y_pos, object_img,
                                          object_colour = object_colour)
plot_ishihara_disc(x_pos, y_pos, rad, object_circles, colour_scheme, save_name = save_name)



## And now in the last step we would maybe like to just see that our object will look nice when we load it
## So maybe easiest to see that the image will be loaded in openCv into a np array or something

## So tomorrow just add comments and function help
## And then make it so that I can present it and put it on my website?
## And maybe some more colour schemes


#import matplotlib.pyplot as plt
#plt.imshow(data)









