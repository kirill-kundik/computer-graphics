import pathlib
from time import time

import cv2
import numpy as np

from lab0507.light import get_lighten_color
from lab0507.model import Model
from lab0507.utils import scale_pixel, get_z_order, project_with_angle

if __name__ == "__main__":
    PROJECT_ROOT = pathlib.Path(__file__).parent.parent
    path = PROJECT_ROOT / "examples" / "lab02" / "african_head.obj"

    frames_count = 360

    width = 500
    height = 800

    min_x, max_x = 200, -200
    min_y, max_y = 200, -200
    min_z, max_z = 200, -200

    model = Model(path, min_x, max_x, min_y, max_y, min_z, max_z)

    theta_x = 0
    theta_z = 0
    frames = []
    origin = [0, 1, 0]

    for theta_y in range(0, frames_count):
        print(f'\rrendering: {theta_y + 1} out of {frames_count} frames', end='')
        theta_z += 1.
        theta_x += 1.

        theta_y_1 = 180 - theta_y

        model_canvas = np.zeros((height, width, 3), dtype=np.uint8)

        rotated_faces = [
            ([
                 project_with_angle(v, theta_x, theta_y_1, theta_z, origin)
                 for v in vs
             ], c)
            for (vs, c) in model.faces
        ]

        ordered_faces = reversed(sorted(rotated_faces, key=get_z_order))

        for face in ordered_faces:
            (v1, v2, v3), color = face

            to_scale_v1 = (*v1, width, height, model.min_x, model.max_x, model.min_y, model.max_y)
            to_scale_v2 = (*v2, width, height, model.min_x, model.max_x, model.min_y, model.max_y)
            to_scale_v3 = (*v3, width, height, model.min_x, model.max_x, model.min_y, model.max_y)

            x1, y1 = scale_pixel(*to_scale_v1)
            x2, y2 = scale_pixel(*to_scale_v2)
            x3, y3 = scale_pixel(*to_scale_v3)

            cv2.line(model_canvas, (x1, y1), (x2, y2), color=(163, 142, 86))
            cv2.line(model_canvas, (x1, y1), (x3, y3), color=(163, 142, 86))
            cv2.line(model_canvas, (x2, y2), (x3, y3), color=(163, 142, 86))

            cv2.drawContours(
                model_canvas,
                [np.array([[x1, y1], [x2, y2], [x3, y3]])],
                0,
                get_lighten_color((v1, v2, v3), color),
                -1
            )

        frames.append(model_canvas)

    while True:
        for frame in frames + list(reversed(frames)):
            start = int(time() * 1000)
            cv2.imshow('model', frame)
            end = int(time() * 1000)
            cv2.waitKey(max(1, 16 - (start - end)))
