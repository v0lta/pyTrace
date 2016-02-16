'''
Created on Feb 12, 2016

@author: moritz
'''

class Camera(object):
    '''
    abstract camera class which outline the functions each camera has to implement. 
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        raise NotImplementedError()

    def generateRay(self,sample):
        raise NotImplementedError()
    
        