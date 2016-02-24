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
                self.npArray = np.array([0., 0., 0., 1.])
            else:
                self.npArray = np.array([x,y,z, 1.])
        else:
            if len(npArray) == 4:
                self.npArray = npArray
            else:
                self.npArray = np.array([npArray[0], npArray[1], npArray[2], 1.0])
                
    def set(self,npArray):
                self.npArray = npArray
                
    def getArray4(self):
        return self.npArray
    def getArray3(self):
        return self.npArray[0:3]
        
    