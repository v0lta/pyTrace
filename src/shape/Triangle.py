'''
Created on Feb 22, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants
import numpy as np

class Triangle(Shape):
    '''
    A triangle object 
    '''
    def __init__(self, a,b,c,transformation=None):
        '''
        Constructor for the triangle class taking the three edge points a,b and c.
        '''
        self.a = a.getArray3()
        self.b = b.getArray3()
        self.c = c.getArray3()
        self.transformation = transformation
        
    def intersect(self, ray):
        '''
        The intersection routine
        '''
        a = self.a; b = self.b; c = self.c;
        
        if self.transformation != None:
            rayInv = self.transformation.transformInverse(ray)
            o = rayInv.origin[0:3]
            d = rayInv.direction[0:3]
        else:        
            o = ray.origin.getArray3()
            d = ray.direction.getArray3()
        
        
        A = [[a[0] - b[0], a[0] - c[0], d[0]],
             [a[1] - b[1], a[1] - c[1], d[1]],
             [a[2] - b[2], a[2] - c[2], d[2]]]
        
        b = [ a[0] - o[0],
              a[1] - o[1],
              a[2] - o[2]];
              
        x = np.linalg.lstsq(A, b)[0]
        
        if x[2] < Constants.epsilon:
            return False
        else:        
            return   ( (0.0 <= x[0])      and (x[0] <= 1.0)
                   and (0.0 <= x[1])      and (x[0] <= 1.0)
                   and (0.0 <= x[0]+x[1]) and (x[0]+x[1] <= 1.0))
        