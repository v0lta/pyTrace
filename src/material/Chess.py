'''
Created on Feb 24, 2016

@author: moritz
'''
from math import floor
from src.math import Point
from src.math import Color

class Chess(object):
    '''
    A surface that looks like a chessboard.
    '''


    def __init__(self, color1, color2, s):
        '''
        Takes two colors for the different rectangles, as well as the rectangle
        size s.
        '''
        self.color1 = color1
        self.color2 = color2
        self.s      = s
        
        
    def getColor(self, texPoint):
        '''
        Takes a point in texture coordinates and returns the corresponding color.
        '''
        p = texPoint.getArray3()
        s = self.s
        
        if (int(floor( p[0]/s)) + int(floor( p[1]/s))
             + int(floor( p[2]/s)))%2 == 0:
            return self.color1
        else:
            return self.color2