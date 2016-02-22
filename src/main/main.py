'''
Created on Feb 18, 2016

@author: moritz
'''

import subprocess
from src.main import Renderer

print("Starting the ray-tracing process.")
rend1 = Renderer()
rend1.main()
#subprocess.call("eog /home/moritz/workspace/pyTrace/img.png", shell=True)
print("Done.")

