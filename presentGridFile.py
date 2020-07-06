# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:23:27 2020

@author: johaant
"""

import cairo
from colourFile import get_colour
import math
PIXEL_SCALE = 1000
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             PIXEL_SCALE,
                             PIXEL_SCALE//2)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

## Make background white
ctx.rectangle(0, 0, PIXEL_SCALE, PIXEL_SCALE)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()


# ctx.arc(0.3, 0.3, 0.181, 0, math.pi*2)
# ctx.close_path()
# ctx.set_source_rgba(0,0,0)
# ctx.fill()

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.1, 0.04)
ctx.set_source_rgba(0,0,0)
ctx.show_text("Colour Assignment")

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.7, 0.04)
ctx.set_source_rgba(0,0,0)
ctx.show_text("Result")

## Dividing rectable
ctx.rectangle(0.5, 0, 0.005, 0.52)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

### VERTICAL LINES
init_height = 0.14
delta_x = 0.08
start_x = 0.1
h = 0.32
ctx.rectangle(start_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x + delta_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x + 2*delta_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x + 3*delta_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x + 4*delta_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

### HOR LINES
init_height = 0.14
delta_y = 0.08
start_x = 0.1
w = 0.32
ctx.rectangle(start_x, init_height, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x, init_height + delta_y, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x, init_height + 2*delta_y, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x, init_height + 3*delta_y, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

ctx.rectangle(start_x, init_height + 4*delta_y, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()
########################


### Pixel colour
ctx.rectangle(0.342, 0.382, 0.078, 0.078)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

ctx.rectangle(0.342, 0.302, 0.078, 0.078)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

ctx.rectangle(0.342, 0.222, 0.078, 0.078)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

ctx.rectangle(0.262, 0.222, 0.078, 0.078)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

ctx.rectangle(0.182, 0.302, 0.078, 0.078)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()

######
## Center position

# ctx.arc(0.14, 0.18, 0.002, 0, math.pi*2)
# ctx.close_path()
# ctx.set_source_rgb(0,0,0)
# ctx.fill()

# ctx.arc(0.22, 0.18, 0.002, 0, math.pi*2)
# ctx.close_path()
# ctx.set_source_rgb(0,0,0)
# ctx.fill()

# ctx.arc(0.14, 0.26, 0.002, 0, math.pi*2)
# ctx.close_path()
# ctx.set_source_rgb(0,0,0)
# ctx.fill()

## Center text
ctx.set_font_size(0.015)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.125, 0.17)
ctx.set_source_rgba(0,0,0)
ctx.show_text("(0,0)")

ctx.set_font_size(0.015)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.205, 0.17)
ctx.set_source_rgba(0,0,0)
ctx.show_text("(0,1)")

ctx.set_font_size(0.015)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.125, 0.25)
ctx.set_source_rgba(0,0,0)
ctx.show_text("(1,0)")


## Pixel centers here
##1##
ctx.move_to(0.135, 0.175)
ctx.line_to(0.145, 0.185)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()

ctx.move_to(0.145, 0.175)
ctx.line_to(0.135, 0.185)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()
##1##
##2##
ctx.move_to(0.215, 0.175)
ctx.line_to(0.225, 0.185)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()

ctx.move_to(0.225, 0.175)
ctx.line_to(0.215, 0.185)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()
##2##
##3##
ctx.move_to(0.135, 0.255)
ctx.line_to(0.145, 0.265)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()

ctx.move_to(0.145, 0.255)
ctx.line_to(0.135, 0.265)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()
##3##


## Circle centers here

ctx.arc(0.2, 0.2, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.4, 0.17, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.40, 0.35, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.33, 0.36, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

### THIS ONE
ctx.arc(0.39, 0.28, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.29, 0.27, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.17, 0.39, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()


## Legend
ctx.arc(0.13, 0.07, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()
ctx.set_font_size(0.02)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.145, 0.076)
ctx.set_source_rgba(0,0,0)
ctx.show_text("Circle center")





ctx.move_to(0.125, 0.09)
ctx.line_to(0.135, 0.1)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()

ctx.move_to(0.135, 0.09)
ctx.line_to(0.125, 0.1)

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.002)
ctx.stroke()
ctx.set_font_size(0.02)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.145, 0.1)
ctx.set_source_rgba(0,0,0)
ctx.show_text("Pixel center")


ctx.rectangle(0.12, 0.11, 0.02, 0.02)
ctx.set_source_rgba(0, 0, 0, 0.5)
ctx.fill()
ctx.set_font_size(0.02)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.145, 0.126)
ctx.set_source_rgba(0,0,0)
ctx.show_text("Object pixel")

#########################
##########################
########################
##########RIGHT SIDE HERE#################################


init_height = 0.14
delta_x = 0.08
start_x = 0.6
h = 0.32
ctx.rectangle(start_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()


ctx.rectangle(start_x + 4*delta_x, init_height, 0.002, h)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()

### HOR LINES
init_height = 0.14
delta_y = 0.08

w = 0.32
ctx.rectangle(start_x, init_height, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()



ctx.rectangle(start_x, init_height + 4*delta_y, w, 0.002)
ctx.set_source_rgba(0, 0, 0)
ctx.fill()


## CIRC CNETERS
from colourFile import get_colour

ctx.arc(0.7, 0.2, 0.05, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', True))
ctx.fill()
ctx.arc(0.7, 0.2, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()


ctx.arc(0.9, 0.17, 0.017, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', True))
ctx.fill()
ctx.arc(0.9, 0.17, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

### BLUE
ctx.arc(0.9, 0.35, 0.017, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', False))
ctx.fill()
ctx.arc(0.9, 0.35, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.83, 0.36, 0.04, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', True))
ctx.fill()
ctx.arc(0.83, 0.36, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

## BLUE
ctx.arc(0.89, 0.28, 0.025, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', False))
ctx.fill()
ctx.arc(0.89, 0.28, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

## BLUE
ctx.arc(0.79, 0.27, 0.043, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', False))
ctx.fill()
ctx.arc(0.79, 0.27, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()


ctx.arc(0.67, 0.39, 0.06, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', True))
ctx.fill()
ctx.arc(0.67, 0.39, 0.003, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()




















surface.write_to_png('grid_plot_1.png')
