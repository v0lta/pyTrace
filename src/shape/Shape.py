'''
Created on Feb 15, 2016

@author: moritz
'''

class Shape(object):
    '''
    Interface which is implemented by all shapes
    '''
    def intesect(self, ray):
        '''
        Each shape should define a ray object intersection function!
        '''
        raise NotImplementedError()
    
        