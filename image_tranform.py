import numpy as np
import utils

def rgb2gray_average(rgb_array):
    rows = rgb_array.shape[0]
    cols = rgb_array.shape[1]
    output_array = np.zeros([rows, cols], dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            pixel = utils.Pixel(rgb_array[i, j])
            output_array[i, j] = (pixel.r + pixel.g + pixel.b) / 3

    return output_array


def rgb2gray_lightness(rgb_array):

    # TODO: Your code here

    return np.zeros([1, 1], dtype=np.uint8)


def rgb2gray_luminosity(rgb_array):

    # TODO: Your code here

    return np.zeros([1, 1], dtype=np.uint8)


def rgb2gray_custom(rgb_array):

    # TODO: Your code here

    return np.zeros([1, 1], dtype=np.uint8)


def windowing_16bit(array_16bit, min_value, max_value):

    # TODO: Your code here

    return np.zeros([1, 1], dtype=np.uint8)

def resize(grayscale_array, resize_factor):

    # TODO: Your code here

    return np.zeros([1, 1], dtype=np.uint8)

# Source: https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
