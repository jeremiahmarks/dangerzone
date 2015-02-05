import math
import fvh2, fvh
import supercircle

masterCircleSet=set()
circlecalled = 0
checkcirclescalled = 0
MINOFFSET=5


class Circle():
  def __init__(self,x,y,r,lm=None, keep=True):
    
    
    global circlecalled
    circlecalled+=1
    self.keep = keep
    self.center=(x,y)
    self.radius=r
    self.checkString=(int(x)/MINOFFSET*MINOFFSET,int(y)/MINOFFSET*MINOFFSET,r)
    masterCircleSet.add(self.checkString)
    self.color="black"
    if not lm:
      self.lm=fvh2.fvh.MyTurtle()
      self.lm.tracer(False)
    else:
      self.lm=lm      
    #self.draw()
    
    
  def draw(self):
    #self.lm=fvh2.fvh.MyTurtle()
    self.lm.pencolor(self.color)
    self.lm.setup()
    self.lm.penup()
    fvh2.circlearound(self.center, self.radius,self.lm)
    if not self.keep:
      self.lm.undo()
      self.lm.undo()

  def drawred(self):
    self.lm.pencolor('red')
    self.lm.penup()
    fvh2.circlearound(self.center, self.radius,self.lm)
    
  def drawwhite(self):
    self.lm.pencolor('white')
    self.lm.penup()
    fvh2.circlearound(self.center, self.radius,self.lm)
  
  def setcolor(self, color):
    self.color=color
    
  
  
  
  
  def realCards(self):
    self.realcards=[]
    self.lm.pu()
    for x in range(4):
      self.lm.goto(self.center)
      self.lm.seth(self.lm.towards(0,0)+90*x)
      self.lm.fd(self.radius)
      self.realcards.append(Circle(self.lm.xcor(), self.lm.ycor(), self.radius/2))
  
  def extendedCards(self, numberOfexteriorCircles):
    self.cardinals=[]
    angle=360.0/numberOfexteriorCircles
    for x in range(numberOfexteriorCircles):
      self.lm.pu()
      self.lm.goto(self.center)
      self.lm.seth(self.lm.towards(0,0)+180+x*angle)
      self.lm.fd(self.radius)
      a=Circle(self.lm.xcor(), self.lm.ycor(), self.radius/2, self.lm, self.keep)
      self.cardinals.append(a)
      if (self.radius/2>=4):
        a.extendedCards(numberOfexteriorCircles)
        for card in a.cardinals:
          self.cardinals.append(card)

  def innerextendedCards(self, numberOfexteriorCircles):
    self.cardinals=[]
    angle=360.0/numberOfexteriorCircles
    for x in range(numberOfexteriorCircles):
      self.lm.pu()
      self.lm.goto(self.center)
      self.lm.seth(self.lm.towards(0,0)+x*angle)
      self.lm.fd(self.radius)
      a=Circle(self.lm.xcor(), self.lm.ycor(), self.radius/2, self.lm, self.keep)
      self.cardinals.append(a)
      if (self.radius/2>=4):
        a.innerextendedCards(numberOfexteriorCircles)
        for card in a.cardinals:
          self.cardinals.append(card)
      
      
  def differentcards(self, numberOfexteriorCircles):
    self.cardinals=[]
    angle=360.0/numberOfexteriorCircles
    for x in range(numberOfexteriorCircles):
      self.lm.pu()
      self.lm.goto(self.center)
      self.lm.seth(self.lm.towards(0,0)+180+x*angle)
      self.lm.fd(self.radius)
      self.cardinals.append(Circle(self.lm.xcor(), self.lm.ycor(), self.radius/2, self.lm, self.keep))
  
  
  def addCardinals(self):
    self.cardinals=[]
    self.cardinals.append(Circle(self.center[0]+self.radius, self.center[1], self.radius/2))
    self.cardinals.append(Circle(self.center[0]-self.radius, self.center[1], self.radius/2))    
    self.cardinals.append(Circle(self.center[0], self.center[1]+self.radius, self.radius/2))
    self.cardinals.append(Circle(self.center[0], self.center[1]-self.radius, self.radius/2))
    #for eachcircle in self.cardinals:
    #  eachcircle.draw()
  def comparetoCardinals(self):
    self.primarytocardinals=[]
    for eachcircle in self.cardinals:
      intersectionpoints=circleinter(self.center, self.radius, eachcircle.center, eachcircle.radius)
      
      self.primarytocardinals.append(Circle(intersectionpoints[0][0], intersectionpoints[0][1], self.radius))
      self.primarytocardinals.append(Circle(intersectionpoints[1][0], intersectionpoints[1][1], self.radius))
      

