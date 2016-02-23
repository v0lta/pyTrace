'''
Created on Feb 23, 2016

@author: moritz
'''

class Intersection(object):
    '''
    An itersection class which stores whether an intersection as occured, where it has occured and
    the normal at the intersection point.
    '''


    def __init__(self, hit, normal=None, point=None):
        '''
        The intersection constructor takes the bool has Int
        the intersection point and the normal at that point.
        '''
        self.hit  = hit
        if normal != None:
            self.normal = normal
            if point != None:
                self.point = point
            else:
                raise ValueError, "Forgot to specify the hit point"
        