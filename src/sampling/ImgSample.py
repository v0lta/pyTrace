'''
Created on Feb 15, 2016

@author: moritz
'''

class ImgSample(object):
    '''
    This class contains samples of the scene, with a coordinates x and y in the image
    space.
    '''


    def __init__(self, x, y, dx=None, dy=None):
        '''
        The constructor creates a new sample. X and y are in image space.
        dx and dy are deviation from the sample mean.
        '''
        self.x = x
        self.y = y
        
        if dx==None:
            self.dx = 0.5
        else:
            self.dx = dx
            
        if dy==None:
            self.dy = 0.5
        else:
            self.dy = dy
        