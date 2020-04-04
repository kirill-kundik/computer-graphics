from lab0809.model import Model
from lab0809.my_open_gl import MyOpenGL

if __name__ == "__main__":
    open_gl = MyOpenGL(800, 800)

    r_big = (250, 170, 100)
    r_small = (40, 30, 20)

    toruses = [
        Model(r_big[i], r_small[i], None).generate_gl()
        for i in range(3)
    ]

    open_gl.draw(toruses)
