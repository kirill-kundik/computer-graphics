from random import randint
from typing import List, Tuple


class Model:
    def __init__(self, file_path: str, min_x, max_x, min_y, max_y, min_z, max_z):
        self._file_path: str = file_path
        self.vertices: List[Tuple] = []
        self.faces: List[Tuple] = []

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z

        self._parse()

    def _parse(self):
        with open(self._file_path, 'r') as input_file:
            for i, line in enumerate(input_file):
                if line.startswith('v '):
                    x, y, z = [float(n) for n in line.split(' ')[1:]]

                    self.vertices.append((x, y, z))

                    self.min_x, self.max_x = min(self.min_x, x), max(self.max_x, x)
                    self.min_y, self.max_y = min(self.min_y, y), max(self.max_y, y)
                    self.min_z, self.max_z = min(self.min_z, z), max(self.max_z, z)
                elif line.startswith('f '):
                    f1, f2, f3 = line.split(' ')[1:]

                    vi1, vi2, vi3 = [int(f.split('/')[0]) - 1 for f in [f1, f2, f3]]

                    self.faces.append(
                        (
                            (tuple(self.vertices[vi] for vi in [vi1, vi2, vi3])),
                            (randint(0, 255), randint(0, 255), randint(0, 255))
                        )
                    )
