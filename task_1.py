from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

W_Width, W_Height = 800,800
line_width = 10
bg_color = (1,1,1, 0)
color = (0, 0, 1)

r_x, r_y = 400, 800
r_len = 30
angle = 0
rains = []


def distance(x1, y1, x2, y2):
    return int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
#house measurement
left_roof = distance(150 - line_width, 350, 400, 500)
left_wall = distance(150, 20, 150, 350)
right_roof = distance(400, 500, 650 + line_width, 350)
right_wall = distance(650, 20, 650, 350)

def collide_with_house(x, y):
    if left_roof == distance(150 - line_width, 350, x, y) + distance(400, 500, x, y):
        return True
    if right_roof == distance(650 + line_width, 350, x, y) + distance(400, 500, x, y):
        return True
    if left_wall == distance(150, 20, x, y) + distance(150, 350, x, y):
        return True
    if right_wall == distance(650, 20, x, y) + distance(650, 350, x, y):
        return True
    return False

def draw_point(x, y, s, color):
    glPointSize(s)
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_line(x1, y1, x2, y2, width, color):
    glLineWidth(width)
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2d(x1,y1)
    glVertex2d(x2,y2)
    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    glVertex2d(x1,y1)
    glVertex2d(x2,y2)
    glVertex2d(x3,y3)
    glEnd()

def draw_house(line_width, color, bg_color):
    #drawing the house:
    draw_line(150, 20, 650, 20, line_width, color)
    draw_line(150, 20 - (line_width//2), 150, 350, line_width, color)
    draw_line(650, 20 - (line_width//2), 650, 350, line_width, color)
    draw_triangle(150 - line_width, 350, 400, 500, 650 + line_width, 350, color)
    draw_triangle(150 + (2 *line_width), 350 + line_width, 400, 500 - line_width, 650 - (2*line_width), 350 + line_width, bg_color[0:3])
    
    #draw door
    draw_line(250, 20, 250, 200, line_width/line_width, color)
    draw_line(350, 20, 350, 200, line_width/line_width, color)
    draw_line(250, 200, 350, 200, line_width/line_width, color)
    #door nob
    draw_point(335, 100, 3, color)
    #draw window
    draw_line(480, 230, 480, 300, line_width/line_width, color)
    draw_line(550, 230, 550, 300, line_width/line_width, color)
    draw_line(480, 230, 550, 230, line_width/line_width, color)
    draw_line(480, 300, 550, 300, line_width/line_width, color)

    draw_line(480 + ((550-480)//2), 230,480 + ((550-480)//2), 300, line_width/line_width, color)
    draw_line(480, 230 + ((300-230)//2), 550, 230 + ((300-230)//2), line_width/line_width, color)

def day_night(color, increment):
    r, g, b, a = color
    return tuple(((r+increment)%1, (g+increment)%1, (b+increment)%1, a))

def keyboard_press(key, x, y):
    global bg_color
    if key == b'a':
        bg_color = day_night(bg_color, 0.01)
    if key == b'd':
        bg_color = day_night(bg_color, -0.01)
    glutPostRedisplay()

def specialKey_press(key, x, y):
    global angle

    if key==GLUT_KEY_LEFT:
        angle -= 1
    if key== GLUT_KEY_RIGHT:		#// up arrow key
        angle += 1
    glutPostRedisplay()


def rain():
    global rains, angle
    for x, y in rains:
        draw_line(x+angle, y, x, y+r_len, 1, color)
    

def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*bg_color);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    glOrtho(0.0, W_Width, 0.0, W_Height, 0.0, 1.0)

    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    #gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    draw_house(line_width, (0.86, 0.46, 0.17), bg_color)
    rain()

    glutSwapBuffers()


def rain_drops_animate():
    glutPostRedisplay()
    global rains
    new_rains=[]
    for i in range(1):
        x = random.randrange(0, W_Width)
        new_rains.append([x, W_Height])

    for i, pos in enumerate(rains):
        pos[0] = (pos[0]+angle*0.1)% W_Width
        pos[1] = pos[1]-abs(angle*0.05)-3

        if 0 <= pos[0] <= W_Width and 0 < pos[1]:

            if not collide_with_house(pos[0], pos[1]):
                new_rains.append(pos)

    rains = new_rains

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(0,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(800, 200)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"It's raining")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(rain_drops_animate)

glutKeyboardFunc(keyboard_press)
glutSpecialFunc(specialKey_press)

glutMainLoop()		#The main loop of OpenGL