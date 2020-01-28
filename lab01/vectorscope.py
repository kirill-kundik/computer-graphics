import os
import pathlib

import numpy as np
import cv2

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:, :, [1, 2]] += 128
    ycbcr[:, :, [0]] += 16
    return ycbcr


def draw_vectoroscope(ycbcr, out_size, vec_name=""):
    im = np.zeros((out_size, out_size, 3), np.uint8)
    height, width, channels = ycbcr.shape

    line_color = (0, 0, 125)

    cv2.line(im, (out_size // 2, 0), (out_size // 2, out_size), line_color, 1)
    cv2.line(im, (0, out_size // 2), (out_size, out_size // 2), line_color, 1)
    cv2.circle(im, (out_size // 2, out_size // 2), out_size // 2, line_color, thickness=1)

    for i in range(height):
        for j in range(width):
            y = ycbcr.item(i, j, 0)
            cr = ycbcr.item(i, j, 1)
            cb = ycbcr.item(i, j, 2)
            new_i = out_size - int(cr / 255.0 * out_size)
            new_j = int(cb / 255.0 * out_size)
            im.itemset((new_i, new_j, 1), y)

    cv2.imshow(f"vectorscope{'_' + vec_name if vec_name else ''}", im)


if __name__ == "__main__":
    # img_name = "original.tif"
    img_name = "pony.jpg"
    img_path = PROJECT_ROOT / "examples" / img_name

    img = cv2.imread(str(img_path))
    cv2.imshow("origin", img)

    ycbcr = rgb2ycbcr(img)

    draw_vectoroscope(ycbcr, 512)

    temp_img = "temp.png"

    cv2.imwrite(temp_img, ycbcr)
    img = cv2.imread(temp_img)
    os.remove(temp_img)

    cv2.imshow("ycbcr", img)

    ycbcr = rgb2ycbcr(img)

    draw_vectoroscope(ycbcr, 512, vec_name="ycbcr")

    cv2.waitKey(0)
