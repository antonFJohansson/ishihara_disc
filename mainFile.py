# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:50:46 2020

@author: johaant
"""


from ishiharaDiscFile import create_ishihara_disc, plot_ishihara_disc
from objectContainmentFile import check_object_containment
from displayObjectFile import manipulate_object

WIDTH = 1
HEIGHT = 1
PIXEL_SCALE = 1000
num_circles = 720
save_name = 'ishihara_disc_1.png'
object_path = 'object_img.PNG'

x_pos, y_pos, rad = create_ishihara_disc(num_circles = num_circles)
object_img = manipulate_object(object_path)
object_circles = check_object_containment(x_pos, y_pos, object_img)
plot_ishihara_disc(x_pos, y_pos, rad, object_circles, save_name = save_name)

## And now in the last step we would maybe like to just see that our object will look nice when we load it
## So maybe easiest to see that the image will be loaded in openCv into a np array or something




#import matplotlib.pyplot as plt
#plt.imshow(data)









