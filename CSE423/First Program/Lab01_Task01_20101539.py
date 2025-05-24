from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
hght = 490
new_x = 0
new_y = 2
r_scn=0
g_scn=0
b_scn=0
def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_lines(x1, y1, x2, y2):
    global r_scn,g_scn,b_scn
    if r_scn > 0.4:
        glColor3f(0, 0, 0)
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
    glutPostRedisplay()

def BuildingHouse():
    glColor3f(0.0, 1.0, 1.0)
    draw_lines(120, 250, 120, 120) #left
    draw_lines(350, 250, 350, 120) #upper
    draw_lines(120, 250, 350, 250) #right
    draw_lines(120, 120, 350, 120) #bottom

    draw_lines(215, 190, 215, 120) #door left
    draw_lines(260, 190, 260, 120) #door right
    draw_lines(215, 190, 260, 190) #door upper line
    draw_points(250, 155) #point

    draw_lines(150, 165, 200, 165) #bottom of left window
    draw_lines(150, 210, 200, 210) #upper of left window
    draw_lines(150, 165, 150, 210) #left of left window
    draw_lines(200, 165, 200, 210) #right of left window
    
    draw_lines(278, 165, 325, 165) #bottom of right window
    draw_lines(278, 210, 325, 210) #upper of right window
    draw_lines(278, 165, 278, 210) #left of right window
    draw_lines(325, 165, 325, 210) #right of left window

    draw_lines(100, 250, 235, 350) #roof left
    draw_lines(235, 350, 370, 250) #roof right
    draw_lines(100, 250, 120, 250) #left
    draw_lines(370, 250, 350, 250) #right

def rainLines(x1, y1, x2, y2):
    global r_scn,g_scn,b_scn
    if r_scn > 0.4:
        glColor3f(0, 0, 0)
    glLineWidth(.5) 
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

x_arr = [10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 490] #defining rain positions

def animate():
    global hght, x_arr, new_x, new_y
    hght = hght - new_y
    if hght < 200:
        hght = 490   

    for i in range(len(x_arr)):
        x_arr[i] += new_x
        if x_arr[i] > 500:
            x_arr[i] = 0
        elif x_arr[i] < 0:
            x_arr[i] = 500

def viewScreen():
    global hght, x_arr, new_x, new_y, r_scn, g_scn, b_scn
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(r_scn,g_scn,b_scn,0)
    glLoadIdentity()
    iterate()
    BuildingHouse()
    #glColor3f(1.0, 1.0, 0.0)  # RGB

    for m in range(len(x_arr)):
        p1 = x_arr[m]
        p2 = x_arr[m] + new_x

        if m % 2 == 0:
            q1 = hght
            q2 = q1 + 20
        else:
            q1 = hght - 40
            q2 = q1 + 20

        rainLines(p1, q1, p2, q2)
        rainLines(p1, q1+60, p2, q2+70)
    
    glutSwapBuffers()
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global new_x
    if key==GLUT_KEY_RIGHT:
        new_x -= 0.5
        print("RIGHT")
    if key== GLUT_KEY_LEFT:
        new_x += 0.5
        print("LEFT")
    glutPostRedisplay()

def keyboardListener(key,x,y):
    global r_scn,g_scn,b_scn
    if key==b'm':
        r_scn += 0.01
        g_scn += 0.01
        b_scn += 0.01

    if key==b'n':
        r_scn -= 0.01
        g_scn -= 0.01
        b_scn -= 0.01
    glutPostRedisplay()  

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1") #window name
glutDisplayFunc(viewScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()