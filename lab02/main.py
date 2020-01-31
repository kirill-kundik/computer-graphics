import pathlib

import cv2
import numpy as np

from lab02 import model, mycv

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def face_model():
    african_head_obj_path = PROJECT_ROOT / "examples" / "lab02" / "african_head.obj"
    m = model.Model(african_head_obj_path)

    height, width = 800, 800

    lines = []

    for face in m.faces:
        for i in range(3):
            x0, y0, _ = m.vertices[face[i] - 1]
            x1, y1, _ = m.vertices[face[(i + 1) % 3] - 1]

            x0 = (x0 + 1.) * width / 2.
            y0 = (y0 + 1.) * height / 2.
            x1 = (x1 + 1.) * width / 2.
            y1 = (y1 + 1.) * height / 2.

            if x0 == width:
                x0 = width - 1
            if x1 == width:
                x1 = width - 1
            if y0 == height:
                y0 = height - 1
            if y1 == height:
                y1 = height - 1

            lines.append((int(x0), int(y0), int(x1), int(y1)))
    return {
        "lines": lines
    }


def sun_model():
    return {
        "lines": [
            (500, 400, 750, 400),
            (50, 400, 300, 400),
            (400, 500, 400, 750),
            (400, 50, 400, 300),
            (470, 470, 750, 750),
            (345, 480, 50, 750),
            (345, 315, 50, 50),
            (470, 320, 750, 50),
            (400, 350, 450, 400),
            (450, 400, 400, 450),
            (750, 70, 720, 100),
            (750, 70, 780, 100),
            (750, 70, 750, 100),
            (720, 120, 720, 150),
            (720, 135, 780, 135),
            (750, 350, 720, 380),
            (750, 350, 780, 380),
            (780, 400, 720, 430),
            (780, 460, 720, 430),
            (750, 415, 750, 445),
            (750, 470, 750, 500),
            (720, 470, 780, 470),
            (720, 500, 780, 500),
            (735, 520, 720, 550),
            (735, 520, 750, 550),
            (780, 520, 750, 550),
            (720, 550, 780, 550),
        ],
        "circles": [
            (400, 400, 100),
            (350, 350, 10),
            (350, 450, 10),
            (750, 200, 30),
        ],
    }


def draw_model(m, win_name="origin", rot=False, color=(0, 255, 255)):  # yellow
    height, width = 800, 800
    blank_image = np.zeros((height, width, 3), np.uint8)

    for line in m.get("lines", []):
        mycv.line(*line, blank_image, color)

    for circle in m.get("circles", []):
        mycv.circle(*circle, blank_image, color)

    if rot:
        blank_image = np.rot90(blank_image, 1)

    cv2.imshow(win_name, blank_image)


def draw_cv(m, win_name="origin", rot=0, color=(0, 255, 255)):  # yellow
    height, width = 800, 800
    blank_image = np.zeros((height, width, 3), np.uint8)
    for (x1, y1, x2, y2) in m.get("lines", []):
        cv2.line(blank_image, (x1, y1), (x2, y2), color)

    for (x, y, radius) in m.get("circles", []):
        cv2.circle(blank_image, (x, y), radius, color)

    if rot:
        blank_image = np.rot90(blank_image, rot)

    cv2.imshow(win_name, blank_image[::-1])


if __name__ == "__main__":
    draw_model(sun_model(), "my lines and circles")
    draw_model(face_model(), "my head model", True, (255, 255, 255))
    draw_cv(face_model(), "cv head model", 0, (255, 255, 255))
    draw_cv(sun_model(), "cv lines and circles", 1)

    while True:
        k = cv2.waitKey(33)
        if k == 32:  # Space key to stop
            break
