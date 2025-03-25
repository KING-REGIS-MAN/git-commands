
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_diamond():
    vertices = [
        [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
        [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]
    ]
    edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_limb(angle, x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(angle, 1, 0, 0)
    glScalef(0.2, 0.6, 0.2)
    draw_diamond()
    glPopMatrix()

def draw_runner(frame):
    # Body
    glPushMatrix()
    glScalef(0.3, 1.0, 0.3)
    draw_diamond()
    glPopMatrix()
    
    # Head
    glPushMatrix()
    glTranslatef(0, 1.2, 0)
    glScalef(0.3, 0.3, 0.3)
    draw_diamond()
    glPopMatrix()
    
    # Arms
    arm_angle = math.sin(frame * 0.1) * 30
    draw_limb(arm_angle, 0.5, 0.8, 0)  # Right Arm
    draw_limb(-arm_angle, -0.5, 0.8, 0)  # Left Arm
    
    # Legs
    leg_angle = math.sin(frame * 0.1) * 30
    draw_limb(-leg_angle, 0.3, -0.8, 0)  # Right Leg
    draw_limb(leg_angle, -0.3, -0.8, 0)  # Left Leg

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    
    frame = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_runner(frame)
        pygame.display.flip()
        pygame.time.wait(33)  # ~30 FPS
        frame += 1
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
