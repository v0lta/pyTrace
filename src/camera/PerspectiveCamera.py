'''
Created on Feb 12, 2016

@author: moritz
'''
from src.camera import Camera
from src.math import OrthonormalBasis
from src.math.Point import Point
from src.sampling import ImgSample
from src.math import Ray
import numpy as np

class PerspectiveCamera(Camera):
    '''
    A class implementing a camera with perspective transformation.
    As described in chapter 9 of the ray tracing-book.
    '''

    def __init__(self, xResolution, yResolution, origin, lookAt, up, s, d):
        '''
        Construct a camera which a ray originating from the same point but
        different directions.
        set the resolution in x and y, as well as the origin the up and look at 
        vector. Additionally the field of view has to be defined.
        '''
        if (xResolution < 1):
            raise NameError('The horizontal resolution must be larger or equal to one.')
        if (yResolution < 1):
            raise NameError('The vertical resolution must be larger or equal to one.')
        if (s <= 0):
            raise NameError('pixel sive s must be positive')
        if (d <= 0):
            raise NameError('view plane distance d must be positive')
        
        self.basis = OrthonormalBasis(lookAt, up);
        self.hres   = xResolution
        self.vres   = yResolution
        self.origin = origin
        self.s      = s   #Pixel size      
        self.d      = d   #view plane distance  
        
    def generateRay(self,imgSample):
        xv = self.s * (imgSample.x - self.hres/2 + imgSample.dx)
        yv = self.s * (imgSample.y - self.vres/2 + imgSample.dy)
        
        direction = xv*self.basis.u + yv*self.basis.v - self.d*self.basis.w
        direction = direction/np.linalg.norm(direction)
        
        #TODO: Replace point class by numpy array!
        return Ray(self.origin, Point(direction[0],direction[1],direction[2]))