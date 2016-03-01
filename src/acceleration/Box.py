'''
Created on Feb 24, 2016

@author: moritz
'''
from src.math import Constants
from src.math import Intersection

class Box(object):
    '''
    An axis aligned boundig box for speedup purposes.
    '''


    def __init__(self, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax):
        '''
        Set up the axis aligned bounding box.
        '''
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax
        self.Zmin = Zmin
        self.Zmax = Zmax
        
    def intersect(self,ray):
        ox = ray.getOrigin3()[0];    oy = ray.getOrigin3()[1];    oz = ray.getOrigin3()[2];
        dx = ray.getDirection3()[0]; dy = ray.getDirection3()[1]; dz = ray.getDirection3()[2];
        
        a = 1.0/dx
        if a >= 0:
            txMin = (self.Xmin - ox)*a
            txMax = (self.Xmax - ox)*a
        else:
            txMin = (self.xMax - ox)*a
            txMax = (self.xMin - ox)*a
            
        b = 1.0 / dy
        if b >= 0:
            tyMin = (self.Ymin - oy) * b
            tyMax = (self.Ymax - oy) * b
        else:
            tyMin = (self.Ymax - oy) * b
            tyMax = (self.Ymin - oy) * b

    
        c = 1.0 / dz;
        if c >= 0:
            tzMin = (self.Zmin - oz) * c
            tzMax = (self.Zmax - oz) * c
        else:
            tzMin = (self.Zmax - oz) * c
            tzMax = (self.Zmin - oz) * c

    
        #find largest entering t value
    
        if txMin > tyMin:
            t0 = txMin
        else:
            t0 = tyMin
        
        if tzMin > t0:
            t0 = tzMin
        
        # find smallest exiting t value
        
        if txMax < tyMax:
            t1 = txMax
        else:
            t1 = tyMax
        
        if tzMax < t1:
            t1 = tzMax
        
        if (t0 < t1) and (t1 > Constants.epsilon):
            return Intersection(True)
        else:
            return Intersection(False)

    
        