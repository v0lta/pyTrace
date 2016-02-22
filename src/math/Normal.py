'''
Created on Feb 22, 2016

@author: moritz
'''
import numpy as np

class Normal(object):
    '''
    A class for normal data encapsulation.
    '''

    def __init__(self, a,b,c):
        '''
        Initialize the normal.
        '''
        self.a = a
        self.b = b
        self.c = c
        self.array = np.linalg.norm(np.array(a,b,c))
        
    def getArray3(self):
        return self.array