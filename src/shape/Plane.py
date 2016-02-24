'''
Created on Feb 22, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants, Intersection, Point, Normal
from src.material import Chess
import numpy as np



class Plane(Shape):
    '''
    A class, which allows to intersect planes.
    '''
    def __init__(self, a, n, material, reflectivity):
        self.a = a.getArray3()  #point a describing, where the plane is.
        self.n = n.getArray3()  #normal n describing the plane's orientation.
        self.material = material
        self.reflectivity = reflectivity
    
    def intersect(self, ray):
        '''
        The ray object intersection function for a planes without transformations.
        '''
        ro = ray.getOrigin3()
        rd = ray.getDirection3()
        
        if np.dot == np.dot(self.n,rd):
            return Intersection(False)
        else:
            t = (np.dot(self.n,self.a) - np.dot(self.n,ro)) / np.dot(self.n,rd)
            if (t <= Constants.epsilon):
                return Intersection(False)
            else:
                pointArray = ro + t*rd;
                color = self.material.getColor(Point(npArray = pointArray))
                return Intersection(True, Normal(npArray = self.n),Point(npArray = pointArray), color)
        
        