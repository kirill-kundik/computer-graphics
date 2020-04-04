from lab0809.model import Model
from lab0809.my_open_gl import MyOpenGL

if __name__ == "__main__":
    open_gl = MyOpenGL(800, 800)

    r_big = (250, 170, 100)
    r_small = (30, 20, 10)

    toruses = [
        Model(r_big[i], r_small[i], None).generate_gl()
        for i in range(1)
    ]

    open_gl.draw(toruses)
