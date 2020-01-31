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
