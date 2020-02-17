import cv2

import numpy as np


def draw_fractal(w, h):
    zoom = 1
    blank_image = np.zeros((h, w, 3), np.uint8)

    c_x, c_y = -0.7, 0.27015
    move_x, move_y = 0.0, 0.0
    max_iter = 255

    for x in range(w):
        for y in range(h):
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + move_x
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + move_y
            i = max_iter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + c_x
                zy, zx = 2.0 * zx * zy + c_y, tmp
                i -= 1

            blank_image[y, x] = (i << 21) + (i << 10) + i * 8

    return blank_image


if __name__ == "__main__":
    cv2.imshow("julia", draw_fractal(1080, 720))

    while True:
        k = cv2.waitKey(33)
        if k == 32:  # Space key to stop
            break
