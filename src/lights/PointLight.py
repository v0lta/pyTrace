'''
Created on Feb 23, 2016

@author: moritz
'''
from src.lights import Light
import numpy as np

class PointLight(Light):
    '''
    This class implements point lights
    '''

    def l(self, hitPoint):
        '''
        Return the vector pointing towards the light source.
        '''
        res = self.position.getArray3() - hitPoint.getArray3()
        res = res/np.linalg.norm(res)
        return res
        
    def L(self):
        '''
        Return the light source intensity.
        '''
        return self.ls * self.color.getColor()
        