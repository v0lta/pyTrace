
# basic Python ray tracer by mortitz wolter.
# this file is the entry point of the ray tracing process.
# inspired by Nils Billen's java version.
import numpy as np
import matplotlib.pyplot as plt

from src.camera.SimpleCamera import SimpleCamera
from src.camera.PerspectiveCamera import PerspectiveCamera

from src.math.Transformation import Transformation
from src.math.Point import Point
from src.shape.Sphere import Sphere
from src.sampling.ImgSample import ImgSample


class Renderer:
    def __init__(self):
        self.width       = 320
        self.height      = 320
        self.sensitivity = 1.0
        self.gamma       = 2.2
        self.gui         = False

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
        camera = SimpleCamera(self.width, self.height, Point(0.0, 0.0, 0.0),
                                   Point(0.0, 0.0, 1.0),0.05)
        
        #camera = PerspectiveCamera(self.width, self.height, Point(0.0, 0.0, 0.0),
        #                           Point(0.0, 0.0, 1.0), Point(0.0, 1.0, 0.0),
        #                           np.array([0.0, 1.0, 0.0])  )
        
        # initialize the scene
        t1 = Transformation()
        shapes = [];
        sphere1 = Sphere(t1); shapes.append(sphere1)
        
        #create the image matrix
        img = np.zeros((self.width,self.height,3))
        
        for x in range(0,self.width-1):
            for y in range(0,self.height-1):
                sample = ImgSample(x,y,)
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
        