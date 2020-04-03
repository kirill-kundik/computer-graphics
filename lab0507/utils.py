import numpy as np

LIGHT_VECTOR = np.array((0., -1., 0.))
VIEW_DIR = np.array((0., 0., -1.))
AMBIENT_COEFF = .1
DIFFUSE_COEFF = .8
SPECULAR_COEFF = 20


def scale_pixel(x, y, _z, width, height, min_x, max_x, min_y, max_y):
    scale = (min(width, height) - 1) / min((max_x - min_x), (max_y - min_y))

    canvas_x = int((x - min_x) * scale)
    canvas_y = int((y - min_y) * scale)

    return canvas_x, height - 1 - canvas_y


def project_with_angle(v, theta_x, theta_y, theta_z, origin=(0, 0, 0)):
    arr = np.array(
        # X
        [[1, 0, 0],
         [0, np.cos(np.radians(-theta_x)), -np.sin(np.radians(-theta_x))],
         [0, np.sin(np.radians(-theta_x)), np.cos(np.radians(-theta_x))]],
    ).dot(
        # Y
        np.array([
            [np.cos(np.radians(-theta_y)), 0, np.sin(np.radians(-theta_y))],
            [0, 1, 0],
            [-np.sin(np.radians(-theta_y)), 0, np.cos(np.radians(-theta_y))]
        ])
    ).dot(
        # Z
        np.array([
            [np.cos(np.radians(-theta_z)), -np.sin(np.radians(-theta_z)), 0],
            [np.sin(np.radians(-theta_z)), np.cos(np.radians(-theta_z)), 0],
            [0, 0, 1]
        ])
    ).dot(
        np.transpose(np.array(v) - np.array(origin))
    ) + np.array(origin)

    return arr[0], arr[1], arr[2]


def get_z_order(face):
    (v1, v2, v3), *_ = face
    return v1[2] + v2[2] + v3[2]
