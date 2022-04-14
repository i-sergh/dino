import cv2
import numpy as np

from random import randint
from time import sleep


class Rect:
    def __init__ (self,cnv, y, x, H, W=None,\
                  clr=(0,255,0), bclr=(1,1,1)):
        #self.senter_y = y
        #self.senter_x = x
        self.y = y
        self.x = x
        self.H = int( H//2 )
        self.clr = clr
        self.back_clr = bclr
        self.cnv = cnv
        
        if W == None:
            self.W = int( H//2 )
        else:
            self.W = int( W//2 )

    def draw(self):
        self.cnv[ self.y - self.W : self.y + self.W,
                 self.x - self.H : self.x + self.H] = self.clr
    def destroy(self):
        self.cnv[ self.y - self.W : self.y + self.W,
                 self.x - self.H : self.x + self.H] = self.back_clr



if __name__ == '__main__':

    cnv = np.ones((800, 800, 3), dtype=np.uint8() )

    test_rect = Rect(cnv, 400, 400, 100, 50)

    while True:

        cv2.imshow('main test', cnv)

        key = cv2.waitKey(1)

        if key == 27:
            break
        if key == ord('q'):
            test_rect.draw()
        if key == ord('e'):
            test_rect.destroy()
cv2.destroyAllWindows()
