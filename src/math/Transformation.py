'''
Created on Feb 15, 20.016

@author: moritz
'''
import numpy as np
from src.math import Ray
from src.math import Point
from src.math import Normal

class Transformation(object):
    '''
    This class represents transformation capable of transforming 3d objects.
    '''

    def __init__(self, matrix=None, inverse=None):
        '''
        Constructor which stores the transformation matrix and it's inverse.
        Default values are identity.
        '''
        if matrix == None:
            self.matrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
                                   [ 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
        else:
            self.matrix  = matrix
        if inverse == None:
            self.inverse = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
                                    [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
        else:
            self.inverse = inverse
            
    def transformInverse(self, inRay):
        outOrigin = np.dot(self.inverse, inRay.origin.getArray4())
        outDirection = np.dot(self.inverse, inRay.direction.getArray4())
        outRay = Ray(outOrigin,outDirection) 
        return outRay
    
    def transformNormal(self, normal):
        dataArray = np.dot(self.inverse.transpose(), normal.getArray4())
        if dataArray[3] != 1.0:
            print "error"
        return Normal(npArray = dataArray)
        
    def transformPoint(self, point):    
        dataArray = np.dot(self.matrix, point.getArray4())
        return Point(npArray = dataArray)
        
    def translation(self, x, y, z):
        '''
        Creates a translation matrix and it's inverse. The translation displaces an object along
        the x,y and z values given.
        '''
        self.matrix  = np.dot( self.matrix,np.array([[1., 0., 0.,  x], [0., 1., 0.,  y], [0., 0., 1.,  z], [0., 0., 0., 1.]]))
        self.inverse = np.dot(self.inverse,np.array([[1., 0., 0., -x], [0., 1., 0., -y], [0., 0., 1., -z], [0., 0., 0., 1.]]))
        
        
    def scale(self, x, y, z):
        '''
        Creates a scaling matrix and it's inverse.
        '''
        self.matrix  = np.dot( self.matrix,np.array([[x,     0.0, 0.0, 0.0],[0.0,     y, 0.0, 0.0], [0.0, 0.0,     z, 0.0], [0.0, 0.0, 0.0, 1.0]]))
        self.inverse = np.dot(self.inverse,np.array([[1.0/x, 0.0, 0.0, 0.0],[0.0, 1.0/y, 0.0, 0.0], [0.0, 0.0, 1.0/z, 0.0], [0.0, 0.0, 0.0, 1.0]]))
    
    def rotateX(self, theta):
        '''
        Rotates an object theta degrees around the x-axis.
        '''
        theta = theta*(np.pi/180.0)
        self.matrix  = np.dot(self.matrix, 
                       np.array([[1.0,          0.0,           0.0,0.0],
                                [0.0,np.cos(theta),-np.sin(theta),0.0],
                                [0.0,np.sin(theta), np.cos(theta) ,0.0],
                                [0.0,            0.0,             0.0,1.0]]))
        self.inverse = np.dot(self.inverse,
                              np.array([[1.0,           0.0,             0.0,0.0],
                                [0.0,np.cos(theta),np.sin(theta)   ,0.0],
                                [0.0,-np.sin(theta), np.cos(theta) ,0.0],
                                [0.0,            0.0,           0.0,1.0]]))
        
    def rotateY(self, theta):
        '''
        Rotates an object theta degrees around the y-axis.
        '''
        theta = theta*(np.pi/180.0)
        self.matrix = np.dot(self.matrix,
                      np.array([[np.cos(theta),  0.0, np.sin(theta),0.0],
                                [           0.0, 1.0,             0.0,0.0],
                                [-np.sin(theta), 0.0, np.cos(theta),0.0],
                                [           0.0, 0.0,           0.0,1.0]]))
        self.inverse =  np.dot(self.inverse,
                        np.array([[ np.cos(theta), 0.0, -np.sin(theta),0.0],
                                [           0.0, 1.0,            0.0,0.0],
                                [np.sin(theta), 0.0, np.cos(theta),0.0],
                                [          0.0, 0.0,           0.0,1.0]]))
        
        
    def rotateZ(self, theta):
        '''
        Rotates an object theta degrees around the z-axis.
        '''
        theta = theta*(np.pi/180.0)
        self.matrix = np.dot(self.matrix,
                      np.array( [[np.cos(theta),  -np.sin(theta),0.0,0.0],
                                [np.sin(theta),   np.cos(theta),0.0,0.0],
                                [          0.0,           0.0,1.0,0.0],
                                [          0.0,           0.0,0.0,1.0]]))
        self.inverse =  np.dot(self.inverse,
                        np.array([[np.cos(theta),  np.sin(theta),0.0,0.0],
                                [-np.sin(theta), np.cos(theta),0.0,0.0],
                                [           0.0,           0.0,1.0,0.0],
                                [           0.0,           0.0,0.0,1.0]]))
    
    
        