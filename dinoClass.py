import cv2

import numpy

from time import sleep


class Rect:
    def __init__ (self, y, x, H, W=None,\
                  clr=(0,255,0), bclr=(1,1,1)):
        self.senter_y = y
        self.senter_x = x
        self.H = int( H//2 )
        self.clr = clr
        self.b_clr = bclr

        if W == None:
            self.W = int( H//2 )
        else:
            self.W = int( W//2 )

    #def draw(self):

    ## TODO: deny from cnv in methods   
