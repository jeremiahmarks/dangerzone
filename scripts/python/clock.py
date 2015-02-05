from fvh import MyTurtle, allcolors, random, datetime
from fvh2 import circlearound, savetocircles



HOURS=24
MINUTES=60
SECONDS=60

class Clock(object):

    def __init__(self):
        self.seconds()
        self.sc.shape('seconds')
        for x in range (2000):
            self.sc.seth(x%360)

    
    def seconds(self):
        self.secondsCenter=(-100,0)
        self.secondsCircle=MyTurtle()
        self.sc=self.secondsCircle
        self.sc.goto(self.secondsCenter)
        self.sc.begin_poly()
        circlearound(self.secondsCenter, 100, self.sc)
        circlearound(self.secondsCenter, 80, self.sc)
        for x in range(SECONDS):
            self.sc.pu()
            self.sc.goto(self.secondsCenter)
            self.sc.seth(270+ (x*(360/SECONDS)))
            self.sc.fd(90)
            self.sc.write(x)
        self.sc.end_poly()
        self.sc.register_shape('seconds', self.sc.get_poly())
        
        
    
