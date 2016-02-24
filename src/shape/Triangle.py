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
        The intersection routine taken from the book.
        '''
        pa = self.a; pb = self.b; pc = self.c;
        
        if self.transformation != None:
            rayInv = self.transformation.transformInverse(ray)
            ro = rayInv.origin[0:3]
            rd = rayInv.direction[0:3]
        else:        
            ro = ray.origin.getArray3()
            rd = ray.direction.getArray3()
        
        
        a = pa[0] - pb[0]; b = pa[0] - pc[0]; c = rd[0]; d = pa[0] - ro[0];
        e = pa[1] - pb[1]; f = pa[1] - pc[1]; g = rd[1]; h = pa[1] - ro[1];
        i = pa[2] - pb[2]; j = pa[2] - pc[2]; k = rd[2]; l = pa[2] - ro[2];
        
        m = f*k - g*j; n = h*k - g*l; p = f*l - h*j;
        q = g*i - e*k; s = e*j - f*i;
        
        invDenom = 1.0 / (a*m + b*q + c*s) 
        
        e1 = d*m - b*n - c*p;
        beta = e1 * invDenom
        
        if beta < 0.0:
            return Intersection(False)
        
        r = e*l - h*i
        e2 = a*n + d*q + c*r
        gamma = e2*invDenom
        
        if (gamma < 0.0):
            return Intersection(False)
        
        if (beta + gamma > 1.0):
            return Intersection(False)
        
        e3 = a*p - b*r + d*s
        t = e3 * invDenom
        
        if t < Constants.epsilon:
            return Intersection(False)
        
        hitPointArray = ro + t*rd 
        hitPoint = self.transformation.transformPoint( Point( npArray = hitPointArray ))
        hitNormalArray = (1 - beta - gamma)*self.an.getArray3() + beta*self.bn.getArray3() + gamma*self.cn.getArray3()
        hitNormal = self.transformation.transformNormal( Normal(npArray = hitNormalArray))
        return Intersection(True, hitNormal, hitPoint, self.color)
        