from OpenGL.GL import *

def convert_zone(x: int, y: int, zone: int, convert_to: int) -> tuple:
    #other zones to 0
    forward: dict[int, tuple] = {
          0: [x, y],
          1: [y, x],
          2: [y, -x],
          3: [-x, y],
          4: [-x, -y],
          5: [-y, -x],
          6: [-y, x],
          7: [x, -y],
    }
    #zone 0 to others
    backwark: dict[int, tuple] = {
          0: [x, y],
          1: [y, x],
          2: [-y, x],
          3: [-x, y],
          4: [-x, -y],
          5: [-y, -x],
          6: [y, -x],
          7: [x, -y],
    }

    if convert_to == 0:
        return forward[zone]
    else: return backwark[convert_to]

def find_zone(dx: int, dy: int)-> int:
    if abs(dx) > abs(dy): # zone 0, 3, 4, 7
        if dx > 0 and dy >= 0:
            return 0
        elif dx > 0 and dy < 0:
            return 7
        elif dx < 0 and dy >= 0:
            return 3
        else: return 4
    # below represent 1,2,5,6
    if dy > 0 and dx >= 0:
        return 1
    elif dy > 0 and dx < 0:
        return 2
    elif dy < 0 and dx < 0:
        return 5
    return 6

def draw(pos: list, color: tuple):
    glPointSize(3)
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(*pos)
    glEnd()

def MPL(start: list, end: list, color)-> None:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    zone = find_zone(dx, dy)
    #convert to zone 0
    start = convert_zone(start[0], start[1], zone, 0)
    end = convert_zone(end[0], end[1], zone, 0)
    #new dx and dy for zone 0
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    #algorithms formula
    de = 2*dy
    dne = 2*(dy-dx)
    d = 2*dy - dx

    while start[0] <= end[0]:
        draw(convert_zone(start[0], start[1], 0, zone), color)

        if d < 0:
            start[0] += 1
            d += de
        else:
            start[0] += 1
            start[1] += 1
            d += dne
