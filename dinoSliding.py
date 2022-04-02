import cv2

import numpy as np
from time import sleep
#color = np.array( (180, 180, 180),  dtype=np.uint8()  )
cnv = np.ones ( (800, 800, 3), dtype=np.uint8() ) #* color

class Rect:
    back_clr = (1, 1, 1)

    def __init__ (self, y, x, H, W=None, clr = (0,255,0) ):
        self.y = y
        self.x = x
        self.H = H//2
        self.clr = clr
        if W == None:
            self.W = H//2
        else:
            self.W = W//2
            
    def draw(self, cnv):
        cnv[ self.y - self.W : self.y + self.W,
             self.x - self.H : self.x + self.H] = self.clr
    def destroy(self, cnv):
        cnv[ self.y - self.W : self.y + self.W,
             self.x - self.H : self.x + self.H] = self.back_clr

class Kakt(Rect):
    def __init__ (self, y, x, H, W=None, clr = (255,255,0) ):
        super().__init__(y, x, H, W, clr)
        self.X = x
        self.Y = y
        
        self.speed = 4
    def moveLeft(self,cnv):
        if self.x - self.H > 0:
            self.destroy(cnv)
            self.x = self.x - self.speed
            self.draw(cnv)
        else:
            self.destroy(cnv)
            self.reborn(cnv)
    def reborn(self, cnv):
        self.x = self.X
        self.y = self.Y
        self.draw(cnv)
class Dino(Kakt):
    velocity = 0
    gravity = -5
    def jump(self):
        self.velocity = 10
        
    def move (self,cnv):
        self.destroy(cnv)
        self.y = self.y - self.velocity + self.gravity
        self.velocity -= 1
        if self.y < self.Y:
            self.draw(cnv)
            while cnv [self.y - self.velocity + self.gravity + self.H ,
                       self.x, 0] == 255 or \
                  cnv [self.y, self.x + self.W, 1] == 255:
                self.destroy(cnv)
                self.velocity = self.gravity
                self.y = self.y - self.velocity + self.gravity
                self.draw (cnv)
        else:
            self.velocity = self.gravity
            self.y = self.Y
            self.draw(cnv)
            
            while cnv [self.y - self.velocity + self.gravity + self.H ,
                       self.x, 0] == 255 or \
                  cnv [self.y, self.x + self.W, 1] == 255:
                self.destroy(cnv)
                self.velocity = - self.gravity
                self.y = self.y - self.velocity + self.gravity
                self.draw (cnv)
            
            
            
            
c = Kakt(700, 600, 200, 80)
c.reborn(cnv)
d = Dino(700, 200, 40, 40, clr=(0,255,255))
d.reborn(cnv)
while True:
    cv2.imshow('izo', cnv)
    c.moveLeft(cnv)
    d.move(cnv)
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == 32:
        d.jump()
    sleep(0.02)
