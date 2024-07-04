from mpl_line import MPL


class Shape:
    def __init__(self, x, y, color, w=36, h=36):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h


    def collide(self, x1, y1) -> bool:
        return self.x - self.w/2 <= x1 <= self.x + self.w/2 and self.y >= y1 >= self.y - self.h


class Diamond(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 20, 28)

    def draw(self):
        MPL([self.x, self.y], [self.x+ self.w/2, self.y+self.h/2], self.color)
        MPL([self.x, self.y], [self.x- self.w/2, self.y+self.h/2], self.color)
        MPL([self.x- self.w/2, self.y+self.h/2], [self.x, self.y+self.h], self.color)
        MPL([self.x+ self.w/2, self.y+self.h/2], [self.x, self.y+self.h], self.color)
    
    def collide(self, other) -> bool:
        return self.x - self.w/2 < other.x + other.w/2 \
            and self.x + self.w/2 > other.x - other.w/2 \
            and self.y < other.y - other.h/2 \
            and self.y + self.h > other.y
    

class Reset(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def draw(self):
        MPL([self.x, self.y], [self.x - self.w/2, self.y - self.h/2], self.color)
        MPL([self.x - self.w/2, self.y - self.h/2], [self.x, self.y - self.h], self.color)
        MPL([self.x - self.w/2, self.y - self.h/2], [self.x + self.w/2, self.y - self.h/2], self.color)


class Pause(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def draw(self):
        MPL([self.x - self.w * 0.3, self.y], [self.x + self.w * 0.5, self.y - self.h * 0.5], self.color)
        MPL([self.x - self.w * 0.3, self.y-self.h], [self.x + self.w * 0.5, self.y - self.h * 0.5], self.color)
        MPL([self.x - self.w * 0.3, self.y-self.h], [self.x - self.w * 0.3, self.y], self.color)


class Play(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def draw(self):
        MPL([self.x - self.w * 0.4, self.y], [self.x - self.w * 0.4, self.y - self.h], self.color)
        MPL([self.x + self.w * 0.4, self.y], [self.x + self.w * 0.4, self.y - self.h], self.color)


class Exit(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def draw(self):
        MPL([self.x - self.w * 0.5, self.y], [self.x + self.w * 0.5, self.y - self.h], self.color)
        MPL([self.x + self.w * 0.5, self.y], [self.x - self.w * 0.5, self.y - self.h], self.color)


class Bucket(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 150, 20)
    
    def draw(self):
        MPL([self.x - self.w/2, self.y], [self.x + self.w/2, self.y], self.color)
        MPL([self.x - self.w * 0.4, self.y - self.h], [self.x + self.w * 0.4, self.y - self.h], self.color)
        MPL([self.x - self.w * 0.4, self.y - self.h], [self.x - self.w * 0.5, self.y], self.color)
        MPL([self.x + self.w * 0.4, self.y - self.h], [self.x + self.w * 0.5, self.y], self.color)

