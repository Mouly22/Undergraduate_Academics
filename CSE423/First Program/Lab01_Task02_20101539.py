from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

lst = []
speed = 0.01
cordinate = [-1, 1]
X = 0
Y = 0
createLst = False
Frozen = True
Blink = False

def draw_points(x, y,color):
    glColor3f(color[0], color[1], color[2])
    glPointSize(6)

    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

class balls:
    def __init__(self, x, y, nx, ny, color):
        self.prev_x = x
        self.prev_y = y
        self.new_x = nx
        self.new_y = ny
        self.color = color

def createList():
    global X,Y, cordinate
    for i in range(random.randint(10, 50)):
                x = random.randint(X-100, X+100) #initial x
                y = random.randint(Y-100, Y+100) #initial y
                nx = cordinate[random.randint(0,1)] #updating x
                ny = cordinate[random.randint(0,1)] #updating y
                color = [random.randint(0,50)/50, random.randint(0,50)/50, random.randint(0,50)/50] #creating color variations
                point = balls(x, y, nx, ny, color)
                lst.append(point)


def animate():
    global Frozen, createLst, lst, speed, cordinate
    if Frozen: 
        if createLst:
            createLst = False #reseting it as False for multiple runtime
            if len(lst) == 0:
                createList()
        else:
            min_speed()
            for i in range(len(lst)):
                x = lst[i].prev_x
                y = lst[i].prev_y
                nx = lst[i].new_x
                ny = lst[i].new_y
                if nx >= 0:
                    x += speed
                else: 
                    x -= speed
                if ny >= 0:
                    y += speed
                else:
                    y -= speed
                if x < 0 or x> 500 or y< 0 or y>500:
                    if nx > 0:
                        lst[i].new_x = -1
                    else:
                        lst[i].new_x = 1
                    if ny >0:
                        lst[i].new_y = -1
                    else:
                        lst[i].new_y = 1
                else:
                    lst[i].prev_x = x
                    lst[i].prev_y = y
def min_speed():
    global speed
    if speed <= 0:
        speed = 0.001

    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global X,Y, createLst, lst, Blink, speed

    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            createLst = True
            lst = []  
            Blink = False
            print('Right Button clicked')
            X, Y = x,500-y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            Blink = True
            speed = 0.01
            print('Left Button clicked')


    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed
    if key=='w':
        print(1)
    if key==GLUT_KEY_UP:
        speed += 0.1
        print('Increasing Speed')

    if key== GLUT_KEY_DOWN:        
        speed -= 0.1
        print("Decreasing Speed")
    glutPostRedisplay()


def keyboardListener(key, x, y):
    global Frozen
    if key == b' ':
        if Frozen == True:
            Frozen = False
        else:
            Frozen = True
        print('Space Clicked')

def viewScreen():
    global Blink
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #draw_points(250,250)
    if not Blink: 
        for i in range(len(lst)):
            draw_points(lst[i].prev_x, lst[i].prev_y, lst[i].color)
    
    else: 
        #print(time.time())
        if (int(time.time()) % 2 == 0) and Frozen:
            for i in range(len(lst)):
                draw_points(lst[i].prev_x, lst[i].prev_y, lst[i].color)
        elif not Frozen:
            for i in range(len(lst)):
                draw_points(lst[i].prev_x, lst[i].prev_y, lst[i].color)

    glutSwapBuffers()
    glutPostRedisplay()
        

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2") #window name
glutIdleFunc(animate)
glutDisplayFunc(viewScreen)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()

