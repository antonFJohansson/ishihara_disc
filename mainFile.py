# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:50:46 2020

@author: johaant
"""


from ishiharaDiscFile import create_ishihara_disc, plot_ishihara_disc

WIDTH = 1
HEIGHT = 1
PIXEL_SCALE = 1000
save_name = 'ishihara_disc.png'

x_pos, y_pos, rad = create_ishihara_disc()

plot_ishihara_disc(x_pos, y_pos, rad, save_name = save_name)





