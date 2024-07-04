from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 800,800
bg_color = (0, 0, 0, 0)
speed = 1
balls = []
freez = False
all_directions = [[1, 1], [-1, -1], [-1, 1], [1, -1]]

class Ball:
    BLINK = False
    def __init__(self, pos, direction, color):
        self.pos = pos
        self.direction = direction
        self.color = color
        self.backup_color = color
    
    def animate(self, speed,):

        #modify direction:
        if self.pos[1] > W_Height or self.pos[1] < 0:
            self.direction[1] *= -1
        if self.pos[0] < 0 or self.pos[0] > W_Width:
            self.direction[0] *= -1

        self.pos[0]  = self.pos[0] + (speed * self.direction[0])
        self.pos[1]  = self.pos[1] + (speed * self.direction[1])

    def draw(self):
        glPointSize(10)
        if not Ball.BLINK:
            glColor3f(*self.color)
        else: glColor3f(0, 0, 0)
        glBegin(GL_POINTS)
        glVertex2f(*self.pos)
        glEnd()

def random_color():
    return (random.random(), random.random(), random.random())

def keyboard_press(key, x, y):
    global freez
    if key == b' ':
        freez = not freez

def specialKey_press(key, x, y):
    global speed
    if key==GLUT_KEY_DOWN:
        speed /= 1.5
    if key== GLUT_KEY_UP:		#// up arrow key
        speed *= 1.5
    glutPostRedisplay()

def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global balls
    if not freez:
        if button==GLUT_LEFT_BUTTON:
            Ball.BLINK = True    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP     
            if state == GLUT_UP:
                Ball.BLINK = False
        if button==GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN: 	
                balls.append(Ball([x, W_Height-y], random.choice(all_directions)[:], random_color()))
    glutPostRedisplay()

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
    for ball in balls:
        ball.draw()

    glutSwapBuffers()

def animation():
    glutPostRedisplay()
    if not freez:
        for ball in balls:
            ball.animate(speed)


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
wind = glutCreateWindow(b"Box")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animation)
glutKeyboardFunc(keyboard_press)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKey_press)

glutMainLoop()		#The main loop of OpenGL