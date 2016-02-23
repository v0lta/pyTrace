'''
Created on Feb 23, 2016

@author: moritz
'''

class Light(object):
    '''
    Abstract light interface.
    '''
    
    def __init__(self, position, shadows, color, ls):
        '''
        Requires the position of the point light to create the instance.
        ''' 
        if (type(self) == Light):
            raise NotImplementedError, "Cannot create object of abstract class Light"
   
        self.position = position
        self.shadows = shadows
        self.color = color
        self.ls    = ls

    def getDirection(self):
        raise NotImplementedError
    
    def L(self):
        raise NotImplementedError
        