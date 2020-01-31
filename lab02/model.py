from typing import List, Tuple


class Model:
    def __init__(self, file_path: str):
        self._file_path: str = file_path
        self.vertices: List[Tuple] = []
        self.faces: List[Tuple] = []

        self._parse()

    def _parse(self):
        with open(self._file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    self.vertices.append(tuple(map(float, line[2:].split(" "))))
                elif line.startswith("f "):
                    self.faces.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
