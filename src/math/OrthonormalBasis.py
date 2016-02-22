'''
Created on Feb 12, 2016

@author: moritz
'''

import numpy as np
from src.math.Point import Point

class OrthonormalBasis(object):
    '''
    Represents a basis in three dimensions consisting of three orthogonal
    Vectors of unit length.
    '''

    def __init__(self, e, l, up):
        '''
        Takes eye point, look at point and up vector to come up with a nice basis,
        following page 154.
        '''
        if type(e) == Point:
            e = e.getArray3()
        if type(l) == Point:
            l = l.getArray3()
        if type(up):
            up = up.getArray3()     
        
        self.w = (e - l)
        self.w = self.w/np.linalg.norm(self.w)
        self.u = np.cross(up,self.w)
        self.u = self.u/np.linalg.norm(self.u);
        self.v = np.cross(self.w,self.u)
        
    def toString(self):
        '''
        Returns the basis vectors as a string.
        '''
        return ( str(self.u) + str(self.v) + str(self.w) )
        