import numpy as np

LIGHT_VECTOR = np.array((0., -1., 0.))
VIEW_DIR = np.array((0., 0., -1.))
AMBIENT_COEFF = .1
DIFFUSE_COEFF = .8
SPECULAR_COEFF = 20


class EventOnRender:
    def __init__(self, source, **attrs):
        self.source = source
        self.attrs = attrs


def translate(vertex, vector):
    return (np.array(vertex) + np.array(vector)).tolist()


def circle(r, vertices_count):
    for i in range(vertices_count):
        angle = 2 * np.pi * i / vertices_count
        yield int(r * np.cos(angle)), int(r * np.sin(angle)), 0


def move_cycle(arr: list):
    copy = arr[1:]
    return copy + [arr[0]]


def scale_pixel(x, y, _z, width, height, min_x, max_x, min_y, max_y):
    scale = (min(width, height) - 1) / min((max_x - min_x), (max_y - min_y))

    canvas_x = int((x - min_x) * scale)
    canvas_y = int((y - min_y) * scale)

    return canvas_x, height - 1 - canvas_y


def project_with_angle(v, theta_x, theta_y, theta_z):
    arr: np.ndarray = np.array(
        # X
        [[1, 0, 0],
         [0, np.cos(-theta_x), -np.sin(-theta_x)],
         [0, np.sin(-theta_x), np.cos(-theta_x)]],
    ).dot(
        # Y
        np.array([
            [np.cos(-theta_y), 0, np.sin(-theta_y)],
            [0, 1, 0],
            [-np.sin(-theta_y), 0, np.cos(-theta_y)]
        ])
    ).dot(
        # Z
        np.array([
            [np.cos(-theta_z), -np.sin(-theta_z), 0],
            [np.sin(-theta_z), np.cos(-theta_z), 0],
            [0, 0, 1]
        ])
    ).dot(
        np.transpose(np.array(v))
    )
    return arr.tolist()


def get_z_order(face):
    (v1, v2, v3), *_ = face
    return v1[2] + v2[2] + v3[2]
