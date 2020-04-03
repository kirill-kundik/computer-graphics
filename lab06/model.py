from random import randint

import cv2
import numpy as np

from lab06.light import get_lighten_color
from lab06.utils import project_with_angle, translate, circle, move_cycle, get_z_order


class Model:
    def __init__(self, R, r, torus_translate, vertices_count=60):
        self.R = R
        self.r = r
        self.vertices_count = vertices_count
        self.torus_translate = torus_translate

        self.faces = []

        self._create_frames()

    def _create_frames(self):
        cut_circles = []
        for i in range(self.vertices_count):
            angle = 2 * np.pi * i / self.vertices_count
            translate_vector = [self.R * np.cos(angle), 0, self.R * np.sin(angle)]
            cut_circles.append(
                [
                    translate(
                        project_with_angle(vertex, theta_y=angle, theta_x=0., theta_z=0.1), translate_vector
                    )
                    for vertex
                    in circle(self.r, self.vertices_count)
                ]
            )
        for circle1, circle2 in zip(cut_circles, move_cycle(cut_circles)):
            for v1, v2, v3, v4 in zip(circle1, move_cycle(circle1), circle2, move_cycle(circle2)):
                self.faces.extend([
                    ((v1, v2, v3), (randint(0, 255), randint(0, 255), randint(0, 255))),
                    ((v2, v4, v3), (randint(0, 255), randint(0, 255), randint(0, 255)))
                ])

    def draw(self, frames_count, width, height):
        frames = []

        for theta_y in range(frames_count):
            print(f'\rrendering: {theta_y + 1} out of {frames_count} frames', end='')

            canvas = np.zeros((height, width, 3), dtype=np.uint8)
            angle = np.radians(theta_y)

            rotated_faces = [
                ([
                     project_with_angle(v, (np.pi / 3), angle, angle)
                     for v in vs
                 ], c)
                for (vs, c) in self.faces
            ]

            translated_faces = [
                ([
                     translate(v, self.torus_translate)
                     for v in vs
                 ], c)
                for (vs, c) in rotated_faces
            ]

            ordered_faces = reversed(sorted(translated_faces, key=get_z_order))

            for vs, original_color in ordered_faces:
                (x1, y1, z1), \
                (x2, y2, z2), \
                (x3, y3, z3) = vs

                lighten_color = get_lighten_color(vs, original_color)

                cv2.drawContours(
                    canvas,
                    [np.array([[int(x1), int(y1)], [int(x2), int(y2)], [int(x3), int(y3)]])],
                    0,
                    lighten_color,
                    -1
                )

            frames.append(canvas)

        return frames
