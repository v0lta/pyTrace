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
import time

import profile




print("Starting the ray-tracing process.")
# (self,world,width,height,sens,gamma):

#spWorld = SphereWorld(300,300,1.0)
trWorld = TriangleWorld(100,100,0.4)
print("world created.")
rend1 = Renderer(1.0,1.0,trWorld)

#profiling
if False:
    t = time.time()
    profile.run('rend1.main()')
    print time.time() - t

#use the single process implementation
if False:
    t = time.time()
    rend1.main()
    print time.time() - t

#use the multiprocess implementation
if True:
    t = time.time()
    rend1.multiRend()
    print time.time() - t

#subprocess.call("eog /home/moritz/workspace/pyTrace/img.png", shell=True)
print("Done.")

