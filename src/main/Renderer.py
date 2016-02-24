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
        #create and render image matrix
        img = rendPart([self,0,self.width,0,self.height])

                
        imgplot = plt.imshow(img)
        plt.gca().invert_yaxis()
        #plt.show()
        plt.savefig("../../img.png")
        print "rend.main done"
        
        
    def multiRend(self):
        processNo = 4;
        p = Pool(processNo)    
        img = np.ones((self.width,self.height,3))
        
        width = self.world.width 
        height = self.world.height
        
        
        #top left				    #top right		
        xStart3 = 0;				xStart4 = width/2;
        xEnd3   = width/2;			xEnd4   = width;
        yStart3 = height/2;			yStart4 = height/2;
        yEnd3   = height;			yEnd4   = height;
        
        #bottom left				#bottom right
        xStart = 0;					xStart2 = width/2;
        xEnd   = width/2;			xEnd2   = width;
        yStart = 0;					yStart2 = 0;
        yEnd   = height/2;			yEnd2   = height/2;
        
        
        
        #res = [[],[],[],[]]
        #res[0] = rendPart([self,xStart,  xEnd,  yStart,  yEnd])
        #res[1] = rendPart([self,  xStart2, xEnd2, yStart2, yEnd2])
        #res[2] = rendPart([self,  xStart3, xEnd3, yStart3, yEnd3])
        #res[3] = rendPart([self,  xStart4, xEnd4, yStart4, yEnd4])
        
        res = p.map( rendPart, [[self, xStart,  xEnd,  yStart,  yEnd],
                               [self,  xStart2, xEnd2, yStart2, yEnd2],
                               [self,  xStart3, xEnd3, yStart3, yEnd3],
                               [self,  xStart4, xEnd4, yStart4, yEnd4]])
            
        img[xStart:xEnd,yStart:yEnd,:] = res[0]
        img[xStart2:xEnd2,yStart2:yEnd2,:] = res[1]
        img[xStart3:xEnd3,yStart3:yEnd3,:] = res[2]
        img[xStart4:xEnd4,yStart4:yEnd4,:] = res[3]

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
    	
    	if i%10 == 0:
    	 	print  float(i)/(xEnd - xStart) * 100.0
                
        for j in range(0,yEnd-yStart):
            x = xStart + i
            y = yStart + j
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
                img[i,j,:] = La*Cs*Rs
                
                #add a contribution for each light.
                for pl in self.world.pointLightLst:
                    Lp = pl.L()
                    Cp = pl.color.getColor()
                    l  = pl.l(intersection.point)
                    n  = intersection.normal.getArray3()
                    img[i,j,:] = img[i,j,:] + (Rs/3.14 * Cs* Lp* Cp * np.dot(l,n ))

                     
                #Fix overflow...
                for k in range(0,2):
             	   if img[i,j,k] > 1.0:
                   		#img[x,y,:] = img[x,y,:]/img[x,y,i]
                   		#img[x,y,:] = img[x,y,:]/5.0; 
                   		img[x,y,:] = [1.,0.,0.]
                  
    return img