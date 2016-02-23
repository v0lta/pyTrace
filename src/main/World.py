'''
Created on Feb 23, 2016

@author: moritz
'''
from src.camera import PerspectiveCamera
from src.shape import Triangle
from src.shape import Sphere

from src.math import Transformation
from src.math import Point

class TriangleWorld(object):
    '''
    a World object with classes that form a scene.
    #TODO.
    '''
    def __init__(self,width,height):
        '''
        Set up a scene with a transformed triangle.
        '''
        
        self.width = width
        self.height = height
        
        #xResolution, yResolution, origin, lookAt, up, s, d
        self.camera = PerspectiveCamera(width, height, Point(0.0, 0.0, -5.0),
                                   Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        
        self.shapes = []; 
        # initialize the scene
        trans = Transformation()
        trans.rotateZ(180);
        trans.scale(0.6, 0.6, 1.0);
        trans.translation(.25,.25, 0.0)
        triangle = Triangle(Point(1.,0.,0.),Point(0.,1.,0.),Point(),trans)
        self.shapes.append(triangle)
        
           
        trans2 = Transformation(); 
        trans2.rotateZ(180);
        trans2.scale(0.6, 0.6, 1.0);
        trans2.translation(0.2, 0.2, 0.)
        triangle2 = Triangle(Point(1.,0.,0.),Point(0.,1.,0.),Point(), trans2)
        self.shapes.append(triangle2)
        

        
        
        
class SphereWorld:
    def __init__(self,width,height):
        '''
        Set up a scene with a transformed sphere.
        '''
        self.width  = width
        self.height = height
        
        self.camera = PerspectiveCamera(width, height, Point(0.0, 0.0, -3.0),
                                   Point(0.0, 0.0, 1.0), Point(0.0, 1.0, 0.0),
                                   1.0, 100.0)
        
        # initialize the scene
        self.shapes = [];    
    
        trans = Transformation(); 
        trans.scale(0.5, 0.5, 1.0)
        trans.rotateZ(180);
        trans.translation(-0.45, 0.2, 0.0)
        
        #sphere1 = Sphere(t1); shapes.append(sphere1)
        
        #t2 = Transformation(); t2.translation(0., -.1, .0)
        
        #t3 = Transformation(); t3.translation(0., 0., 0.)       
        sphere = Sphere(trans); 
        self.shapes.append(sphere)
           
        
        