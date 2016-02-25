'''
Created on Feb 12, 2016

@author: moritz
'''
import numpy as np

class Ray(object):
    '''
    Represents a ray in three dimensions.
    '''

    def __init__(self, origin, direction):
        '''
        Sets the starting point or origin and the direction into which the ray moves.
        '''
        if type(origin).__module__ == np.__name__:
            self.origin = origin
            self.direction = direction
        else:
            self.origin = origin.getArray4()
            self.direction = direction.getArray4()

        
    def set(self, origin, direction):
        '''
        Only set 4 dim nparrays, no type check for speed.
        '''
        self.origin = origin
        self.direction = direction
        
    def getOrigin4(self):      
        return self.origin
    def getOrigin3(self):
        return self.origin[0:3]
    def getDirection4(self):
        return self.direction
    def getDirection3(self):
        return self.direction[0:3]
    