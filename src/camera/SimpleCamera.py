'''
Created on Feb 17, 2016

@author: moritz
'''
from src.math.Ray import Ray
from src.math.Point import Point

class SimpleCamera(object):
    '''
    A simple camera without a perspective projection.
    '''


    def __init__(self, xResolution, yResolution, origin, lookat,s):
        '''
        Sets up the simple view plane camera
        '''
        self.hres = xResolution
        self.vres = yResolution
        self.origin      = origin
        self.lookat      = lookat
        self.s    = s   #Pixel size
        
    def generateRay(self,sample):
        '''
        Generate Rays from the center of the corresponding pixel according to page
        66 of the book.
        '''
        xw = self.s *(sample.x - self.hres/2.0 + 0.5)
        yw = self.s *(sample.y - self.vres/2.0 + 0.5)
        
        origin = Point(self.origin.x + xw, self.origin.y + yw, self.origin.z )
        direction = self.lookat
        
        ray = Ray(origin,direction)
        return ray
        