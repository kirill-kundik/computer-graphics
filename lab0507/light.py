import numpy as np

from lab0507.utils import LIGHT_VECTOR, VIEW_DIR, AMBIENT_COEFF, DIFFUSE_COEFF, SPECULAR_COEFF


def get_lighten_color(face, original_color):
    v1, v2, v3 = face
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    x3, y3, z3 = v3

    # diffuse
    normal_vector: np.ndarray = np.array([
        (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1),
        (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1),
        (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    ])

    normal_vector = normal_vector / np.linalg.norm(normal_vector)

    diffuse_light = max(LIGHT_VECTOR.dot(normal_vector), 0.0)

    # specular
    reflect_dir = 2 * normal_vector * (
            normal_vector.dot(LIGHT_VECTOR) / normal_vector.dot(normal_vector)
    ) - LIGHT_VECTOR

    specular_light = pow(max(VIEW_DIR.dot(reflect_dir), 0.0), 32)

    return tuple(
        min(255, int(
            c * (AMBIENT_COEFF + DIFFUSE_COEFF * diffuse_light + SPECULAR_COEFF * specular_light)
        )) for c in original_color
    )
