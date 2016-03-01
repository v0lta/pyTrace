'''
Created on Feb 23, 2016

@author: moritz
'''

from src.math import Point, Normal
from src.shape import Triangle

import pyximport; pyximport.install();
from src.shape.CTriangle import CTriangle


class ObjShape(object):
    '''
    This class reads in WaveFront (object Files)
    '''


    def __init__(self, path, color, reflectivity, transformation):
        '''
        Supply the path to the .obj file.
        '''
        self.path = path
        self.color = color
        self.reflectivity = reflectivity
        self.transformation = transformation
                
        self.vertices = []
        self.textCoords = []
        self.normals = []
        self.f = []
   
        #read in the file.
        self.read()
        
        #create a list of trindgles.
        self.triangleList = []
        for f in self.f:
            
            ptListA = self.vertices[f[0][0] - 1]
            a = Point(ptListA[0], ptListA[1], ptListA[2])
            
            ptListB = self.vertices[f[1][0] - 1]
            b = Point(ptListB[0], ptListB[1], ptListB[2])
            
            ptListC = self.vertices[f[2][0] - 1]
            c = Point(ptListC[0], ptListC[1], ptListC[2])
     
            normListA = self.normals[f[0][2] - 1]
            na = Normal(normListA[0], normListA[1], normListA[2])
            
            normListB = self.normals[f[1][2] - 1]
            nb = Normal(normListB[0], normListB[1], normListB[2])
            
            normListC = self.normals[f[2][2] - 1]
            nc = Normal(normListC[0], normListC[1], normListC[2])

            self.triangleList.append(Triangle(a,b,c, self.color, self.reflectivity, self.transformation,
                                     na, nb, nc))
            
   
    def read(self):     
        with open(self.path) as file:
            lines = file.readlines()
        
        for l in lines:
            if l[0:2] == "v ":
                self.vertices.append([float(x) for x in l[2:].split()])
            if l[0:2] == "vt":    
                self.textCoords.append([float(x) for x in l[2:].split()])
            if l[0:2] == "vn":
                self.normals.append([float(x) for x in l[2:].split()])
            if l[0:2] == "f ":
                tmp = l[2:].split() 
                f = [[],[],[]]
                for i in range(0,3):
                    f[i] = [int(x) for x in str(tmp[i]).split("/")]
                self.f.append(f)
                    
                #self.f.append([float(x) for x in l[2:].split("/")]) 
                
        if False:        
            print "v :" + str(self.vertices)
            print "vt:" + str(self.textCoords)
            print "vn:" + str(self.normals)
            print "f :" + str(self.f)
            print "--------------------------"