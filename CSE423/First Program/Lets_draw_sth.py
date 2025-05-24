from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500,500

ballx = bally = 0
speed = 1
ball_size = 5
create_new = False


def draw_points(x, y, s):
    glPointSize(s) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glColor3f(1.0, 0.0, 1.0)
    glEnd()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    # drawAxes()
    global ballx, bally, ball_size
    draw_points(ballx, bally, ball_size)
    # drawShapes()

    # if(create_new):
    #     m,n = create_new
    #     glBegin(GL_POINTS)
    #     glColor3f(0.7, 0.8, 0.6)
    #     glVertex2f(m,n)
    #     glEnd()


    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx, bally,speed
    ballx=(ballx+speed)%180
    bally=(bally+speed)%180

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

wind = glutCreateWindow(b"OpenGL Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)


glutMainLoop()		#The main loop of OpenGL
