import pathlib
import random

import cv2
import numpy as np

from lab03 import model, mycv

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def face_model():
    african_head_obj_path = PROJECT_ROOT / "examples" / "lab02" / "african_head.obj"
    m = model.Model(african_head_obj_path)

    height, width = 800, 800
    blank_image = np.zeros((height, width, 3), np.uint8)
    cv2_image = np.zeros((height, width, 3), np.uint8)

    # mycv.triangle(442, 457, 429, 446, 442, 450, blank_image, (255, 255, 255))
    # cv2.imshow("x", blank_image)
    # return

    for face in m.faces:
        x0, y0, _ = m.vertices[face[0] - 1]
        x1, y1, _ = m.vertices[face[1] - 1]
        x2, y2, _ = m.vertices[face[2] - 1]

        x0 = (x0 + 1.) * width / 2.
        y0 = abs(height - (y0 + 1.) * height / 2.)
        x1 = (x1 + 1.) * width / 2.
        y1 = abs(height - (y1 + 1.) * height / 2.)
        x2 = (x2 + 1.) * width / 2.
        y2 = abs(height - (y2 + 1.) * height / 2.)

        if x0 == width:
            x0 = width - 1
        if x1 == width:
            x1 = width - 1
        if x2 == width:
            x2 = width - 1
        if y0 == height:
            y0 = height - 1
        if y1 == height:
            y1 = height - 1
        if y2 == height:
            y2 = height - 1

        mycv.triangle(mycv.Point(x0, y0), mycv.Point(x1, y1), mycv.Point(x2, y2), blank_image,
                      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # print(int(x0), int(y0), int(x1), int(y1), int(x2), int(y2))
        # mycv.triangle(mycv.Point(x0, y0), mycv.Point(x1, y1), mycv.Point(x2, y2), blank_image, (255, 255, 255))
        # cv2.imshow("mycv", blank_image)
        # while True:
        #     k = cv2.waitKey(33)
        #     if k == 32:  # Space key to stop
        #         break

        cv2.drawContours(cv2_image, [np.array([(int(x0), int(y0)), (int(x1), int(y1)), (int(x2), int(y2))])], 0,
                         (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), -1)

    cv2.imshow("mycv", blank_image)
    cv2.imshow("cv2", cv2_image)


if __name__ == "__main__":
    face_model()

    while True:
        k = cv2.waitKey(33)
        if k == 32:  # Space key to stop
            break
