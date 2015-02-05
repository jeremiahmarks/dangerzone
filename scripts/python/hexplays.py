from fvh import MyTurtle
masterHexSet=[]
masterHexList=[]
distanceBetweenLayers=None

class Hex(object):
    def __init__(self,center,lengthPerSide):
        global masterHexSet
        global masterHexList
        tempcenter=(int(center[0]),int(center[1]))
        masterHexSet.append(tempcenter)
        self.center=center
        self.length=lengthPerSide
        self.turt=None
        masterHexList.append(self)

    def drawhex(self):
        self.points=[]
        if not self.turt:
            self.turt=MyTurtle()
            self.turt.setup()
        self.turt.pu()
        self.turt.goto(self.center)
        self.turt.seth(240)
        self.turt.fd(self.length)
        self.turt.seth(0)
        self.turt.pd()
        for x in range(6):
            self.turt.fd(self.length)
            self.turt.left(60)
            self.points.append(self.turt.pos())

    def findCenter(self):
        self.smallestx, self.smallesty=self.points[0][0],self.points[0][1]
        self.largestx, self.largesty = self.points[0][0],self.points[0][1]
        for point in self.points:
            if point[0]<self.smallestx:
                self.smallestx=point[0]
            if point[0]>self.largestx:
                self.largestx=point[0]
            if point[1]<self.smallesty:
                self.smallesty=point[1]
            if point[1]>self.largesty:
                self.largesty=point[1]
        self.center=((self.smallestx+self.largestx)/2, (self.largesty+self.smallesty)/2)
        self.turt.pu()
        self.turt.goto(self.center)
        self.turt.dot()
        
    def setDistanceBetweenLayers(self):
        global distanceBetweenLayers
        if self.center==(0,0):
            self.drawhex()
            self.findCenter()
            distanceBetweenLayers=2*self.largesty
    
    def createSurrounding(self,layers):
#        print "I am supposed to create: "+str(layers)
        if not distanceBetweenLayers:
            temp=Hex((0,0), self.length)
            temp.setDistanceBetweenLayers
        for x in range (6):
            distance=distanceBetweenLayers
            self.turt.pu()
            self.turt.goto(self.center)
            layer=1
            while(layer<layers):
                self.turt.goto(self.center)
                self.turt.seth(30+(x*60))
                self.turt.fd(distance)
                temppoint=(int(self.turt.pos()[0]),int(self.turt.pos()[1])) 
                if temppoint not in masterHexSet:
                    temp=Hex(self.turt.pos(),self.length)
                    temp.drawhex()
                    if layers-layer>0:
                        temp.createSurrounding(layers-layer)
                distance=distance+distanceBetweenLayers
                self.turt.pencolor('red')
                self.drawhex()
                layer+=1
    def writeatcenter(self, whattowrite):
        self.turt.pu()
        self.turt.goto(self.center)
        self.turt.write(whattowrite)
