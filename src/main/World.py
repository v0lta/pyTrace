'''
Created on Feb 23, 2016

@author: moritz
'''
from src.camera import PerspectiveCamera
from src.lights import PointLight

from src.shape import Triangle, Sphere, ObjShape, Plane
from src.material import Chess

from src.math import Transformation
from src.math import Point
from src.math import Color
from src.math.Normal import Normal

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
        
        #set up the camera (xResolution, yResolution, origin, lookAt, up, s, d)
        self.camera = PerspectiveCamera(width, height, Point(-4.0, 4.0, -5.0),
                                   Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        #self.camera = PerspectiveCamera(width, height, Point(-8.0, 8.0, -6.0), #table camera
        #                           Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
        #                           1.0/width, 1.0)
        
        
        #set up the lights (position, shadows, color, ls)
        self.pointLightLst = []
        pointLight1 = PointLight(Point(0.0, 4.0, -0.5), False, Color(.8,.0,.0), 4.)
        pointLight2 = PointLight(Point(-4.0, 0.0, -0.5), False, Color(.0,.8,.8), 4.)
        self.pointLightLst.append(pointLight1)
        self.pointLightLst.append(pointLight2)
        
        # initialize the scene
        self.shapes = [];    
        #background plane
        chessPattern = Chess(Color(0.1,0.1,0.1),Color(0.3,0.3,0.3),0.5)
        p1 = Plane(Point(0.0,0.0,0.0),Normal(0.0,0.0,-1.0), chessPattern, 0.9)
        self.shapes.append(p1)
        
        
        trans3 = Transformation();
        #trans3.rotateX(-85) #table rotation
        obj = ObjShape("../../obj/cube.obj",Color(0.5,0.6,0.5), 0.8, trans3)
        self.shapes = self.shapes + obj.triangleList 
        #"../../obj/cube.obj"
        
        
        
class SphereWorld:
    def __init__(self,width,height,ambient):
        '''
        Set up a scene with a transformed sphere.
        '''
        self.width  = width
        self.height = height
        self.ambient = ambient
        
        #xResolution, yResolution, origin, lookAt, up, s, d
        self.camera = PerspectiveCamera(width, height, Point(-2.0, 0.0, -5.0),
                                   Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        
        #set up the lights (position, shadows, color, ls)
        self.pointLightLst = []
        pointLight1 = PointLight(Point(0.0, 4.0, -0.5), False, Color(.8,.8,.8), 4.)
        self.pointLightLst.append(pointLight1)
        
        
        # initialize the scene
        self.shapes = [];    
        #background plane
        chessPattern = Chess(Color(0.1,0.1,0.1),Color(0.3,0.3,0.3),0.5)
        p1 = Plane(Point(0.0,0.0,5.0),Normal(0.0,0.0,-1.0), chessPattern, 0.9)
        self.shapes.append(p1)
        
        #sphere 1
        trans = Transformation(); 
        trans.translation(0.2, 0., 0.)
        trans.scale(0.75, 0.75, 0.75)                       
        sphere = Sphere(Color(0.,0.6,0.), 0.9, trans ); #red sphere at the origin.
        self.shapes.append(sphere)
        
        #sphere 2
        trans = Transformation(); 
        trans.translation(-0.3, 0.1, 0.)
        trans.scale(0.75, 0.75, 0.75)                       
        sphere = Sphere(Color(0.,0.6,0.6), 0.9, trans ); #red sphere at the origin.
        self.shapes.append(sphere)
             
        
class TestWorld:
    def __init__(self,width,height,ambient):
        '''
        Set up a scene with a transformed sphere.
        '''
        self.width  = width
        self.height = height
        self.ambient = ambient
        
        #xResolution, yResolution, origin, lookAt, up, s, d
        self.camera = PerspectiveCamera(width, height, Point(0.0, 0.0, 0.0),
                                   Point(0.0, 0.0, 10.0), Point(0.0, 1.0, 0.0),
                                   1.0/width, 1.0)
        
        #set up the lights (position, shadows, color, ls)
        self.pointLightLst = []
        pointLight1 = PointLight(Point(1.0, 1.0, 0.5), False, Color(.8,.8,.8), 4.)
        self.pointLightLst.append(pointLight1)
        
        
        # initialize the scene
        self.shapes = [];    
        #background plane
        #chessPattern = Chess(Color(0.1,0.1,0.1),Color(0.3,0.3,0.3),0.5)
        #p1 = Plane(Point(0.0,0.0,20.0),Normal(0.0,0.0,-1.0), chessPattern, 0.9)
        #self.shapes.append(p1)
        
        trans = Transformation()
        obj = ObjShape("../../obj/torus.obj",Color(0.5,0.6,0.5), 0.8, trans)
        self.shapes = self.shapes + obj.triangleList 
        
        
        
        
        

    
           
        
        