import numpy as np
import pygame
from OpenGL.GL import *
from pygame.locals import *

from lab0809.utils import project_with_angle


class MyOpenGL:
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._clock = pygame.time.Clock()

        self._init()

        self.objects = []

    def _init(self):
        pygame.init()
        pygame.display.set_mode((self._width, self._height), DOUBLEBUF | OPENGL)

        glOrtho(0, self._width, 0, self._height, 2000, -2000)
        glTranslatef(self._width / 2, self._height / 2, 0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [4, 4, 4, 1])
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 0, 0])

    @staticmethod
    def draw(objects):
        rotations = [0 for _ in objects]
        # light_angle = [0, 0, 1]
        glRotatef(-40, 1, .5, 0)

        while True:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)

            shadow_casters = []
            draw_bottom_plane()

            # light_angle = project_with_angle(light_angle, 0.1, 0.05, 0.025)
            #
            # glLightfv(GL_LIGHT0, GL_POSITION, light_angle + [0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            for tor_i, tor in enumerate(objects):
                glPushMatrix()
                rotations[tor_i] += (tor_i + 1) * 1.5

                glRotatef(rotations[tor_i], 0, 1, 0)
                glRotatef(rotations[tor_i], 0, 0, 1)
                for face in tor.draw_gl():
                    rotation = np.radians(rotations[tor_i])
                    shadow_casters.append(
                        [project_with_angle(v, theta_x=0, theta_y=-rotation, theta_z=-rotation) for v in face]
                    # [rotate(v, theta_x=rotation) for v in face]
                    # [rotate(v, theta_y=-rotation) for v in face]
                    # [rotate(v, theta_z=-rotation) for v in face]
                    )

                glPopMatrix()

            glBegin(GL_TRIANGLES)
            for shadow_caster in shadow_casters:
                glColor3fv((0, 0, 0))
                for (x, y, z) in shadow_caster:
                    glVertex3fv((x, -349.5, z))
            glEnd()

            pygame.display.flip()
            pygame.time.wait(10)


def draw_bottom_plane():
    bottom_y = -350
    size = 1200

    glColor3fv((.9, .3, .1))
    v1, v2, v3, v4 = \
        (-size / 2, bottom_y, -size / 2), \
        (-size / 2, bottom_y, size / 2), \
        (size / 2, bottom_y, size / 2), \
        (size / 2, bottom_y, -size / 2)

    glBegin(GL_QUADS)
    for v in (v1, v2, v3, v4):
        glVertex3fv(v)
    glEnd()

    return [0, 0, 0, bottom_y]
