'''
Created on Feb 15, 2016

@author: moritz
'''
from src.shape.Shape import Shape
import numpy as np

class Sphere(Shape):
    '''
    A class implementing unit spheres spheres (c = 0.0, r = 1.0). 
    Larger or displaced spheres can be obtained by using transformations.
    '''
    def __init__(self, transformation):
        self.transformation = transformation
    
    def intersect(self, ray):
        '''
        The ray object intersection function for spheres.
        '''
        rayInv = self.transformation.transformInverse(ray)

        ro = rayInv.origin[0:3]
        rd = rayInv.direction[0:3]

        a = np.dot(rd.transpose(), rd) 
        b = 2.0 * np.dot(ro.transpose(), rd)
        c = np.dot(ro.transpose(), ro) - 1.0
 
        #the discriminant decides what values the roots are going to have.
        d = b*b - 4.0*a*c
        
        if (d < 0):
            # Negative discriminant => no intersections.
            return False
        else:
            if (b < 0):
                q = -0.5 *( b - np.sqrt(d))
            else:
                q = -0.5 *( b + np.sqrt(d))
        
        t0 = q/a;
        t1 = c/q;
        
        #only report a hit if the intersection has a positive t.
        return (t0 >= 0) or (t1 >= 0)
            
            
        
        
    