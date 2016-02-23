'''
Created on Feb 22, 2016

@author: moritz
'''
import numpy as np

class Normal(object):
    '''
    A class for normal data encapsulation.
    '''

    def __init__(self, a=None,b=None,c=None,npArray=None):
        '''
        Initialize the normal.
        '''
        if npArray != None:
            self.npArray = npArray
        else:
            self.npArray = np.array(a,b,c)
        
        #normalize
        self.npArray = self.npArray/np.linalg.norm(npArray)
        
    def getArray3(self):
        return self.npArray[0:3]
    def getArray4(self):
        return np.array([self.npArray[0], self.npArray[1], self.npArray[2], 1.0])