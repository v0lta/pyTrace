'''
Created on Feb 12, 2016

@author: moritz
'''
import numpy as np

class Point(object):
    '''
    Point implementation in three dimensions.
    '''
    def __init__(self,x=None,y=None,z=None, npArray=None):
        '''
        Constructor initializing the x,y and z coordinate.
        '''
         
        if (npArray == None): 
            if (x == None) and (y == None) and (z == None):
                self.npArray = np.array([0., 0., 0.])
            else:
                self.npArray = np.array([x,y,z])
        else:
            self.npArray = npArray
                
    def getArray4(self):
        return np.array([self.npArray[0], self.npArray[1], self.npArray[2], 1.0])
    def getArray3(self):
        return np.array([self.npArray[0], self.npArray[1], self.npArray[2]])
        
    