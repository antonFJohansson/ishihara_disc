# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:24:26 2020

@author: johaant
"""
import cairo
from colourFile import get_colour
import math
PIXEL_SCALE = 1000
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             PIXEL_SCALE,
                             PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

## Make background white
ctx.rectangle(0, 0, PIXEL_SCALE, PIXEL_SCALE)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()


ctx.arc(0.3, 0.3, 0.181, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(0,0,0)
ctx.fill()

ctx.arc(0.3, 0.3, 0.177, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(1,1,1)
ctx.fill()

## Main blue
ctx.arc(0.3, 0.3, 0.15, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', 'foreground'))
ctx.fill()




## Overlapping red
ctx.arc(0.42, 0.3, 0.07, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', 'foreground'))
ctx.fill()


## Small red
ctx.arc(0.15, 0.15, 0.03, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', 'foreground'))
ctx.fill()

## Green below
ctx.arc(0.46, 0.467, 0.05, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', 'foreground'))
ctx.fill()


## Green big
ctx.arc(0.7, 0.3, 0.15, 0, math.pi*2)
ctx.close_path()
ctx.set_source_rgba(*get_colour('red-green', 'foreground'))
ctx.fill()


ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.28, 0.31)
ctx.set_source_rgba(0,0,0)
ctx.show_text("A")

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.41, 0.31)
ctx.set_source_rgba(0,0,0)
ctx.show_text("B")

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.135, 0.162)
ctx.set_source_rgba(0,0,0)
ctx.show_text("C")

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.445, 0.48)
ctx.set_source_rgba(0,0,0)
ctx.show_text("D")

ctx.set_font_size(0.04)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.68, 0.31)
ctx.set_source_rgba(0,0,0)
ctx.show_text("E")








plot_centers = False
if plot_centers:
    ctx.arc(0.6, 0.55, 0.004, 0, math.pi*2)
    ctx.close_path()
    ctx.set_source_rgba(0,0,0)
    ctx.fill()
    
    ctx.arc(0.3, 0.5321, 0.004, 0, math.pi*2)
    ctx.close_path()
    ctx.set_source_rgba(0,0,0)
    ctx.fill()
    
    ctx.arc(0.15, 0.15, 0.004, 0, math.pi*2)
    ctx.close_path()
    ctx.set_source_rgba(0,0,0)
    ctx.fill()
    
    ctx.arc(0.42, 0.3, 0.004, 0, math.pi*2)
    ctx.close_path()
    ctx.set_source_rgba(0,0,0)
    ctx.fill()
    
    ctx.arc(0.3, 0.3, 0.004, 0, math.pi*2)
    ctx.close_path()
    ctx.set_source_rgba(0,0,0)
    ctx.fill()


surface.write_to_png('test_plot_2.png')



