import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array):
    '''Invert the color of the image received.'''
    #your code here
    inverted_array = array.copy()
    inverted_array = 255 - inverted_array
    image = Image.fromarray(inverted_array)
    image.show()
    return inverted_array
def ft_red(array):
    '''Reds the color of the image received.'''
    red_array = array.copy()
    red_array[:,:,1] = 0
    red_array[:,:,2] = 0
    image = Image.fromarray(red_array)
    image.show()
    return red_array
    #your code here
def ft_green(array):
    '''Greens the color of the image received.'''
    #your code here
    green_array = array.copy()
    green_array[:,:,0] = 0
    green_array[:,:,2] = 0
    image = Image.fromarray(green_array)
    image.show()
    return green_array
def ft_blue(array):
    '''Blues the color of the image received.'''
    #your code here
    blue_array = array.copy()
    blue_array[:,:,0] = 0
    blue_array[:,:,1] = 0
    image = Image.fromarray(blue_array)
    image.show()
    return blue_array
def ft_grey(array):
    '''Greys the color of the image received.'''
    #your code here
    grey_array = array.copy()
    gray_scale = 0.3 * grey_array[:,:,0] + 0.59 * grey_array[:,:,1] + 0.11 * grey_array[:,:,2]
    grey_array[:,:,0] = gray_scale
    grey_array[:,:,1] = gray_scale
    grey_array[:,:,2] = gray_scale
    image = Image.fromarray(grey_array)
    image.show()
    return grey_array


# def ft_invert(array) -> array:
#     #your code here
#     return array
# def ft_red(array) -> array:
#     '''Reds the color of the image received.'''
#     #your code here
#     return array
# def ft_green(array) -> array:
#     '''Greens the color of the image received.'''
#     #your code here
#     return array
# def ft_blue(array) -> array:
#     '''Blues the color of the image received.'''
#     #your code here
#     return array
# def ft_grey(array) -> array:
#     '''Greys the color of the image received.'''
#     #your code here
#     return array