def checkCircles(circle1, circle2):
  global checkcirclescalled
  checkcirclescalled+=1
  points=circleinter(circle1.center, circle1.radius, circle2.center, circle2.radius)
  if points:
    points=((float("%.2f" % points[0][0]),float("%.2f" % points[0][1])),(float("%.2f" % points[1][0]),float("%.2f" % points[1][1])))
  
  return points


def circleinter((x0, y0), r0, (x1, y1), r1):
  """
  This modules accepts two circles and then determines where they meet. 
  the circles are submitted as x,y,r where x,y is the center of the circle
  and r is the radius.
  
  """
  dx=float(x1-x0)
  dy=float(y1-y0)
  
  d=(dx**2+dy**2)**0.5
  
  if (d>(r0+r1)):
    return None
    
  if (d< math.fabs(r0-r1)):
    return None
  if (d==0):
    return None
  
  a = ((r0*r0) - (r1*r1) + (d*d)) / (2.0 * d)
  
  x2 = x0 + (dx * a/d)
  y2 = y0 + (dy * a/d)
  
  h = ((r0*r0) - (a*a))**0.5
  
  rx = -dy * (h/d)
  ry = dx * (h/d)
  
  xi = x2 + rx
  xi_prime = x2 - rx
  yi = y2 + ry
  yi_prime = y2 - ry
  
  return (xi,yi),(xi_prime,yi_prime)

