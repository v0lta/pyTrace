'''
Created on Feb 12, 2016

@author: moritz
'''
from src.camera import Camera
from src.math import OrthonormalBasis
from src.sampling import ImgSample
from src.math import Ray
import math

class PerspectiveCamera(Camera):
    '''
    A class implementing a camera with perspective transformation.
    '''

    def __init__(self, xResolution, yResolution, origin, lookAt, up, fov):
        '''
        set the resolution in x and y, as well as the origin the up and look at 
        vector. Additionally the field of view has to be defined.
        '''
        if (xResolution < 1):
            raise NameError('The horizontal resolution must be larger or equal to one.')
        if (yResolution < 1):
            raise NameError('The vertical resolution must be larger or equal to one.')
        if (fov <= 0):
            raise NameError(' The field of view must be greater then zero degrees.')
        if (fov >= 180):
            raise NameError(' The field of view must be smaller then 180 degrees.')
        
        self.origin = origin;
        self.basis = OrthonormalBasis(lookAt, up);

        self.invxResolution = 1.0 / xResolution;
        self.invyResolution = 1.0 / yResolution;
        self.width = 2.0 * math.tan(0.5 * fov);
        self.height = ( yResolution * self.width) * self.invxResolution;
        
    def generateRay(self,imgSample):
        u = self.width * ( imgSample.x * self.invxResolution - 0.5)
        v = self.height * ( imgSample.y * self.invyResolution - 0.5)
        
        direction = self.lookAt; #FIXME
        
        return Ray(self.origin, direction)