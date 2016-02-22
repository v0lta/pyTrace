'''
Created on Feb 22, 2016

@author: moritz
'''
from src.shape import Shape
from src.math import Constants
import numpy as np


class SimplePlane(Shape):
    '''
    A class, which allows to intersect planes.
    '''
    def __init__(self, a, n):
        self.a = a.getArray3()  #point a describing, where the plane is.
        self.n = n.getArray3()  #normal n describing the plane's orientation.
    
    def intersect(self, ray):
        '''
        The ray object intersection function for simple spheres without transformations.
        '''
        ro = ray.origin.getArray3()
        rd = ray.direction.getArray3()
        
        if np.dot == np.dot(self.n,rd):
            return False
        else:
            t = (np.dot(self.n,self.a) - np.dot(self.n,ro)) / np.dot(self.n,rd)
            return (t >= Constants.epsilon)
        
        