def differentCircles(primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta,lm=None):
  filenameStrings=['primaryCircleRadius','secondaryCircleRadius','numberOfSecondaryCircles','secondaryCircleTheta']
  filenameValues=[primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta]
  filenameZip=zip(filenameStrings,filenameValues)
  filename=''
  for values in filenameZip:
    filename=filename+values[0]+str(values[1])
  filename='circles/'+filename+'.eps'
  
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  ts=lm.getscreen()
  circlelist=[]
  newlist=[]
  primaryCircle=Circle(0,0,primaryCircleRadius,lm)
  primaryCircle.draw()
  circlelist.append(primaryCircle)
  for circle in range(numberOfSecondaryCircles):
    lm.pu()
    lm.goto(primaryCircle.center)
    lm.seth(circle*secondaryCircleTheta)
    lm.fd(primaryCircleRadius)
    temp=Circle(lm.xcor(), lm.ycor(), secondaryCircleRadius, lm)
    temp.draw()
    circlelist.append(temp)
  totalbefore=len(circlelist)
  totalafter=0
  counter=0
  while(totalbefore!=totalafter):
    totalbefore=len(circlelist)
    for firstCircleplace in range(len(circlelist)):
      firstCircle=circlelist[firstCircleplace]
      for secondCircleplace in range(firstCircleplace,len(circlelist)):
        secondCircle=circlelist[secondCircleplace]
        thisRadius=min(firstCircle.radius, secondCircle.radius)/2
        if (thisRadius<10):
          continue
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          if ((int(newCircles[0][0])/MINOFFSET*MINOFFSET,int(newCircles[0][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            temp=Circle(newCircles[0][0], newCircles[0][1], thisRadius,lm)
            temp.draw()
            newlist.append(temp)
          if ((int(newCircles[1][0])/MINOFFSET*MINOFFSET,int(newCircles[1][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            temp=Circle(newCircles[1][0], newCircles[1][1], thisRadius,lm)
            temp.draw()
            newlist.append(temp)
          ts.update()
          
    counter=len(circlelist)
    for item in newlist:
      item.draw()
      circlelist.append(item)
    ts.update()
    newlist=[]
    totalafter=len(circlelist)
  fvh2.savetocircles(lm,filename)

def differentCirclesforViewing(primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta,lm=None):
  """
  This is designed with something like the following in mind:
  
  lm=circleint.fvh2.fvh.MyTurtle()
  for a in range(2,100):
    for b in range(3600):
      circleint.differentCirclesforAnimation(200,15,a,b/10.0,lm)
      lm.clear()
  
  and then make a gif of the results
  
  """
  global masterCircleSet
  masterCircleSet=set()
  filenameStrings=['primaryCircleRadius','secondaryCircleRadius','numberOfSecondaryCircles','secondaryCircleTheta']
  filenameValues=[primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta]
  filenameZip=zip(filenameStrings,filenameValues)
  filename=''
  for values in filenameZip:
    filename=filename+values[0]+'%03d' % values[1]
  filename='circles/testa/'+filename+'.eps'
  
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  ts=lm.getscreen()
  circlelist=[]
  newlist=[]
  primaryCircle=Circle(0,0,primaryCircleRadius,lm)
  primaryCircle.draw()
  circlelist.append(primaryCircle)
  colorcounter=0
  for circle in range(numberOfSecondaryCircles):
    lm.pu()
    lm.goto(primaryCircle.center)
    lm.seth((secondaryCircleTheta+(circle*secondaryCircleTheta))%360)
    lm.fd(primaryCircleRadius)
    temp=Circle(lm.xcor(), lm.ycor(), secondaryCircleRadius, lm)
    temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
    colorcounter+=1
    temp.draw()
    circlelist.append(temp)
  totalbefore=len(circlelist)
  totalafter=0
  counter=0
  
  while(totalbefore!=totalafter):
    totalbefore=len(circlelist)
    for firstCircleplace in range(len(circlelist)):
      firstCircle=circlelist[firstCircleplace]
      for secondCircleplace in range(len(circlelist)):
        secondCircle=circlelist[secondCircleplace]
        thisRadius=min(firstCircle.radius, secondCircle.radius)/2
        if (thisRadius<10):
          continue
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          if ((int(newCircles[0][0])/MINOFFSET*MINOFFSET,int(newCircles[0][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            
            temp=Circle(newCircles[0][0], newCircles[0][1], thisRadius,lm)
            temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
            
            colorcounter+=1
            temp.draw()
            newlist.append(temp)
          if ((int(newCircles[1][0])/MINOFFSET*MINOFFSET,int(newCircles[1][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            
            temp=Circle(newCircles[1][0], newCircles[1][1], thisRadius,lm)
            temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
            colorcounter+=1
            temp.draw()
            newlist.append(temp)
          ts.update()
          #masterCircleSet=set()
          
    counter=len(circlelist)
    for item in newlist:
      #item.draw()
      circlelist.append(item)
    ts.update()
    newlist=[]
    totalafter=len(circlelist)
    

  #fvh2.savetocircles(lm,filename,aheight=(primaryCircleRadius+secondaryCircleRadius),awidth=(primaryCircleRadius+secondaryCircleRadius),ax=-(primaryCircleRadius+secondaryCircleRadius)/2.0, ay=-(primaryCircleRadius+secondaryCircleRadius)/2.0 )  
  fvh2.savetocircles(lm,filename,togif=True)#,aheight=(primaryCircleRadius+secondaryCircleRadius),awidth=(primaryCircleRadius+secondaryCircleRadius))#,ax=-(primaryCircleRadius+secondaryCircleRadius)/2.0, ay=-(primaryCircleRadius+secondaryCircleRadius)/2.0 )

def differentCirclesforAnimation(primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta,lm=None):
  """
  This is designed with something like the following in mind:
  
  lm=circleint.fvh2.fvh.MyTurtle()
  for a in range(2,100):
    for b in range(3600):
      circleint.differentCirclesforAnimation(200,15,a,b/10.0,lm)
      lm.clear()
  
  and then make a gif of the results
  
  """
  filenameStrings=['primaryCircleRadius','secondaryCircleRadius','numberOfSecondaryCircles','secondaryCircleTheta']
  filenameValues=[primaryCircleRadius, secondaryCircleRadius, numberOfSecondaryCircles, secondaryCircleTheta]
  filenameZip=zip(filenameStrings,filenameValues)
  filename=''
  for values in filenameZip:
    filename=filename+values[0]+str(values[1])
  filename='circles/neatani/'+filename+'.eps'
  
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  ts=lm.getscreen()
  circlelist=[]
  newlist=[]
  primaryCircle=Circle(0,0,primaryCircleRadius,lm)
  #primaryCircle.draw()
  circlelist.append(primaryCircle)
  colorcounter=0
  for circle in range(numberOfSecondaryCircles):
    lm.pu()
    lm.goto(primaryCircle.center)
    lm.seth((secondaryCircleTheta+(circle*secondaryCircleTheta))%360)
    lm.fd(primaryCircleRadius)
    temp=Circle(lm.xcor(), lm.ycor(), secondaryCircleRadius, lm)
    temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
    colorcounter+=1
    temp.draw()
    circlelist.append(temp)
  totalbefore=len(circlelist)
  totalafter=0
  counter=0
  
  while(totalbefore!=totalafter):
    totalbefore=len(circlelist)
    for firstCircleplace in range(len(circlelist)):
      firstCircle=circlelist[firstCircleplace]
      for secondCircleplace in range(firstCircleplace,len(circlelist)):
        secondCircle=circlelist[secondCircleplace]
        thisRadius=min(firstCircle.radius, secondCircle.radius)/2
        if (thisRadius<10):
          continue
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          if ((int(newCircles[0][0])/MINOFFSET*MINOFFSET,int(newCircles[0][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            temp=Circle(newCircles[0][0], newCircles[0][1], thisRadius,lm)
            temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
            colorcounter+=1
            temp.draw()
            newlist.append(temp)
          if ((int(newCircles[1][0])/MINOFFSET*MINOFFSET,int(newCircles[1][1])/MINOFFSET*MINOFFSET,thisRadius) not in masterCircleSet):
            temp=Circle(newCircles[1][0], newCircles[1][1], thisRadius,lm)
            temp.setcolor(fvh.allcolors[colorcounter%len(fvh.allcolors)])
            colorcounter+=1
            temp.draw()
            newlist.append(temp)
          ts.update()
          
    counter=len(circlelist)
    for item in newlist:
      #item.draw()
      circlelist.append(item)
    ts.update()
    newlist=[]
    totalafter=len(circlelist)
  #fvh2.savetocircles(lm,filename)  

def createDrawing(bigdiameter,diameter):
  lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  a=Circle(0,0,bigdiameter,lm)
  b=Circle(bigdiameter,0,diameter,lm)
  circlelist=[a,b]
  totalbefore=len(masterCircleSet)
  totalafter=0
  newlist=[]
  counter=0
  #print totalbefore
  while((totalbefore!=totalafter) and (len(masterCircleSet)<750)):
    #print (circlecalled, checkcirclescalled)
    #print totalbefore, totalafter
    #raw_input()
    print len(masterCircleSet)
    totalbefore=len(masterCircleSet)
    for firstCircleplace in range(counter,len(circlelist)):
      firstCircle=circlelist[firstCircleplace]
      for secondCircleplace in range(len(circlelist)):
        secondCircle=circlelist[secondCircleplace]
        newCircles=checkCircles(firstCircle, secondCircle)
      #print newCircles, len(newlist)
      #raw_input((totalbefore,totalafter))
        if newCircles:
          if ((int(newCircles[0][0])/MINOFFSET*MINOFFSET,int(newCircles[0][1])/MINOFFSET*MINOFFSET,diameter) not in masterCircleSet):
            newlist.append(Circle(newCircles[0][0], newCircles[0][1], diameter,lm))
          else:
            print newCircles[0]
          if ((int(newCircles[1][0])/MINOFFSET*MINOFFSET,int(newCircles[1][1])/MINOFFSET*MINOFFSET,diameter) not in masterCircleSet):
            newlist.append(Circle(newCircles[1][0], newCircles[1][1], diameter,lm))
          else:
            print newCircles[1]
    counter=len(circlelist)
    for item in newlist:
      item.draw()
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
  lm.tracer(True)
  a.lm.tracer(True)
  fvh2.savetocircles(a.lm)
    
          
def createanotherdrawing(startSize):
  a=Circle(0,0,startSize)
  smallestsize=startSize
  a.addCardinals()
  a.lm.undo()
  a.lm.undo()
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    circlelist.append(eachitem)
    eachitem.lm.undo()
    eachitem.lm.undo()
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      
      for secondCircle in circlelist:
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2
        if (thisDiameter<=1):
          #print "first break"
          break
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter)
              newCircle.draw()
              circlelist.append(newCircle)
              #for eachCard in newCircle.cardinals:
                #circlelist.append(eachCard)
      #if (thisDiameter<=1):
        #print "second break"
        
    
    for item in newlist:
      circlelist.append(item)
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
    
  fvh2.savetocircles(a.lm)
  
def yetanotherdrawing(startdiameter,numberofoutsidecircles):
  lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm)
  a.lm.undo()
  a.lm.undo()  
  a.differentcards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    eachitem.lm.undo()
    eachitem.lm.undo()
    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      print "new firstCircle : " + str(firstCircle.checkString)
      print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2.0
        if (thisDiameter<=1):
          #print "first break"
          #secondCircle.draw()
          break
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              #newCircle.realCards()
              circlelist.append(newCircle)
              #for eachCard in newCircle.realcards:
              #  circlelist.append(eachCard)
        #secondCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    for item in newlist:
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
  for acircle in circlelist:
    acircle.draw()
  lm.tracer(True)
    
  fvh2.savetocircles(a.lm)


def yetanotherdrawingagain(startdiameter,numberofoutsidecircles, recursive=False, lm=None):
  global masterCircleSet
  masterCircleSet=set()
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm)
#  a.lm.undo()
#  a.lm.undo()  
  a.differentcards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    #eachitem.lm.undo()
    #eachitem.lm.undo()
    eachitem.differentcards(numberofoutsidecircles)
    for subitem in eachitem.cardinals:
      #subitem.lm.undo()
      #subitem.lm.undo()
      circlelist.append(subitem)

    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    #print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      #print "new firstCircle : " + str(firstCircle.checkString)
      #print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2.0
        if (min(firstCircle.radius, secondCircle.radius)<=1):
          #print "first break"
          #secondCircle.draw()
          break
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          #print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              
              newlist.append(newCircle)
              if recursive:
                newCircle.differentcards(numberofoutsidecircles)
                for eachCard in newCircle.cardinals:
                  circlelist.append(eachCard)
        #secondCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    
    for item in newlist:
      item.draw()
      circlelist.append(item)
    
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
  

  lm.tracer(True)
  fvh2.savetocircles(a.lm)

def yetanotherdrawingagainwithmax(startdiameter,numberofoutsidecircles, recursive=False, lm=None,stepsize=2):
  global masterCircleSet
  masterCircleSet=set()
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm,False)
#  a.lm.undo()
#  a.lm.undo()  
  a.differentcards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    #eachitem.lm.undo()
    #eachitem.lm.undo()
    eachitem.differentcards(numberofoutsidecircles)
    for subitem in eachitem.cardinals:
      #subitem.lm.undo()
      #subitem.lm.undo()
      circlelist.append(subitem)

    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
#    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      #print "new firstCircle : " + str(firstCircle.checkString)
      #print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #firstCircle.drawred()
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/float(stepsize)
        if (min(firstCircle.radius, secondCircle.radius)<=1):
          #print "first break"
          #secondCircle.draw()
          break
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          #print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              newCircle.draw()
              circlelist.append(newCircle)
              if recursive:
                newCircle.differentcards(numberofoutsidecircles)
                for eachCard in newCircle.cardinals:
                  eachCard.draw()
                  circlelist.append(eachCard)
        #secondCircle.draw()
        #firstCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    for item in newlist:
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
  lm.tracer(True)
  fvh2.savetocircles(a.lm)
    
  


  
def yadwm(startdiameter):
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter)
  a.addCardinals()
  
  a.lm.undo()
  a.lm.undo()
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    eachitem.lm.undo()
    eachitem.lm.undo()
    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      for secondCircle in circlelist:
        thisDiameter=max(firstCircle.radius, secondCircle.radius)/2.0
        if (thisDiameter<=32):
          #print "first break"
          break
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          #lm.tracer(False)
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter)
              newCircle.addCardinals()
              newCircle.draw()
              circlelist.append(newCircle)
              for eachCard in newCircle.cardinals:
                eachCard.draw()
                circlelist.append(eachCard)
          #lm.tracer(True)
      #if (thisDiameter<=1):
        #print "second break"
        
    
    for item in newlist:
      circlelist.append(item)
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
    
  fvh2.savetocircles(a.lm)
  
def makeart1():

  for size in range(7,11):
    for numberofsides in range(1,10):
        for recursive in (False, True):
            print 2**size,numberofsides,recursive
            lm=fvh2.fvh.MyTurtle()
            ts=lm.getscreen()
            ts.screensize(2**(size+2),2**(size+2),'grey50')
            ts.setup(2**(size+3),2**(size+3),0,0)
            yetanotherdrawingagain(2**size,numberofsides,recursive,lm)
            tc=ts.getcanvas()
            filename="circles/startSize"+str(size)+"numberofsides"+str(numberofsides)+str(recursive)+'.eps'
            ts.update()
            tc.postscript(file=filename, height=2**(size+2), width=2**(size+2),x=-2**(size+1),y=-2**(size+1))
            ts.bye()
            
def makeart2():

  for size in range(8,11):
    for numberofsides in range(6,10):
      for recursive in (False, True):
        for stepsize in range(2,4):  
          print stepsize**size,numberofsides,recursive
          lm=fvh2.fvh.MyTurtle()
          ts=lm.getscreen()
          ts.screensize(stepsize**(size+2),stepsize**(size+2),'grey50')
          ts.setup(stepsize**(size+3),stepsize**(size+3),0,0)
          yetanotherdrawingagainwithmax(stepsize**size,numberofsides,recursive,lm,stepsize)
          tc=ts.getcanvas()
          filename="circles/max"+str(size)+str(numberofsides)+str(recursive)+'.eps'
          tc.postscript(file=filename, height=stepsize**(size+2), width=stepsize**(size+2),x=-stepsize**(size+1),y=-stepsize**(size+1))
          ts.bye()
          
def yetanotherdrawingagainwithcontinue(startdiameter,numberofoutsidecircles, recursive=False, lm=None):
  global masterCircleSet
  masterCircleSet=set()
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  lm.tracer(False)
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm)
  a.draw()
  a.lm.undo()
  a.lm.undo()  
  a.differentcards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    eachitem.draw()
    eachitem.lm.undo()
    eachitem.lm.undo()
    #eachitem.draw()
    eachitem.differentcards(numberofoutsidecircles)
    for subitem in eachitem.cardinals:
      subitem.draw()
      subitem.lm.undo()
      subitem.lm.undo()
      circlelist.append(subitem)

    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    #print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      #print "new firstCircle : " + str(firstCircle.checkString)
      #print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2.0
        if (min(firstCircle.radius, secondCircle.radius)<=4):
          #print "first break"
          #secondCircle.draw()
          continue
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          #print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              newCircle.draw()
              newlist.append(newCircle)
              if recursive:
                newCircle.differentcards(numberofoutsidecircles)
                for eachCard in newCircle.cardinals:
                  eachCard.draw()
                  circlelist.append(eachCard)
        #secondCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    for item in newlist:
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
  lm.tracer(True)  
  fvh2.savetocircles(a.lm)
  
def yetanotherdrawingagainwithcontinueandextended(startdiameter,numberofoutsidecircles, recursive=False, lm=None):
  global masterCircleSet
  masterCircleSet=set()
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm)
#  a.lm.undo()
#  a.lm.undo()  
  a.extendedCards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  for eachitem in a.cardinals:
    #eachitem.lm.undo()
    #eachitem.lm.undo()
    #eachitem.differentcards(numberofoutsidecircles)
    #for subitem in eachitem.cardinals:
      #subitem.lm.undo()
      #subitem.lm.undo()
      #circlelist.append(subitem)

    circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      #print "new firstCircle : " + str(firstCircle.checkString)
      #print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2.0
        if (min(firstCircle.radius, secondCircle.radius)<=4):
          #print "first break"
          #secondCircle.draw()
          continue
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          #print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              
              newlist.append(newCircle)
              if recursive:
                newCircle.extendedCards(numberofoutsidecircles)
                for eachCard in newCircle.cardinals:
                  circlelist.append(eachCard)
        #secondCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    for item in newlist:
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
    
  fvh2.savetocircles(a.lm)
  return circlelist
  
def yadei(startdiameter,numberofoutsidecircles, recursive=False, lm=None):
  global masterCircleSet
  masterCircleSet=set()
  if not lm:
    lm=fvh2.fvh.MyTurtle()
  lm.setup()
  smallestsize=startdiameter
  a=Circle(0,0,startdiameter,lm)
#  a.lm.undo()
#  a.lm.undo()  
  a.innerextendedCards(numberofoutsidecircles)
  circlelist=[]
  circlelist.append(a)
  #for eachitem in a.cardinals:
    #eachitem.lm.undo()
    #eachitem.lm.undo()
    #eachitem.differentcards(numberofoutsidecircles)
    #for subitem in eachitem.cardinals:
      #subitem.lm.undo()
      #subitem.lm.undo()
      #circlelist.append(subitem)

    #circlelist.append(eachitem)
  totalbefore=len(masterCircleSet)
  totalafter=0
  while ((totalbefore!=totalafter)):
    print "Just started new while loop. number of circles in circlelist: "+str(len(circlelist))
    
    totalbefore=len(masterCircleSet)
    newlist=[]
    for firstCircle in circlelist:
      #print "new firstCircle : " + str(firstCircle.checkString)
      #print "Current number of circles in circlelist: "+str(len(circlelist))
      #firstCircle.drawred()
      for secondCircle in circlelist:
        #secondCircle.drawred()
        thisDiameter=min(firstCircle.radius, secondCircle.radius)/2.0
        if (min(firstCircle.radius, secondCircle.radius)<=4):
          #print "first break"
          #secondCircle.draw()
          continue
        if thisDiameter<smallestsize:
          smallestsize=thisDiameter
          #print "New Smallest Size: "+ str(smallestsize)
        newCircles=checkCircles(firstCircle, secondCircle)
        if newCircles:
          
          for x in newCircles:
            if ((int(x[0])/MINOFFSET*MINOFFSET, int(x[1])/MINOFFSET*MINOFFSET, thisDiameter) not in masterCircleSet):
              newCircle=Circle(x[0], x[1],thisDiameter,lm)
              
              newlist.append(newCircle)
              if recursive:
                newCircle.innerextendedCards(numberofoutsidecircles)
                for eachCard in newCircle.cardinals:
                  circlelist.append(eachCard)
        #secondCircle.draw()
      #if (thisDiameter<=1):
        #print "second break"
        
      #firstCircle.draw()
    for item in newlist:
      circlelist.append(item)
    newlist=[]
    totalafter=len(masterCircleSet)
    if (totalafter==totalbefore):
      print "no more moves"
    
  fvh2.savetocircles(a.lm)
  return circlelist
  
def itsOct():
  pass
