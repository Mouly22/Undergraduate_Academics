from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

WINDOW_WIDTH  = 500
WINDOW_HEIGHT = 750
over = False
reset = False
count = 0
freeze = False
speed = 1
catcher = False
color = [random.randint(0,50)/50, random.randint(0,50)/50, 1]
class AABB:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def collides_with(self, other):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2
    

# Global variables
box1 = AABB(200, 450, 30, 40)
box2 = AABB(70, 10, 120, 18)
box3 = AABB(30, 700, 40, 40)
box4 = AABB(220, 700, 40, 40)
box5 = AABB(430, 700, 40, 40)

box_speed = 20
collision = False

def zoneFinding(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) >= abs(dy):
        if dx > 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dy >= 0 and dx <= 0:
            zone = 2
        elif dx < 0 and dy <= 0:
            zone = 5
        else:
            zone = 6

    return zone

def rootToZone0(z, x, y):
    if z == 0:
        return (x, y)
    elif z == 1:
        return (y, x)
    elif z == 2:
        return (y, -x)
    elif z == 3:
        return (-x, y)
    elif z == 4:
        return (-x, -y)
    elif z == 5:
        return (-y, -x)
    elif z == 6:
        return (-y, x)
    elif z == 7:
        return (x, -y)
    else:
        return (0, 0)

def Zone0ToRoot(Z, x, y):
    if Z == 0:
        return (x, y)
    elif Z == 1:
        return (y, x)
    elif Z == 2:
        return (-y, x)
    elif Z == 3:
        return (-x, y)
    elif Z == 4:
        return (-x, -y)
    elif Z == 5:
        return (-y, -x)
    elif Z == 6:
        return (y, -x)
    elif Z == 7:
        return (x, -y)
    else:
        return (0, 0)

