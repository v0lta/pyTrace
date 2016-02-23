import numpy as np
import matplotlib.pyplot as plt

#misc
from src.camera import PerspectiveCamera
from src.sampling import ImgSample

#math
from src.math import Point


class Renderer:
    def __init__(self,sens,gamma,world):
        
        # validate the input 
        if (world.width <= 0):
            raise NameError('Width must be positive.')
        if (world.height <= 0):
            raise NameError('Height must be positive.')
        if (gamma <= 0):
            raise NameError('Gamma must be positive.')
        if (sens <= 0):
            raise NameError('Sensitivity must be positive.')
                
        self.width       = world.width
        self.height      = world.height
        self.sensitivity = sens
        self.gamma       = gamma
        self.world       = world


    def main(self):    
        # parse command line arguments...(comes later)
    
            
        #create the image matrix
        img = np.zeros((self.width,self.height,3))
        
        for x in range(0,self.width):
            for y in range(0,self.height):
                sample = ImgSample(x,y)
                currentRay = self.world.camera.generateRay(sample)
                
                #Using exhaustive ray Tracing
                hit = False
                for currentShape in self.world.shapes:
                    if currentShape.intersect(currentRay) != False:
                        hit = True
                        
                if hit == True:
                    img[x,y,1] = 1
                
        imgplot = plt.imshow(img)
        #plt.show()
        plt.savefig("../../img.png")
        