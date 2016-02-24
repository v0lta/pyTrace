'''
Created on Feb 23, 2016

@author: moritz
'''
from src.camera import PerspectiveCamera
from src.lights import PointLight

from src.shape import Triangle
from src.shape import Sphere
from src.shape import ObjShape

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
        self.camera = PerspectiveCamera(width, height, Point(5.0, 5.0, -5.0),
                                   Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        
        #set up a point light (position, shadows, color, ls)
        self.pointLight = PointLight(Point(0.0, 0.0, -4.0), False, Color(.8,.8,.8), 2.)
        
        self.shapes = []; 
        
        trans3 = Transformation();
        obj = ObjShape("../../obj/cube.obj",Color(0.0,0.6,0.0), 0.8, trans3)
        self.shapes = obj.triangleList + self.shapes

        
        
        
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
        sphere = Sphere(Color(0.,0.6,0.), 0.9, trans ); #red sphere at the origin.
        self.shapes.append(sphere)
        
        trans = Transformation(); 
        trans.translation(-0.25, 0.1, 0.)
        trans.scale(0.75, 0.75, 0.75)                       
        sphere = Sphere(Color(0.,0.6,0.6), 0.9, trans ); #red sphere at the origin.
        self.shapes.append(sphere)
        
        
        

    
           
        
        