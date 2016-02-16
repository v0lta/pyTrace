'''
Created on Feb 15, 2016

@author: moritz
'''
from src.shape.Shape import Shape

class Sphere(Shape):
    '''
    A class implementing spheres.
    '''
    def __init__(self, transformation):
        self.transformation = transformation
    
    def intesect(self, ray):
        '''
        The ray object intersection function for spheres.
        '''
        rayInv = self.transformation.transfromInverse(ray)
        origin = rayInv.origin
        
        
    