import pygame
from OpenGL.GL import *
from pygame.locals import *

from lab08.utils import project_with_angle


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
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [2, 2, 2, 1])

    @staticmethod
    def draw(objects):
        rotations = [0 for _ in objects]
        light_angle = [0, 0, 1]

        while True:
            light_angle = project_with_angle(light_angle, 0.1, 0.05, 0.025)

            glLightfv(GL_LIGHT0, GL_POSITION, light_angle + [0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            for tor_i, tor in enumerate(objects):
                glPushMatrix()
                rotations[tor_i] += (tor_i + 1) * 1.5
                glRotatef(rotations[tor_i], 1, 1, 1)
                tor.draw_gl()
                glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)
