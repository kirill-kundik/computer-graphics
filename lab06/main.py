import cv2

from lab06.model import Model

if __name__ == "__main__":
    width = 600
    height = 600

    torus_translate = [200, 200, 0]
    torus = Model(R=160, r=40, torus_translate=torus_translate)

    rendered_frames = torus.draw(
        frames_count=360,
        width=width,
        height=height
    )

    while True:
        for f in rendered_frames:
            cv2.imshow('torus', f)
            cv2.waitKey(2)
