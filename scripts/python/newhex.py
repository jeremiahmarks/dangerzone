from fvh import MyTurtle
masterHexSet=[]
masterHexList=[]
distanceBetweenLayers=None
points=["sw","se","e","ne","nw","w"]

def drawit(circleXfromCenter,rootHex):
    heading=90
    rootHex.turt.pu()
    rootHex.turt.seth(heading)
    rootHex.setDistanceBetweenLayers()
    rootHex.turt.fd(distanceBetweenLayers)
    newturt=Hex(rootHex.turt.pos(), rootHex.length)
    newturt.drawBlack()
    heading=heading-60
    for x in range(circleXfromCenter-1):
        rootHex.turt.seth(heading)
        rootHex.turt.fd(distanceBetweenLayers)
        newturt=Hex(rootHex.turt.pos(), rootHex.length)
        newturt.drawBlack()
    for x in range(5):
        heading=heading-60
        for y in range(circleXfromCenter):
            rootHex.turt.seth(heading)
            rootHex.turt.fd(distanceBetweenLayers)
            newturt=Hex(rootHex.turt.pos(), rootHex.length)
            newturt.drawBlack()

def drawsome(x):
    a=Hex((0,0),10)
    a.drawBlack()
    for circle in range(1,x):
        drawit(circle,a)
    counter=1
    for ahex in masterHexList:
        ahex.write(counter)
        counter+=1

def checkInMasterHexSet(point):
    tempx=round(point[0],-1)
    tempy=round(point[1],-1)
    temppos=(tempx,tempy)
    return temppos in masterHexSet

class Hex(object):

    def __init__(self, center, lengthperside):
        global masterHexSet
        global masterHexList
        
        self.center=center
        self.length=lengthperside
        tempx=round(center[0],-1)
        tempy=round(center[1],-1)
        temppos=(tempx,tempy)
        masterHexSet.append(temppos)
        masterHexList.append(self)
        self.turt=MyTurtle()
        self.turt.setup()
        self.turt.tracer(False)
        self.points={}
        
    def drawBlack(self):
        self.turt.pu()
        self.turt.pencolor('black')
        self.turt.goto(self.center)
        self.turt.seth(240)
        self.turt.fd(self.length)
        self.turt.seth(0)
        self.turt.pd()
        for eachpoint in points:
            self.points[eachpoint]=self.turt.pos()
            self.turt.fd(self.length)
            self.turt.lt(60)
        self.turt.pu()
        self.turt.goto(self.center)
        
    def drawRed(self):
        self.turt.pu()
        self.turt.pencolor('red')
        self.turt.goto(self.center)
        self.turt.seth(240)
        self.turt.fd(self.length)
        self.turt.seth(0)
        self.turt.pd()
        for eachpoint in points:
            self.points[eachpoint]=self.turt.pos()
            self.turt.fd(self.length)
            self.turt.lt(60)
        self.turt.pu()
        self.turt.goto(self.center)
    
    def setDistanceBetweenLayers(self):
        global distanceBetweenLayers
        distanceBetweenLayers=self.points['ne'][1]-self.points['se'][1]
    
    def createLayers(self,numberOfLayers):
        if not distanceBetweenLayers:
            self.setDistanceBetweenLayers()
        for x in range(1,numberOfLayers+1):
            for y in range(6):
                self.turt.pu()
                self.turt.goto(self.center)    
                self.turt.seth(90-(y*60))
                self.turt.fd(x*distanceBetweenLayers)
                if not checkInMasterHexSet(self.turt.pos()):
                    tempHex=Hex(self.turt.pos(), self.length)
                    tempHex.drawBlack()
                    if (numberOfLayers-x>=1):
                        tempHex.createLayers(numberOfLayers-x)
    
    def colorBlack(self):
        self.turt.fillcolor('black')
        self.turt.fill(True)
        self.drawBlack()
        self.turt.fill(False)
        if self.something:
            self.turt.pencolor('white')
            self.turt.write(self.something)
            self.turt.pencolor('black')
    
    def colorWhite(self):
        self.turt.fillcolor('white')
        self.turt.fill(True)
        self.drawBlack()
        self.turt.fill(False)
        if self.something:
            self.turt.pencolor('black')
            self.turt.write(self.something)

    
        
    def write(self,something):
        self.something=something
        self.turt.goto(self.center)
        self.turt.write(something)
        
