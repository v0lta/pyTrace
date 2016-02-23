'''
Created on Feb 18, 2016

@author: moritz
'''

# basic Python ray tracer by mortitz wolter.
# this file is the entry point of the ray tracing process.

#import subprocess
from src.main import Renderer
from World import TriangleWorld
from World import SphereWorld

print("Starting the ray-tracing process.")
# (self,world,width,height,sens,gamma):

spWorld = SphereWorld(200,200)
trWorld = TriangleWorld(250,250)
rend1 = Renderer(1.0,1.0,trWorld)

rend1.main()
#subprocess.call("eog /home/moritz/workspace/pyTrace/img.png", shell=True)
print("Done.")

