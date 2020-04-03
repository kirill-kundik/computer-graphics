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


def line(x0, y0, x1, y1, image, color):
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
            image[y, x] = color
        else:
            image[x, y] = color

        error2 += derror2

        if error2 > dx:
            y += 1 if y1 > y0 else -1
            error2 -= dx * 2


def circle(x1, y1, r, image, color):
    x = 0
    y = r

    delta = 1 - 2 * r

    while y >= 0:
        image[x1 + x, y1 + y] = color
        image[x1 + x, y1 - y] = color
        image[x1 - x, y1 + y] = color
        image[x1 - x, y1 - y] = color

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


def triangle(t0: Point, t1: Point, t2: Point, image, color):
    if t0.y > t1.y:
        t0, t1 = t1, t0
    if t0.y > t2.y:
        t0, t2 = t2, t0
    if t1.y > t2.y:
        t1, t2 = t2, t1

    total_height: int = t2.y - t0.y

    for y in range(total_height):
        second_half: bool = y > t1.y - t0.y or t1.y == t0.y

        segment_height: int = t2.y - t1.y if second_half else t1.y - t0.y

        alpha: float = y / total_height
        beta: float = float((y - (t1.y - t0.y if second_half else 0))) / segment_height

        ax = t0 + (t2 - t0) * alpha
        bx = t1 + (t2 - t1) * beta if second_half else t0 + (t1 - t0) * beta

        if ax.x > bx.x:
            ax, bx = bx, ax

        for j in range(ax.x, bx.x + 1):
            image[j, t0.y + y] = color
