from fvh import MyTurtle
from turtle import Vec2D
import math

class particle(object):

    def __init__(self, xpos, ypos, mass):
        self.mass=mass
        self.position=(xpos,ypos)
        self.turt=MyTurtle()
        self.turt.pu()
        self.turt.goto(self.position)
        self.position=self.turt.pos()
        
    def nextStep(self, allParticles):
        self.nextPos=self.turt.pos()
        for part in allParticles:
            self.nextPos=(self.nextPos+part.turt.pos())*0.5
            
    def gotonext(self):
        self.turt.pd()
        self.turt.seth(self.turt.towards(self.nextPos))
        self.turt.fd(self.mass)
    
    def getMasses(self,allParticles):
        newlist=[]
        for part in allParticles:
            if self.turt.pos()==part.turt.pos():
                self.mass=self.mass+part.mass
                part.mass=0
                
    def positiona(self,timet):
        x=100*math.sin(timet)
        y=150*math.cos(timet)
        self.turt.goto(x,y)
        self.turt.pd()
        
    
