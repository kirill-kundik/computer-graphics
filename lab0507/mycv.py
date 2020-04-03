class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def line(x0, y0, x1, y1):
    steep = False

    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    derror2 = abs(dy) * 2
    error2 = 0
    y = y0

    for x in range(x0, x1 + 1):
        if steep:
            yield y, x

        else:
            yield x, y

        error2 += derror2

        if error2 > dx:
            y += 1 if y1 > y0 else -1
            error2 -= dx * 2


def circle(x1, y1, r):
    x = 0
    y = r

    delta = 1 - 2 * r

    while y >= 0:
        yield x1 + x, y1 + y,
        yield x1 + x, y1 - y,
        yield x1 - x, y1 + y,
        yield x1 - x, y1 - y,

        error = 2 * (delta + y) - 1

        if delta < 0 and error <= 0:
            x += 1
            delta += 2 * x + 1

            continue

        error = 2 * (delta - x) - 1

        if delta > 0 and error > 0:
            y -= 1
            delta += 1 - 2 * y

            continue

        x += 1
        delta += 2 * (x - y)
        y -= 1


def triangle(t0, t1, t2):
    if t0[1] > t1[1]:
        t0, t1 = t1, t0

    if t0[1] > t2[1]:
        t0, t2 = t2, t0

    if t1[1] > t2[1]:
        t1, t2 = t2, t1

    (x0, y0), (x1, y1), (x2, y2) = t0, t1, t2

    total_height = y2 - y0

    for y in range(y0, y1 + 1):
        segment_height = y1 - y0 + 1

        alpha = float(y - y0) / total_height
        beta = float(y - y0) / segment_height

        ax = int(x0 + (x2 - x0) * alpha)
        bx = int(x0 + (x1 - x0) * beta)

        if ax > bx:
            ax, bx = bx, ax

        for j in range(ax, bx + 1):
            yield j, y
