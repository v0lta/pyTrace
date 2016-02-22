'''
Created on Feb 12, 2016

@author: moritz
'''
from src.math import Point

class Ray(object):
    '''
    Represents a ray in three dimensions.
    '''

    def __init__(self, origin, direction):
        '''
        Sets the starting point or origin and the direction into which the ray moves.
        '''
        self.origin = origin
        self.direction = direction