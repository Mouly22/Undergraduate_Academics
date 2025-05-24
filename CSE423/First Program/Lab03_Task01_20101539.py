from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
rad = 0
cordinate = [-1, 1]
lst = []
freeze = False
speed = 1.5


def circle_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(-x + cx, y + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(-y + cx, -x + cy)


def midpoint_circle(cx, cy, radius):
    x = 0
    y = radius
    d = 1 - radius
    circle_points(x, y, cx, cy)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        circle_points(x, y, cx, cy)


def draw_circle(cx, cy, radius):
    glBegin(GL_POINTS)
    midpoint_circle(cx, cy, radius)
    glEnd()


class single_circle:
    global WINDOW_HEIGHT, WINDOW_WIDTH, lst

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.radius = 1
        a = WINDOW_WIDTH
        b = WINDOW_HEIGHT

        self.max_radius = max(
            [math.sqrt((x - a)**2 + (y - 0)**2), math.sqrt((x - 0)**2 + (y - b)**2), math.sqrt((x - a)**2 + (y - b)**2), math.sqrt((x - 0)**2 + (y - 0)**2)])
        print(f'Ripple created at ({self.X},{self.Y}) point')
        print(f'Current number of ripples: {len(lst)+1}')




def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def animation():
    global lst, freeze, speed 
    if freeze == False: 
        for elm in lst:
            elm.radius += speed
            if elm.radius > elm.max_radius:
                lst.remove(elm)
                print(f'Ripple at ({elm.X, elm.Y}) is removed. Radius is {elm.radius}. Max radius is {elm.max_radius}. ')
                print(f'Current number of ripples:{(len(lst))}')

    glutPostRedisplay()

def show_screen():
    # this function should contain the logic for drawing objects
    # DO NOT do game logic here (e.g. object movement, collision detection, sink detection etc.)

    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(2)
    for elm in lst:
        draw_circle(elm.X, elm.Y, elm.radius)  
    

    # do not forget to call glutSwapBuffers() at the end of the function
    glutSwapBuffers()

def mouseListener(button, state, x, y):
    global X,Y, lst, freeze

    if freeze == False and button == GLUT_RIGHT_BUTTON:
        
        if state == GLUT_DOWN:
           
            print('Right Button clicked')
            X, Y = x,500-y
            var = single_circle(X, Y)
            lst.append(var)

    glutPostRedisplay()

def keyboard_ordinary_keys(key, _, __):
    global freeze
    # check against alphanumeric keys here (e.g. A..Z, 0..9, spacebar, punctuations)
    # must cast characters to binary when comparing (e.g. key == b'q')
    if key == b' ':
        if freeze == True:
            freeze = False
        else:
            freeze = True


    glutPostRedisplay()



def keyboard_special_keys(key, _, __): 
    global speed
  
   
    if key == GLUT_KEY_LEFT:
        speed += .5
        
    elif key == GLUT_KEY_RIGHT:
        if speed <= 0.1:
           speed = 0.1
        else:
           speed -= .5

    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Water Ripples")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)

glutKeyboardFunc(keyboard_ordinary_keys)
glutSpecialFunc(keyboard_special_keys)
glutMouseFunc(mouseListener)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()



