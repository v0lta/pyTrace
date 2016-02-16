'''
Created on Feb 12, 2016

@author: moritz
'''

import numpy as np

class OrthonormalBasis(object):
    '''
    Represents a basis in three dimensions consisting of three orthogonal
    Vectors of unit length.
    '''


    def __init__(self, a, b):
        '''
        Takes two numpy arrays and computes a cross product to find another orthogonal vector.
        '''
        self.w = np.linalg.norm(a)
        self.u = np.cross(a,b)
        self.u = np.linalg.norm(self.u);
        self.v = np.cross(self.w,self.u)
        
    def toString(self):
        '''
        Returns the basis vectors as a string.
        '''
        return ( str(self.u) + str(self.v) + str(self.w) )
        