import numpy as np
import matplotlib.pyplot as plt

from src.camera import OrthographicCamera
from src.camera import PerspectiveCamera

from src.math import Transformation
from src.math import Point
from src.math import Normal
from src.shape import Sphere
from src.shape import SimpleSphere
#from src.shape import SimplePlane
from src.sampling import ImgSample


class Renderer:
    def __init__(self):
        self.width       = 300
        self.height      = 300
        self.sensitivity = 1.0
        self.gamma       = 2.2


    def main(self):    
        # parse command line arguments...(comes later)
    
        # validate the input 
        if (self.width <= 0):
            raise NameError('Width must be positive.')
        if (self.height <= 0):
            raise NameError('Height must be positive.')
        if (self.gamma <= 0):
            raise NameError('Gamma must be positive.')
        if (self.sensitivity <= 0):
            raise NameError('Sensitivity must be positive.')
        
        # initialize the camera.
        #  xResolution, yResolution, origin, lookat,s
        #camera = OrthographicCamera(self.width, self.height, Point(0.0, 0.0, -1.0),
        #                           Point(0.0, 0.0, 1.0),0.1)
        
        
        #xResolution, yResolution, origin, lookAt, up, s, d
        camera = PerspectiveCamera(self.width, self.height, Point(0.0, 2.0, -1.0),
                                   Point(0.0, 0.0, -1.0), Point(0.0, 1.0, 0.0),
                                   2.0, 0.5)
        
        # initialize the scene
        shapes = [];
         
        #t1 = Transformation(); t1.scale(1.0, 1.0, 1.0)
        #sphere1 = Sphere(t1); shapes.append(sphere1)
        
        t2 = Transformation(); t2.translation(0.0, 2.0, 0.0)
        sphere2 = Sphere(t2); shapes.append(sphere2)
        
        #sphere3 = SimpleSphere(Point(0.0,0.0,0.0),1.0); shapes.append(sphere3)
        #sphere4 = SimpleSphere(Point(0.0,1.0,0.0),1.0); shapes.append(sphere4)
               
        #create the image matrix
        img = np.zeros((self.width,self.height,3))
        
        for x in range(0,self.width):
            for y in range(0,self.height):
                sample = ImgSample(x,y)
                currentRay = camera.generateRay(sample)
                
                #Using exhaustive ray Tracing
                hit = False
                for currentShape in shapes:
                    if currentShape.intersect(currentRay) != False:
                        hit = True
                        
                if hit == True:
                    img[x,y,1] = 1
                
        imgplot = plt.imshow(img)
        #plt.show()
        plt.savefig("../../img.png")
        