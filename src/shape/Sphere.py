'''
Created on Feb 15, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants
from src.math import Intersection
from src.math import Normal
from src.math import Point
import numpy as np


class Sphere(Shape):
    '''
    A class implementing unit spheres spheres (c = 0.0, r = 1.0). 
    Larger or displaced spheres can be obtained by using transformations.
    '''
    def __init__(self, color, reflectivity, transformation):
        self.transformation = transformation
        self.color = color
        self.reflectivity = reflectivity
    
    def intersect(self, ray):
        '''
        The ray object intersection function for spheres.
        '''
        rayInv = self.transformation.transformInverse(ray)

        ro = rayInv.origin[0:3]
        rd = rayInv.direction[0:3]

        a = np.dot(rd, rd) 
        b = 2.0 * np.dot(ro, rd)
        c = np.dot(ro, ro) - 1.0
 
        #the discriminant decides what values the roots are going to have.
        d = b*b - 4.0*a*c
        
        if (d < 0):
            # Negative discriminant => no intersections.
            return Intersection(False)
        else:
            if (b < 0):
                q = -0.5 *( b - np.sqrt(d))
            else:
                q = -0.5 *( b + np.sqrt(d))
        
        t0 = q/a;
        t1 = c/q;
        
        #only report a hit if the intersection has a positive t > epsilon.
        hasInt = (t0 >= Constants.epsilon) or (t1 >= Constants.epsilon)
        if hasInt:
            if (t0 < t1):
                hitPointArray = ro + t0*rd 
                hitPoint = self.transformation.transformPoint( Point( npArray = hitPointArray ))
                hitNormal = self.transformation.transformNormal( Normal( npArray = hitPointArray ))
                return Intersection(hasInt, hitNormal, hitPoint) 
            else:
                hitPointArray = ro + t1*rd 
                hitPoint = self.transformation.transformPoint( Point( npArray = hitPointArray ))
                hitNormal = self.transformation.transformNormal( Normal( npArray = hitPointArray ))
                return Intersection(hasInt, hitNormal, hitPoint)
        else:
            return Intersection(False) 
            

        
        
    