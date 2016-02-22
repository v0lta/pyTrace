'''
Created on Feb 12, 2016

@author: moritz
'''
import numpy as np

class Point(object):
    '''
    Point implementation in three dimensions.
    '''
    def __init__(self, x=None,y=None,z=None):
        '''
        Constructor initializing the x,y and z coordinate.
        '''
        self.x = x
        self.y = y
        self.z = z
        
        #set defaults.
        if x == None:
            self.x = 0.0
        if y == None:
            self.y = 0.0
        if y == None:
            self.z = 0.0
                
    def getArray4(self):
        return np.array([self.x, self.y, self.z, 1.0])
    def getArray3(self):
        return np.array([self.x, self.y, self.z])
        
    