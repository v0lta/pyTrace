'''
Created on Feb 22, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants
from src.math import Intersection
from src.math import Normal
from src.math import Point
import numpy as np

class Triangle(Shape):
    '''
    A triangle object 
    '''
    def __init__(self, a, b, c, color, reflectivity, transformation=None, an=None, bn=None, cn=None ):
        '''
        Constructor for the triangle class taking the three edge points a,b and c.
        '''
        self.a = a.getArray3()
        self.b = b.getArray3()
        self.c = c.getArray3()
        self.color = color
        self.reflectivity = reflectivity
        if transformation != None:
            self.transformation = transformation
        if an != None:
            self.an = an
        else:
            self.an = np.cross((self.c -self.a), (self.b - self.a))
        if bn != None:
            self.bn = bn
        else:
            self.bn = np.cross((self.a - self.b), (self.c -self.b))
        if cn != None:
            self.cn = cn
        else:
            self.cn = np.cross((self.a - self.c), (self.b -self.c))
        
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
            return Intersection(False)
        else:        
            if   ( (0.0 <= x[0])      and (x[0] <= 1.0)
                   and (0.0 <= x[1])      and (x[0] <= 1.0)
                   and (0.0 <= x[0]+x[1]) and (x[0]+x[1] <= 1.0)):
                hitPointArray = o + x[2]*d 
                hitPoint = self.transformation.transformPoint( Point( npArray = hitPointArray ))
                hitNormalArray = (1 - x[0] - x[1])*self.an.getArray3() + x[0]*self.bn.getArray3() + x[1]*self.cn.getArray3()
                hitNormal = self.transformation.transformNormal( Normal(npArray = hitNormalArray))
                return Intersection(True,hitNormal,hitPoint)
            else:
                return Intersection(False) 
        