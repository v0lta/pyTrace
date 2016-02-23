'''
Created on Feb 23, 2016

@author: moritz
'''
from src.camera import PerspectiveCamera
from src.lights import PointLight
from src.shape import Triangle
from src.shape import Sphere

from src.math import Transformation
from src.math import Point
from src.math import Color

class TriangleWorld(object):
    '''
    a World object with classes that form a scene.
    #TODO.
    '''
    def __init__(self,width,height,ambient):
        '''
        Set up a scene with a transformed triangle.
        '''
        
        self.width = width
        self.height = height
        self.ambient = ambient
        
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
    def __init__(self,width,height,ambient):
        '''
        Set up a scene with a transformed sphere.
        '''
        self.width  = width
        self.height = height
        self.ambient = ambient
        
        #xResolution, yResolution, origin, lookAt, up, s, d
        self.camera = PerspectiveCamera(width, height, Point(0.0, 0.0, -5.0),
                                   Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        
        #set up a point light (position, shadows, color, ls)
        self.pointLight = PointLight(Point(2.0, 2.0, -4.0), False, Color(.8,.8,.8), 4.)
        
        # initialize the scene
        self.shapes = [];    
        trans = Transformation(); 
        trans.translation(0.2, 0., 0.)
        trans.scale(0.75, 0.75, 0.75)                       
        sphere = Sphere(trans, Color(0.,0.6,0.), 0.9 ); #red sphere at the origin.
        self.shapes.append(sphere)
        
        trans = Transformation(); 
        trans.translation(-0.25, 0.1, 0.)
        trans.scale(0.75, 0.75, 0.75)                       
        sphere = Sphere(trans, Color(0.,0.6,0.6), 0.9 ); #red sphere at the origin.
        self.shapes.append(sphere)
        
        
        

    
           
        
        