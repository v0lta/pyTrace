'''
Created on Feb 15, 2016

@author: moritz
'''
import numpy as np

class Transformation(object):
    '''
    This class represents transformation capable of transforming 3d objects.
    '''

    def __init__(self, matrix, inverse):
        '''
        Constructor which stores the transformation matrix and it's inverse.
        '''
        self.matrix  = matrix
        self.inverse = inverse
        
    def translation(self, x, y, z):
        '''
        Creates a translation matrix and it's inverse. The translation displaces an object along
        the x,y and z values given.
        '''
        self.matrix  = np.matrix([[1, 0, 0,  x], [0, 1, 0,  y], [0, 0, 1,  z], [0, 0, 0, 1]])
        self.inverse = np.matrix([[1, 0, 0, -x], [0, 1, 0, -y], [0, 0, 1, -z], [0,0,0,1]])
        
    def scale(self, x, y, z):
        '''
        Creates a scaling matrix and it's inverse.
        '''
        self.matrix  = np.matrix([[x,   0, 0, 0],[0, y,   0, 0], [0, 0, z,   0], [0, 0, 0, 1]])
        self.inverse = np.matrix([[1/x, 0, 0, 0],[0, 1/y, 0, 0], [0, 0, 1/z, 0], [0, 0, 0, 1]])
    
    def rotateX(self, theta):
        '''
        Rotates an object theta degrees around the x-axis.
        '''
        theta = theta*(np.pi/180)
        self.matrix = np.matrix([1,            0,             0,0],
                                [0,np.cos(theta),-np.sin(theta),0],
                                [0,np.sin(theta), np.cos(theta) ,0],
                                [0,            0,             0,1])
        self.inverse = np.matrix([1,           0,             0,0],
                                [0,np.cos(theta),np.sin(theta),0],
                                [0,-np.sin(theta), np.cos(theta) ,0],
                                [0,            0,             0,1])
        
    def rotateY(self, theta):
        '''
        Rotates an object theta degrees around the y-axis.
        '''
        theta = theta*(np.pi/180)
        self.matrix = np.matrix([np.cos(theta),  0, np.sin(theta),0],
                                [            0,  1,             0,0],
                                [-np.sin(theta), 0, np.cos(theta),0],
                                [             0, 0,             0,1])
        self.inverse = np.matrix([np.cos(theta), 0, -np.sin(theta),0],
                                [            0,  1,             0,0],
                                [np.sin(theta), 0, np.cos(theta),0],
                                [             0, 0,             0,1])
        
        
    def rotateZ(self, theta):
        '''
        Rotates an object theta degrees around the z-axis.
        '''
        theta = theta*(np.pi/180)
        self.matrix = np.matrix([np.cos(theta),  -np.sin(theta),0,0],
                                [np.sin(theta),   np.cos(theta),0,0],
                                [            0,               0,1,0],
                                [            0,               0,0,1])
        self.matrix = np.matrix([np.cos(theta),  np.sin(theta),0,0],
                                [-np.sin(theta),   np.cos(theta),0,0],
                                [            0,               0,1,0],
                                [            0,               0,0,1])
    
    
        