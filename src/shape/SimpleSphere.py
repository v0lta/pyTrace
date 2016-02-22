'''
Created on Feb 18, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants
import numpy as np

class SimpleSphere(Shape):
    '''
    A class implementing spheres with center at c and radius r.
    '''
    def __init__(self, c,r):
        self.c = c.getArray3()
        self.r = r
    
    def intersect(self, ray):
        '''
        The ray object intersection function for simple spheres without transformations.
        '''
        ro = ray.origin.getArray3()
        rd = ray.direction.getArray3()
        
        a = np.dot(rd.transpose(), rd) 
        tmp1 = ro - self.c
        b = 2.0 * np.dot(tmp1.transpose(), rd)
        c = np.dot(tmp1.transpose(), tmp1) - self.r**2
 
        #the discriminant decides what values the roots are going to have.
        d = b*b - 4.0*a*c
        
        if (d < 0):
            # Negative discriminant => no intersections.
            return False
        else:
            if (b < 0):
                q = -0.5*(b - np.sqrt(d))
            else:
                q = -0.5*(b + np.sqrt(d))
        
        t0 = q/a;
        t1 = c/q;
        
        t2 = -0.5 * ( b + np.sqrt(d))/a
        t3 = -0.5 * ( b - np.sqrt(d))/a
        
        #only report a hit if the intersection has a positive t > epsilon.
        return (t0 >= Constants.epsilon) or (t1 >= Constants.epsilon)
            
            
        
        
    