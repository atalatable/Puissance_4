import math

class Piece:
    def __init__(self, height, dt, E=0.7):
        self.G = 9.81
        self.E =  E
        self.K = math.sqrt(2*height/self.G)
        self.V = [math.sqrt(2*self.G*height)]
        self.H = [height]
        self.TM = [self.K]
        self.S = 2*self.K
        self.height = height
        self.bounce = 0
        self.dt = dt
        self.t = 0
        self.T = 0

        for i in range(1, 20):
            self.S *= self.E
            self.V.append(self.E*self.V[i-1])
            self.H.append(self.E*self.E*self.H[i-1])
            self.TM.append(self.TM[i-1]+self.S)

    def calc(self):
        if self.bounce == 0: self.y = self.height-0.5*self.G*self.t*self.t
        else: self.y = self.V[self.bounce]*self.t-0.5*self.G*self.t*self.t
        if self.y < 0:
            self.t -= self.dt
            self.T -= self.dt
            tau=self.TM[self.bounce]-self.T
            self.t += tau
            self.T += tau
            if self.bounce == 0: self.y = self.height-0.5*self.G*self.t*self.t
            else: self.y = self.V[self.bounce]*self.t-0.5*self.G*self.t*self.t
            self.y = 0
            self.bounce += 1
            self.t = 0
        self.t+=self.dt
        self.T+=self.dt
    
    def setHeight(self, height): 
        self.height = height
    
    def isMoving(self):
       return False if self.H[self.bounce]<0.005 else True