'''
Created on Feb 15, 2016

@author: moritz
'''

class ImgSample(object):
    '''
    This class contains samples of the scene, with a coordinates x and y in the image
    space.
    '''


    def __init__(self, x, y):
        '''
        The constructor creates a new sample. X and y are in image space.
        '''
        self.x = x
        self.y = y