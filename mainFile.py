# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:50:46 2020

@author: johaant
"""


from ishiharaDiscFile import create_ishihara_disc, plot_ishihara_disc
from objectContainmentFile import check_object_containment

WIDTH = 1
HEIGHT = 1
PIXEL_SCALE = 1000
num_circles = 720
save_name = 'ishihara_disc.png'
object_path = 'object_img_2.PNG'

x_pos, y_pos, rad = create_ishihara_disc(num_circles = num_circles)
object_circles = check_object_containment(x_pos, y_pos, object_path)
plot_ishihara_disc(x_pos, y_pos, rad, object_circles, save_name = save_name)

#import matplotlib.pyplot as plt
#plt.imshow(data)









