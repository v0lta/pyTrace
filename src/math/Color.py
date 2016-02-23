'''
Created on Feb 23, 2016

@author: moritz
'''
import numpy as np

class Color(object):
    '''
    Contains a numpy array with color definitions for red, green
    and blue raning from 1 to 255.
    '''


    def __init__(self, red=None,green=None,blue=None,npArray=None):
        '''
        Sets up the color.
        '''
        if npArray != None:
            self.npArray = npArray
        else:
            if (red < 0) or (red > 255):
                raise ValueError, "Red value out of bounds"
            if (green < 0) or (green > 255):
                raise ValueError, "green value out of bounds"
            if (blue < 0) or (blue > 255):
                raise ValueError, "blue value out of bounds"
            self.npArray = np.array([red,green,blue])
            
    def getColor(self):
        return self.npArray