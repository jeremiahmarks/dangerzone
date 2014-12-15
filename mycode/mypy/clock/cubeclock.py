from mypy.clock import arabic
import datetime
from fvh import MyTurtle
from time import sleep

class timebox(object):
    """
    The time box is used to house a numerical representation of an element of the time
    It will also provide an easy to reference indication of how much space the 
    digits will need in order to be displayed properly, and, should the need
    arise, provide a way to keep two seperate turtle objects evenly spaced
    """
    def __init__(self, numbertodisplay, numbersize):
        self.number=numbertodisplay
        self.size=float(numbersize)
        
        lm=MyTurtle()
        lm.tracer(False)
        pos=0.0
        #on size: for a '1', the height=numbersize, width=numbersize/8
        #         for everything else: h=numbersize, w=numbersize/2
        
        lm.begin_poly()
        for digit in self.number:
            if digit=='0':
                arabic.zero(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='1':
                arabic.one(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/8.0)
            elif digit=='2':
                arabic.two(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='3':
                arabic.three(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='4':
                arabic.four(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='5':
                arabic.five(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='6':
                arabic.six(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='7':
                arabic.seven(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='8':
                arabic.eight(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            elif digit=='9':
                arabic.nine(startpos=(pos,0), lm=lm, height=self.size)
                pos=pos+(self.size/2.0)
            pos=pos+(self.size/5.0)
        lm.end_poly()
        
        lms=lm.getscreen()
        lms.addshape(str(self.size)+self.number, lm.get_poly())
        lm.shape(str(self.size)+self.number)
        lm.st()
        
        self.lm=lm
        self.width=pos
        
        #return lm

class clockface(object):

    def __init__(self):
        self.starttime=datetime.datetime.now()
        self.hourcube=clockcube('hour', self.starttime)
        self.minutecube=clockcube('minute', self.starttime)
        self.secondcube=clockcube('second', self.starttime)
        
        self.cubes=[self.hourcube, self.minutecube, self.secondcube]
        
    def createNumbers(self,listOfSizes):
        """
        This method accepts a list of sizes and then creates the cubes for each
        unit at the desired size
        """
        numbersizes=zip(self.cubes, listOfSizes)
        
        for cube in numbersizes:
            cube[0].createnumbercubes(cube[1])
    
        
class clockcube(object):

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
            
    def createnumbercubes(self,size):
        self.size=size
        self.numbers=[]
        self.widest=0
        
        for eachnumber in range(self.numberofunits):
            abox=timebox('%02d' % eachnumber, self.size)
            if abox.width>self.widest: self.widest=abox.width
            self.numbers.append(abox)
    
    def arrangetocube(self):
        self.numbersinhor=(len(self.numbers)-1)/3
        self.numbersinvert=(len(self.numbers)-1)-(2*self.numbersinhor)
        self.boxwidth=self.numbersinhor*self.widest
        self.boxheight=self.numbersinvert*self.size
        self.innerbox=[(self.boxwidth/2.0, self.boxheight/2.0), (-self.boxwidth/2.0, self.boxheight/2.0),(-self.boxwidth/2.0, -self.boxheight/2.0),(self.boxwidth/2.0, -self.boxheight/2.0)]
        nexposition=[self.innerbox[0][0]-self.widest, self.innerbox[0][1]]
        for value in range(self.current+1, self.current+self.numberofunits):
            if (nexposition[0]>=(-self.boxwidth/2.0) and nexposition[1]==self.innerbox[0][1]):
                self.numbers[value%self.numberofunits].lm.goto(nexposition[0],nexposition[1])
                if ((nexposition[0]-self.widest)>-self.boxwidth/2.0):
                    nexposition[0]=nexposition[0]-self.widest
                else:
                    nexposition[0]=nexposition[0]-self.widest
                    nexposition[1]=nexposition[1]-self.size
            elif nexposition[1]>-self.boxheight/2.0:
                self.numbers[value%self.numberofunits].lm.goto(nexposition[0],nexposition[1])
                
                if ((nexposition[1]-self.size)>(-self.boxheight/2.0)):
                    nexposition[1]=nexposition[1]-self.size
                else:
                    nexposition[1]=nexposition[1]-self.size
                    nexposition[0]=nexposition[0]+self.widest
            else:
                self.numbers[value%self.numberofunits].lm.goto(nexposition[0],nexposition[1])
                nexposition[0]=nexposition[0]+self.widest
        
        
