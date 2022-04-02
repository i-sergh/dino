import cv2
import numpy as np
from time import sleep
import math
main_cnv = np.ones( ( 800, 800, 3), dtype=np.uint8() )

class Rect:
    back_color = (1,1,1)
    color = (0, 0, 120)
    def __init__(self, y, x, L, H=None):
        self.x = x
        self.y = y
        self.L = L
        if H == None:
            self.H = L
        else:
            self.H = H
            
    def draw(self, cnv):
        cnv[self.y:self.y+self.L,
            self.x:self.x+self.H,
            :] = self.color
    def destroy (self, cnv):
        cnv[self.y:self.y+self.L ,
            self.x:self.x+self.H,
            :] = self.back_color
class Cact(Rect):
    
    def __init__(self, y, x, L, H=None ):
        super().__init__(y,x,L,H)
        self.X = x
        self.Y = y
    
    color = (0, 255,0)
    back_color = (1,1,1)
    speed = 1
    def moveLeft( self, cnv ):
        if self.x > 0:
            self.destroy(cnv)
            self.x = self.x - self.speed
            self.draw(cnv)
        else:
            self.destroy(cnv)
            self.reborn(cnv)
    def reborn (self, cnv):
        self.x = self.X
        self.y = self.Y
        self.draw(cnv)

class Dino(Cact):
    '''
    def __init__ (self ):
        super().__init__()
        '''
    color = (200, 0,255)
    velocity = 0
    gravity = -5
    def jump(self, cnv):
        self.velocity = 10
        
    def move (self, cnv):
        
        self.destroy(cnv)
        self.y = self.y - self.velocity + self.gravity
        self.velocity -= 1
         
        if self.y < self.Y:
            self.draw (cnv)

            while cnv[self.y - self.velocity + self.gravity + self.L, self.x + self.L, 1] == 255:
                #print(True)
                self.velocity =   abs( self.gravity)
                
                self.destroy(cnv)
                self.y = self.y - self.velocity + self.gravity
                self.draw (cnv)
                #print(self.velocity)
                #self.y
            
                
        else:
            self.velocity = 0
            self.y = self.Y
            
            
            

     
   
c = Cact(700, 600, 40, 160)
c2 = Cact(500, 600, 40, 160)
dino = Dino (700, 100, 40)  
dino.reborn(main_cnv)
while True:
    c.moveLeft(main_cnv)
    c2.moveLeft(main_cnv)
    cv2.imshow('dino', main_cnv)

    dino.move(main_cnv)

    key = cv2.waitKey(1)
    if key ==27:
        break
    if key == 32:
        dino.jump(main_cnv)
    if key == ord('a'):
        dino.moveLeft(main_cnv)
    sleep(0.001)

cv2.destroyAllWindows()