def Zone0_Ldraw(Z,x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx  

    x = x1
    y = y1

    
    tempx, tempy = Zone0ToRoot(Z,x,y)
    glVertex2f(tempx,tempy) 

    while x < x2:
        x += 1
        if d < 0:
            d = d + 2 * dy
        else:
            d = d + 2 * (dy - dx)
            y += 1
        
        tempx, tempy = Zone0ToRoot(Z,x,y)
      
        glVertex2f(tempx,tempy) #jekhane show korbe pixel

def mid_point_drawline(x1,y1,x2,y2):
    a = zoneFinding(x1,y1,x2,y2)
    x1,y1 = rootToZone0(a,x1,y1)
    x2,y2 = rootToZone0(a,x2,y2)
    glPointSize(2) 
    glBegin(GL_POINTS)
    Zone0_Ldraw(a,x1,y1,x2,y2)
    glEnd()

    
def catchbox_draw():
    global box1, box2
    if box1.y < 0:
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(1.0, 1.0, 1.0)

    mid_point_drawline(box2.x, box2.y,box2.x-10 + box2.w, box2.y)
    mid_point_drawline(box2.x + box2.w-10, box2.y,box2.x + box2.w, box2.y + box2.h)

    mid_point_drawline(box2.x + box2.w, box2.y + box2.h,box2.x-10, box2.y + box2.h)

    mid_point_drawline(box2.x-10, box2.y + box2.h,box2.x, box2.y)




def diamond_draw():
    global box1, color
    glColor3f(color[0], color[1], color[2])

    
    center_x = box1.x + box1.w / 2
    center_y = box1.y + box1.h / 2

    mid_point_drawline(center_x, box1.y,box1.x + box1.w, center_y)
    
    mid_point_drawline(box1.x + box1.w, center_y,center_x, box1.y + box1.h)


    mid_point_drawline(center_x, box1.y + box1.h,box1.x, center_y)
    mid_point_drawline(box1.x, center_y,center_x, box1.y)





def arrow_draw():
    global box3
   
    glColor3f(0.0, 1.0, 1.0)
    

    
    center_x = box3.x + box3.w / 2
    center_y = box3.y + box3.h / 2

    mid_point_drawline(center_x, box3.y + box3.h,box3.x, center_y)
    mid_point_drawline(box3.x, center_y,center_x, box3.y)

    mid_point_drawline(center_x-20, center_y,center_x+box3.w-20, center_y)




def playGame_draw():
    global box4
    glColor3f(1.0, 1.0, 0.0)


    mid_point_drawline(box4.x + box4.w, box4.y,box4.x + box4.w, box4.y + box4.h)

    mid_point_drawline(box4.x+20, box4.y + box4.h,box4.x+20, box4.y)


def pauseGame_draw():
    global box4
    glColor3f(1.0, 1.0, 0.0)

    triangle_width = 15

    mid_point_drawline(box4.x + triangle_width, box4.y,box4.x + triangle_width, box4.y + box4.h)
    mid_point_drawline(box4.x + triangle_width, box4.y + box4.h,box4.x + box4.w, box4.y + box4.h / 2)

    mid_point_drawline(box4.x + box4.w, box4.y + box4.h / 2,box4.x + triangle_width, box4.y)


def crossGame_draw():
    global box5
    glColor3f(1.0, 0.0, 0.0)

    mid_point_drawline(box5.x + box5.w, box5.y,box5.x, box5.y + box5.h)

    mid_point_drawline(box5.x+box5.w, box5.y + box5.h,box5.x, box5.y)


def draw_box(box):
    global collision, box1, freeze

    catchbox_draw()
    diamond_draw()
    arrow_draw()
    crossGame_draw()

    if freeze == False:
        playGame_draw()
    else:
        pauseGame_draw()


def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def check_collision():
    global box1, box2, box3, collision
   

    if box1.collides_with(box2):
        collision = True
        count_ball()
        diamond_generate()
    
    else:
        collision = False


def diamond_generate():
    global box1, color
    color = [random.randint(0,50)/50, random.randint(0,50)/50, 1]
    box1 = AABB(random.randint(20,450), 750, 30, 40)

def ballInfo():
    global count,speed
    count += 1
    speed += 0.4

def count_ball():
    global collision, count, reset, speed
    if reset== False:
        if collision == True:
            ballInfo()
            print(f"Score: {count}")
    else:
        count = 0
        speed = 1
        if collision == True:
            ballInfo()
            print(f"Score: {count}")
def restart():
    global freeze, over
    count_ball()
    diamond_generate()
    freeze = False
    over = False
    

    print('Starting over!')

def mouse_click(button, state, x, y):
    global box3, box4, box5, reset, count, over, freeze, catcher 
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        mx, my = x, WINDOW_HEIGHT-y
        mouse_box = AABB(mx, my, 1, 1)

        if box3.collides_with(mouse_box):
            reset = True
            if reset== True:
                restart()
                catcher = False
                reset = False
                
        elif box4.collides_with(mouse_box):
            if freeze == False:
                freeze = True
                   
            else:
                freeze = False
              

        elif box5.collides_with(mouse_box):
            over = True
            
            if over == True:
                print(f"Goodbye! Score is {count}") 
                catcher = True
                reset = True
                glutLeaveMainLoop() 

    glutPostRedisplay()

      
def animation():
    global box1, over, count, freeze,speed, reset, catcher
    if not freeze:
        box1.y -= 1 + speed
        
    else:
        box1.y = box1.y
    
    if box1.y < 0:
        if not over:
            print(f"Game Over! Score: {count}")
            catcher = True
            
        over = True

    check_collision()

    glutPostRedisplay()      


def show_screen():
    # this function should contain the logic for drawing objects
    # DO NOT do game logic here (e.g. object movement, collision detection, sink detection etc.)

    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # draw stuffs here
    draw_box(box1)
    draw_box(box2)
    draw_box(box3)
    draw_box(box4)
    draw_box(box5)

    # do not forget to call glutSwapBuffers() at the end of the function
    glutSwapBuffers()



       
def keyboard_ordinary_keys(key, _, __):
    # check against alphanumeric keys here (e.g. A..Z, 0..9, spacebar, punctuations)
    # must cast characters to binary when comparing (e.g. key == b'q')

    glutPostRedisplay()


def keyboard_special_keys(key, _, __): 
    global box2, freeze, catcher
    # if key == GLUT_KEY_UP:
    #     box2.y += box_speed
    # elif key == GLUT_KEY_DOWN:
    #     box2.y -= box_speed
    if catcher == False:
        if freeze == False:
            if key == GLUT_KEY_LEFT:
                if box2.x >= 30:
                    box2.x -= box_speed
                
            elif key == GLUT_KEY_RIGHT:
                if box2.x <= 369:
                    box2.x += box_speed
    

    glutPostRedisplay()

    check_collision()

    # don't forget to call glutPostRedisplay()
    # otherwise your animation will be stuck
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Catch the Diamonds!")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)

glutKeyboardFunc(keyboard_ordinary_keys)
glutSpecialFunc(keyboard_special_keys)
glutMouseFunc(mouse_click)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()