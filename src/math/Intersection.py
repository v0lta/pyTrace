'''
Created on Feb 23, 2016

@author: moritz
'''

class Intersection(object):
    '''
    An itersection class which stores whether an intersection as occured, where it has occured and
    the normal at the intersection point.
    '''


    def __init__(self, hit, normal=None, point=None, color = None):
        '''
        The intersection constructor takes the bool has Int
        the intersection point and the normal at that point.
        '''
        self.hit  = hit
        if hit == True:
            self.normal = normal
            self.point = point
            self.color = color
