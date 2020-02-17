import colorsys

import cv2
import numpy as np


def rgb_conversion(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


def mandelbrot(x, y):
    c0 = np.complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conversion(i)
        c = c * c + c0
    return 0, 0, 0


def draw_fractal(width):
    blank_image = np.zeros((width // 2, width, 3), np.uint8)
    for x in range(blank_image.shape[1]):
        for y in range(blank_image.shape[0]):
            blank_image[y, x] = mandelbrot((x - (0.75 * width)) / (width / 4),
                                           (y - (width / 4)) / (width / 4))
    return blank_image


if __name__ == "__main__":
    WIDTH = 1024
    cv2.imshow("mandelbrot", draw_fractal(WIDTH))
    while True:
        k = cv2.waitKey(33)
        if k == 32:  # Space key to stop
            break
