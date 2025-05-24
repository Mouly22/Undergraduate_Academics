from Lets_draw_sth import draw_points
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_lines(x1, y1, x2, y2):
    glLineWidth(.5) 
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(250, 250)
    # draw_lines(120, 250, 120, 120) #left
    # draw_lines(350, 250, 350, 120) #upper
    # draw_lines(120, 250, 350, 250) #right
    # draw_lines(120, 120, 350, 120) #bottom

    # draw_lines(215, 190, 215, 120) #door left
    # draw_lines(260, 190, 260, 120) #door right
    # draw_lines(215, 190, 260, 190) #door upper line
    # draw_lines(238, 190, 238, 120) #middle line

    # draw_lines(150, 165, 200, 165) #bottom of left window
    # draw_lines(150, 210, 200, 210) #upper of left window
    # draw_lines(150, 165, 150, 210) #left of left window
    # draw_lines(200, 165, 200, 210) #right of left window
    
    # draw_lines(278, 165, 325, 165) #bottom of right window
    # draw_lines(278, 210, 325, 210) #upper of right window
    # draw_lines(278, 165, 278, 210) #left of right window
    # draw_lines(325, 165, 325, 210) #right of left window

    # draw_lines(100, 250, 235, 350) #roof left
    # draw_lines(235, 350, 370, 250) #roof right
    # draw_lines(100, 250, 120, 250) #left
    # draw_lines(370, 250, 350, 250) #right


    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()