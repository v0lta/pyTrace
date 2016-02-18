'''
Created on Feb 15, 2016

@author: moritz
'''
from src.shape.Shape import Shape
from src.math.Transformation import Transformation
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

        a = np.dot(rayInv.direction, rayInv.direction)
        b = 2.0 * np.dot(rayInv.direction, rayInv.origin)
        c = np.dot(rayInv.origin, rayInv.origin) - 1.0
        
 
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
        
        return (t0 >= 0) or (t1 >= 0)
            
            
        
        
    