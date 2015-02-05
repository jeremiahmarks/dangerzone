from mypy.clock import romans
import datetime
from fvh import MyTurtle
from time import sleep

"""
Sample input:

from mypy.clock import clockrings
a=clockrings.clockface()
a.maketurtles([40,30,20])
a.setuptheclock([150,300,400])
a.run()

To Do: 
  add arabic number support
  resolve spacing issues with ones and fiftys
      rewrote all roman numerals so that all units will now start in the
      top left hand corner, rather than the top right hand corner.
  resolve height issue with fives
      see resolution for spacing issue of ones and fiftys
  set 0 to twentyfour for hours and figure out something to do for minutes and seconds
  add support for partial unit completion and smooth out transition(perhaps sleep for 1/10 of a second rather than one second)
  build it into a square shape rather than a circle
  make numbers that actually signify the time stand out. 

"""
def convtoroman(data):
    """
    This module is designed to accept a numeral and then convert it to its 
    value in roman numerals. It should accept values between 1 and 3999
    """
    I=(1,'I')
    V=(5,'V')
    X=(10,'X')
    L=(50,'L')
    C=(100,'C')
    D=(500,'D')
    M=(1000,'M')
    
    allvals=[I,V,X,L,C,D,M]
    
    if data==0:
        data=1
        
    romanstring=''
    
    thousands=data/1000
    hundreds=(data/100)%10
    tens=(data/10)%10
    ones=data%10
    
 
    for m in range(thousands):
        romanstring=romanstring+M[1]

    if hundreds==4:
        romanstring=romanstring+"CD"
    elif hundreds==9:
        romanstring=romanstring+"CM"
    else:
        for d in range(hundreds/5):
            romanstring=romanstring+D[1]
        for c in range(hundreds%5):
            romanstring=romanstring+C[1]
    if tens==4:
        romanstring=romanstring+"XL"
    elif tens==9:
        romanstring=romanstring+"XC"
    else:
        for l in range(tens/5):
            romanstring=romanstring+L[1]
        for x in range(tens%5):
            romanstring=romanstring+X[1]
    
    if ones==4:
        romanstring=romanstring+"IV"
    elif ones==9:
        romanstring=romanstring+"IX"
    else:
        for v in range(ones/5):
            romanstring=romanstring+V[1]
        for i in range(ones%5):
            romanstring=romanstring+I[1]
    return romanstring

class timebox(object):

    def __init__(self, numbertodisplay, numbersize):
        self.number=numbertodisplay
        self.size=numbersize


class clockface(object):

    def __init__(self):
        self.starttime=datetime.datetime.now()
        
        self.hoursring=clockring('hour', self.starttime)
        self.minutesring=clockring('minute',self.starttime)
        self.secondsring=clockring('second',self.starttime)
        self.rings=[self.hoursring, self.minutesring, self.secondsring]
        
    def maketurtles(self, listofnumbers):
        ringsizes=zip(self.rings, listofnumbers) 
        for eachring in ringsizes:
            eachring[0].createnumbers(eachring[1])
    
    def setuptheclock(self, listofdiameters):
        clockdias=zip(self.rings, listofdiameters)
        for eachring in clockdias:
            eachring[0].createClock(eachring[1])
    
    def run(self):
        while True:
            newtime=datetime.datetime.now()
            for eachring in self.rings:
                eachring.update(newtime)
            #print newtime
            sleep(0.1)

class clockring(object):

    def __init__(self, unit, starttime):
        self.unit=unit
        self.starttime=starttime
        if self.unit=='hour':
            self.numberofunits=24
            self.current=self.starttime.hour
            self.percentpassed=self.starttime.minute/60.0
        elif self.unit=='minute':
            self.numberofunits=60
            self.current=self.starttime.minute
            self.percentpassed=self.starttime.second/60.0
        elif self.unit=='second':
            self.numberofunits=60
            self.current=self.starttime.second
            self.percentpassed=self.starttime.microsecond/1000000.0
            
        

    def createnumbers(self, size):
        self.size=size
        self.numbers=[]
        for eachnumber in range(self.numberofunits):
            #numbers.append(timebox(eachnumber, self.size))
            romannumbers=convtoroman(eachnumber)
            lm=MyTurtle()
            lm.tracer(False)
            pos=0
            lm.begin_poly()
            for letter in romannumbers:
                if letter=='I':
                    romans.one(startpos=(pos,0), lm=lm, cube=self.size)
                    pos=pos+(self.size/2.0)
                elif letter=='V':
                    romans.five(startpos=(pos,0), lm=lm, cube=self.size)
                    pos=pos+self.size
                elif letter=='X': 
                    romans.ten(startpos=(pos,0), lm=lm, cube=self.size)
                    pos=pos+self.size
                elif letter=='L':
                    romans.fifty(startpos=(pos,0), lm=lm, cube=self.size)
                    pos=pos+self.size/2.0              
                
            lm.end_poly()
            lm.tracer(False)
            lms=lm.getscreen()
            lms.addshape(self.unit+str(eachnumber), lm.get_poly())
            lm.shape(self.unit+str(eachnumber))
            lm.st()
            
            lm.clear()
            lm.pu()
            
            lm.seth(0)
#            lm.goto(self.size*len(romannumbers),25*len(self.unit))
            lm.getscreen().update()
            lm.settiltangle(90)
            self.numbers.append(lm)
        
    def createClock(self, diameter):
        self.diameter=diameter
        self.offset=360.0/self.numberofunits
        x=0
        for eachnumber in range(self.current, self.current+self.numberofunits):
            self.numbers[eachnumber%self.numberofunits].goto(0,0)
            self.numbers[eachnumber%self.numberofunits].seth(x*self.offset)
            self.numbers[eachnumber%self.numberofunits].fd(diameter)
            x+=1
        self.numbers[0].getscreen().update()
    
    def update(self,time):
        if self.unit=='hour':
            self.current=time.hour
            self.percentpassed=self.starttime.minute/60.0
        elif self.unit=='minute':

            self.current=time.minute
            self.percentpassed=self.starttime.second/60.0
        elif self.unit=='second':
            self.current=time.second
            self.percentpassed=self.starttime.microsecond/1000000.0
            #print self.percentpassed
        x=0
        for eachnumber in range(self.current, self.current+self.numberofunits):
            self.numbers[eachnumber%self.numberofunits].goto(0,0)
            self.numbers[eachnumber%self.numberofunits].seth((x*self.offset)+(self.offset*self.percentpassed))
            print self.unit + str((self.offset*self.percentpassed))
            self.numbers[eachnumber%self.numberofunits].fd(self.diameter)
            if x==0:
                self.numbers[eachnumber%self.numberofunits].color('red')
            else:
                self.numbers[eachnumber%self.numberofunits].color('black')
            x+=1
        self.numbers[0].getscreen().update()
