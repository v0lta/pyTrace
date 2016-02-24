import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool


#misc
from src.sampling import ImgSample

#math
from src.math import Intersection
from src.math import Normal


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
        #create the image matrix
        img = np.zeros((self.width,self.height,3))
        
        
        for x in range(0,self.width):
            print float(x)/self.width
            for y in range(0,self.height):
                sample = ImgSample(x,y)
                currentRay = self.world.camera.generateRay(sample)
                
                #Using exhaustive ray Tracing
                intersectionLst = [];
   
                for currentShape in self.world.shapes:
                    
                    intersection = currentShape.intersect(currentRay)
                    if intersection.hit == True:
                        intersectionLst.append(intersection)
                
                if intersectionLst:       
                    #Find the intersection closest to the camera. (There can only be one camera.)
                    dists = []
                    for currentIntersetion in intersectionLst:
                        camPos = self.world.camera.origin.getArray3()
                        intPos = currentIntersetion.point.getArray3()
                        dist = np.linalg.norm(camPos - intPos) 
                        dists.append(dist)
                    index = dists.index(min(dists))
                    intersection = intersectionLst[index]
                           
                    #use the found intersection for rendering.
                    La = self.world.ambient
                    Rs = currentShape.reflectivity
                    Cs = intersection.color.getColor()
                    img[x,y,:] = La*Cs*Rs
                    
                    #add a contribution for each light.
                    for pl in self.world.pointLightLst:
                        Lp = pl.L()
                        Cp = pl.color.getColor()
                        l  = pl.l(intersection.point)
                        n  = intersection.normal.getArray3()
                        img[x,y,:] = img[x,y,:] + (Rs/3.14 * Cs* Lp* Cp * np.dot(l,n ))

                        
                    #Fix overflow...
                    for i in range(0,2):
                        if img[x,y,i] > 1.0:
                            #img[x,y,:] = img[x,y,:]/img[x,y,i]
                            #img[x,y,:] = img[x,y,:]/5.0; 
                            img[x,y,:] = [1.,0.,0.]

        
                
        imgplot = plt.imshow(img)
        plt.gca().invert_yaxis()
        #plt.show()
        plt.savefig("../../img.png")
        print "rend.main done"
        
        
        
    def multiRend(self):
        processNo = 4;
        p = Pool(processNo)    
        img = np.ones((self.width,self.height,3))
        
        for y in range(0,self.height):
            
            #give lines to each process.
            xStart = 0
            xEnd   = self.width
            yStart = y
            yEnd   = y+1
            yStart2 = yEnd
            yEnd2   = y+2
            yStart3 = yEnd2
            yEnd3 = y+3
            yStart4 = yEnd3
            yEnd4 = y+4
            
            res = p.map( rendPart, [[self, xStart, xEnd, yStart,  yEnd],
                                    [self, xStart, xEnd, yStart2, yEnd2],
                                    [self, xStart, xEnd, yStart3, yEnd3],
                                    [self, xStart, xEnd, yStart4, yEnd4]])
            
            img[xStart:xEnd,yStart:yEnd,:] = res[0]
            img[xStart:xEnd,yStart2:yEnd2,:] = res[1]
            img[xStart:xEnd,yStart3:yEnd3,:] = res[2]
            img[xStart:xEnd,yStart4:yEnd4,:] = res[3]
            print float(y)/self.height
            
        
            
        #xStart = 0
        #yStart = 0
        #xEnd = self.width
        #yEnd = self.height                
        #img[xStart:xEnd,yStart:yEnd,:] = rendPart([self,xStart,xEnd,yStart,yEnd])    
        

        
        imgplot = plt.imshow(img)
        plt.gca().invert_yaxis()
        #plt.show()
        plt.savefig("../../img2.png")
        print "rend.multiRand done"
        
   
def rendPart(args):
    self = args[0]
    xStart = args[1]
    xEnd = args[2]
    yStart = args[3] 
    yEnd  = args[4]
    img = np.zeros((xEnd-xStart,yEnd-yStart,3))
        
    for i in range(0,xEnd-xStart):
        for j in range(0,yEnd-yStart):
            x = xStart + i
            y = yStart + j
            sample = ImgSample(x,y)
            currentRay = self.world.camera.generateRay(sample)
                
            #Using exhaustive ray Tracing
            for currentShape in self.world.shapes:
                    intersection = currentShape.intersect(currentRay)
                    if intersection.hit == True:
                        img[i,j,:] = (self.world.ambient*currentShape.color.getColor()*currentShape.reflectivity +
                                     (currentShape.reflectivity/3.14 * currentShape.color.getColor()* 
                                      self.world.pointLight.L()* self.world.pointLight.color.getColor() * 
                                      np.dot(self.world.pointLight.l(intersection.point),
                                              intersection.normal.getArray3() )))

                        
                        #Fix overflow...
                        for k in range(0,2):
                            if img[i,j,k] > 1.0:
                                #img[x,y,:] = img[x,y,:]/img[x,y,i]
                                #img[x,y,:] = img[x,y,:]/5.0; 
                                img[i,j,:] = [1.,0.,0.]
                                
    return img