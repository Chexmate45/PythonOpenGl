import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy



class Pyramid():
    vertices = [
        [1,-1,-1],
        [1,-1,1],
        [-1,-1,1],
        [-1,-1,-1],
        [0,1,0]
    ]
    edges = [
        [0,1],
        [0,3],
        [0,4],
        [1,4],
        [1,2],
        [2,4],
        [2,3],
        [3,4]
    ]

    surfaces = (
        (1,2,4),
        (0,1,2,3),
        (0,1,4),
        (0,3,4),
        (2,3,4)
    )

    def __init__(self, mul=1):
        self.edges = Pyramid.edges
        self.vertices = list(numpy.multiply(numpy.array(Pyramid.vertices), mul))
        self.surfaces = Pyramid.surfaces
    def draw(self):
        self.draw_sides()
        glLineWidth(5)
        glBegin(GL_LINES)#lines
        for edge in self.edges:
            for vertex in edge:
                glColor3f(1,1,1)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def draw_sides(self):
        glLineWidth(5)
        glBegin(GL_QUADS)#surfaces
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(1,0,0)
                glVertex3fv(self.vertices[vertex])

        glEnd()
    def move(self,x,y,z):
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1]+ y, vert[2]+ z), self.vertices))

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    #glRotatef(45, 0, 1, 0)
    glTranslatef(0,0,-20)
    glEnable(GL_DEPTH_TEST)

    p = Pyramid()
    vel = 0.1
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.move(-vel, 0, 0)
        if keys[pygame.K_RIGHT]:
            p.move(vel, 0, 0)
        if keys[pygame.K_UP]:
            p.move(0, vel, 0)
        if keys[pygame.K_DOWN]:
            p.move(0, -vel, 0)
        if keys[pygame.K_w]:
            p.move(0, 0, -vel)
        if keys[pygame.K_s]:
            p.move(0, 0, vel)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        p.draw()
        pygame.display.flip()
main()
