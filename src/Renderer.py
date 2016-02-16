
# basic Python ray tracer by mortitz wolter.
# this file is the entry point of the ray tracing process.
# inspired by Nils Billen's java version.
import numpy as np
from src.camera.PerspectiveCamera import PerspectiveCamera
from src.math.Point import Point

print("Starting the ray-tracing process.")

class Renderer:
    width       = 640
    height      = 640
    sensitivity = 1.0
    gamma       = 2.2
    gui         = True

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
        camera = PerspectiveCamera(self.width, self.height, Point(0.0, 0.0, 0.0),
                                   Point(0.0, 0.0, 1.0), Point(0.0, 1.0, 0.0),
                                   np.array([0.0, 1.0, 0.0])  )
        
        # initialize the scene
        