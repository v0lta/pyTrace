'''
Created on Feb 23, 2016

@author: moritz
'''

class ObjShape(object):
    '''
    This class reads in WaveFront (object Files)
    '''


    def __init__(self, path):
        '''
        Supply the path to the .obj file.
        '''
        self.path = "./obj/plane.obj"
        #read in the file
        
        self.vertices = []
        self.textCoords = []
        self.normals = []
        self.f = []
   
        #read in the file.
        self.read()
        
        #create a list of trinagles.
        self.triangelList = []
   
   
   
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