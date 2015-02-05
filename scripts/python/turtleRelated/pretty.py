

from turtle import Turtle

class MyTurtle(Turtle):
    """
    This function uses Turtle as a parent function and adds a 
    jump, gohome, and clean home method to the default methods. 
    
    Jump will retract the turtles pen, move it 'distance' 
    units in the direction it is facing, and then put its 
    pen back on the ground.
    
    gohome simply jumps the turtle home
    
    clean home jumps the turtle home and then cleans up its tracks
    
    """
    def jump(self, distance):
        self.pu()
        self.forward(distance)
        self.pd()

    def jumpto(self, point):
      self.pu()
      self.goto(point)
      self.pd()
        
    def gohome(self):
        self.pu()
        self.goto(0,0)
        self.pd()
        
    def cleanhome(self):
        self.gohome()
        self.clear()
        
def prettyDraw():
  leftpoints=((-75, 75), (-75, 0), (-75,-75))
  rightpoints=((75,75), (75, 60), (75,45), (75,30), (75,15), (75,0), (75,-15), (75, -30), (75, -45), (75,-60), (75, -75))
  
  mover=MyTurtle()
  mover.speed(0)
  ts=MyTurtle.getscreen(mover)
  ts.screensize(150,150)
  for leftpoint in leftpoints:
    
    for rightpoint in rightpoints:
      mover.jumpto(leftpoint)
      mover.goto(rightpoint)
  
def pdraw(numOfLPoints,numOfRPoints):
  
  mover=MyTurtle()
  mover.speed(0)
  ts=MyTurtle.getscreen(mover)
  ts.screensize(600,600)
  thesize=ts.screensize()
  vBars=thesize[0]/2
  hBars=thesize[1]/2
  leftstep=thesize[0]/numOfLPoints
  rightstep=thesize[1]/numOfRPoints
  for x in range(-vBars, vBars, leftstep):
    for y in range (-hBars, hBars, rightstep):
      #print str(-hBars)+ ","+str(y)+" TO: "+str(hBars)+","+str(x)
      mover.jumpto((-hBars,-x))
      mover.goto((hBars,y))
      
