from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from icons import Diamond, Reset, Pause, Play, Exit, Bucket
import random
import time

#display properties
W_Width, W_Height = 500,800
bg_color = (0, 0, 0, 0)
#game icons
diamonds = []
bucket = Bucket(75, 21, (1, 1, 1))
bar_icons = {
            "reset": Reset(30, W_Height-10, (0.53, 0.99, 0.89)),
            "pause": Pause(W_Width/2, W_Height-10, (1, 0.9, 0.01)),
            "play": Play(W_Width/2, W_Height-10, (1, 0.9, 0.01)),
            "exit": Exit(W_Width-30, W_Height-10, (1, 0, 0)),        
            }

#game properties
levels = {5: 200, 10: 250, 15: 300, 25: 350, 30: 400, 40: 450, 60:480, 80: 510, 100: 530, 150: 550}
bucket_speed = 1600
level = 150
score = 0
run: bool = True
game_over = False
prev_time = time.time()
dt = time.time() - prev_time

def random_color():
    return (random.randint(128, 255)/255, random.randint(128, 255)/255, random.randint(128, 255)/255)

diamonds.append(Diamond(random.randint(20, W_Width-20), W_Height, random_color()))


def keyboard_press(key, x, y):
    if key == b' ':
        pass

def specialKey_press(key, x, y):
    if run:
        if key==GLUT_KEY_LEFT:
            if bucket.x - bucket.w * 0.55> 0:
                bucket.x -= bucket_speed * dt
        if key== GLUT_KEY_RIGHT:
            if bucket.x + bucket.w * 0.55 < W_Width:
                bucket.x += bucket_speed * dt
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global run, game_over, diamonds, score, bucket, level, levels
    if run and state == GLUT_DOWN and bar_icons["play"].collide(x, W_Height - y):
        run = not run
    
    elif not run and state == GLUT_DOWN and bar_icons["pause"].collide(x, W_Height - y):
        run = not run
    
    elif state == GLUT_DOWN and bar_icons["reset"].collide(x, W_Height- y):
        print("Starting Over!")
        run = True
        game_over = False
        score = 0
        level = levels.get(score, 150)
        bucket.color = (1, 1, 1)
        diamonds = []
        diamonds.append(Diamond(random.randint(20, W_Width-20), W_Height, random_color()))

    elif state == GLUT_DOWN and bar_icons["exit"].collide(x, W_Height- y):
        print(f"Goodbye! Score: {score}")
        glutLeaveMainLoop()


    glutPostRedisplay()

def display():
    global score, game_over ,diamonds, bucket, levels, level, prev_time, dt
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*bg_color);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initializde the matrix
    glLoadIdentity()
    glOrtho(0.0, W_Width, 0.0, W_Height, 0.0, 1.0)

    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    #gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    new_time = time.time() 
    dt = new_time - prev_time
    prev_time = new_time
    bucket.draw()
    for d in diamonds:
        if run and not game_over:
            if d.y + d.h * 0.3 < 0:
                print(f"Game Over! Score: {score}")
                game_over = not game_over
                bucket.color = (1, 0, 0)
                diamonds = []

            else:
                if d.collide(bucket):
                    score += 1
                    print(f"Score: {score}")
                    level = levels.get(score, level )
                    diamonds = []
                    diamonds.append(Diamond(random.randint(20, W_Width-20), W_Height, random_color()))

                d.y -= level * dt
        d.draw()

    for id, icon in bar_icons.items():
        if run and id == "pause":
            pass
        elif not run and id == "play":
            pass
        else: icon.draw()

    glutSwapBuffers()

def animation():
    glutPostRedisplay()


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
wind = glutCreateWindow(b"Catch the Diamonds!")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animation)
glutKeyboardFunc(keyboard_press)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKey_press)

glutMainLoop()		#The main loop of OpenGL