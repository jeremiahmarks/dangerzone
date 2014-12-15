import fvh
import fvhmans
import math
import datetime
from wand.image import Image

def anothercircle(innumofpoints, outnumofpoints, innerrad, outterrad, lm=None):
  if not lm:
    lm=fvh.MyTurtle()
  lm.speed(0)
  lm.ht()
  lm.tracer(False)
  innercircle={}
  outtercircle={}
  innerdeg=360.0/innumofpoints
  outterdeg=360.0/outnumofpoints
  
  for point in range(innumofpoints):
    lm.gohome()
    lm.setheading(point*innerdeg)
    lm.pu()
    lm.fd(innerrad)
    innercircle[point]=lm.position()
  for apoint in range(outnumofpoints):
    lm.gohome()
    lm.setheading(apoint*outterdeg)
    lm.pu()
    lm.fd(outterrad)
    outtercircle[apoint]=lm.position()
  for start in range(len(innercircle)):
    for end in range(len(outtercircle)):
      lm.goto(innercircle[start])
      lm.pd()
      lm.goto(outtercircle[end])
      #print outtercircle[end], innercircle[start]
      lm.pu()
  lm.tracer(True)
  savetocircles(lm)   
   
def getCirclePoints(numofPoints, radius):
  lm=fvh.MyTurtle()
  lm.speed(0)
  lm.ht()
  circlepoints={}
  degperpt=360.0/numofPoints
  for point in range(numofPoints):
    lm.gohome()
    lm.pu()
    lm.setheading(point*degperpt)
    lm.fd(radius)
    circlepoints[point]=lm.position()
  #lm.bye()
  return circlepoints

def savetocircles(aturtle,afilename=None,aheight=None,awidth=None,ax=None,ay=None, togif=True, topng=False):
  
  if not afilename:
    datetime.datetime.now()
    afilename='circles/'+datetime.datetime.now().strftime('%Y-%b-%d_%H:%M:%S.%f'+'.eps')
  aturtle.getscreen().getcanvas().postscript(file=afilename, height=aheight, width=awidth, x=ax, y=ay)
  if togif:
    with Image(filename=afilename) as img:
      with img.convert('gif') as newimg:
        newfilename=afilename[:-3]+'gif'
        newimg.save(filename=newfilename)
  if topng:
    with Image(filename=afilename) as img:
      with img.convert('png') as newimg:
        newfilename=afilename[:-3]+'png'
        newimg.save(filename=newfilename)
    
    
def graph():
  lm=fvh.MyTurtle()
  lm.ht()
  lm.speed(0)
  for x in range(0,10000,5):
    lm.goto(x/100.0, 10*math.sin(x/100.0))

def cirstr():
  lm=fvh.MyTurtle()
  lm.speed(0)
  lm.ht()
  lm.tracer(False)
  circlepoints=getCirclePoints(20,800)
  strpoints={}
  for x in range(0,100,8):
    strpoints[x]=(300,x*20)
    strpoints[x+1]=(300,-(x*20))
    strpoints[x+2]=(-300,-(x*20))
    strpoints[x+3]=(-300,(x*20))
    strpoints[x+4]=(x*20,300)
    strpoints[x+5]=(-(x*20),300)
    strpoints[x+6]=(-(x*20),-300)
    strpoints[x+7]=((x*20),-300)
    
    #for y in range(8):
        #print x,y,strpoints[x+y]
  minScreenSize=fvhmans.getSS([circlepoints, strpoints])
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  lm.getscreen().screensize(minScreenSize[0],minScreenSize[1])
  for start in range(len(circlepoints)):
    for end in range(len(strpoints)):
      lm.pu()
      lm.goto(circlepoints[start])
      lm.pd()
      lm.goto(strpoints[end])
      #print str(start) +'to' + str(end)
      #print circlepoints[start],strpoints[end]
  lm.tracer(True)
  fname="circles/fvh2cirstrw_.eps"
  print fname
  savetocircles(lm ,afilename=fname,awidth=minScreenSize[0], aheight=minScreenSize[1],ax=-minScreenSize[0]/2.0,ay=-minScreenSize[1]/2.0 )
  
def acirstr(pointsincircle, circleDiameter, strstop, strtopes,lm=None):
  if not lm:
    lm=fvh.MyTurtle()
  lm.speed(0)
  lm.ht()
  lm.tracer(False)
  circlepoints=getCirclePoints(pointsincircle,circleDiameter)
  strpoints={}
  for x in range(0,strstop,8):
    strpoints[x]=(strtopes,x*20)
    strpoints[x+1]=(strtopes,-(x*20))
    strpoints[x+2]=(-strtopes,-(x*20))
    strpoints[x+3]=(-strtopes,(x*20))
    strpoints[x+4]=(x*20,strtopes)
    strpoints[x+5]=(-(x*20),strtopes)
    strpoints[x+6]=(-(x*20),-strtopes)
    strpoints[x+7]=((x*20),-strtopes)
  print len(strpoints)
    
    #for y in range(8):
        #print x,y,strpoints[x+y]
  minScreenSize=fvhmans.getSS([circlepoints, strpoints])
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  lm.getscreen().screensize(minScreenSize[0],minScreenSize[1])
  for start in range(len(circlepoints)):
    for end in range(len(strpoints)):
      lm.pu()
      lm.goto(circlepoints[start])
      lm.pd()
      lm.goto(strpoints[end])
      #print str(start) +'to' + str(end)
      #print circlepoints[start],strpoints[end]
  lm.tracer(True)
  fname="circles/fvh2cirstrw_"+str(pointsincircle)+'o'+str(circleDiameter)+'o'+str(strstop)+'o'+str(strtopes)+".eps"
  print fname
  savetocircles(lm ,afilename=fname,awidth=minScreenSize[0], aheight=minScreenSize[1],ax=-minScreenSize[0]/2.0,ay=-minScreenSize[1]/2.0,togif=True )
  
def cirstra(pointsinCircle,circlediameter,pointsinsquare,squaresize,lm):
  #lm=fvh.MyTurtle()
  lm.speed(0)
  lm.ht()
  lm.tracer(False)
  circlepoints=getCirclePoints(pointsinCircle,circlediameter)
  strpoints={}
  squarestep=squaresize/float(pointsinsquare)
  for x in range(0,(pointsinsquare*8),8):
    strpoints[x]=(squaresize,(x/8)*squarestep)
    strpoints[x+1]=(squaresize,-((x/8)*squarestep))
    strpoints[x+2]=(-squaresize,-((x/8)*squarestep))
    strpoints[x+3]=(-squaresize,((x/8)*squarestep))
    strpoints[x+4]=((x/8)*squarestep,squaresize)
    strpoints[x+5]=(-((x/8)*squarestep),squaresize)
    strpoints[x+6]=(-((x/8)*squarestep),-squaresize)
    strpoints[x+7]=(((x/8)*squarestep),-squaresize)
    
    #for y in range(8):
        #print x,y,strpoints[x+y]
  minScreenSize=fvhmans.getSS([circlepoints, strpoints])
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  lm.getscreen().screensize(minScreenSize[0],minScreenSize[1])
  #lm.getscreen().setup(minScreenSize[0]+200, minScreenSize[1]+200)
  circlepoints=fvhmans.center(circlepoints)
  strpoints=fvhmans.center(strpoints)
  for start in range(len(circlepoints)):
    for end in range(len(strpoints)):
      lm.pu()
      lm.goto(circlepoints[start])
      lm.pd()
      lm.goto(strpoints[end])
      #print str(start) +'to' + str(end)
      #print circlepoints[start],strpoints[end]
  lm.tracer(True)
  savetocircles(lm ,awidth=minScreenSize[0], aheight=minScreenSize[1],ax=-minScreenSize[0]/2.0,ay=-minScreenSize[1]/2.0 )

  
def twoshapes(firstpoints, secondpoints,lm):
  lm.reset()
  lm.setup()
  minScreenSize=fvhmans.getSS([firstpoints, secondpoints])
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  b=lm.getscreen()
  b.screensize(minScreenSize[0],minScreenSize[1])
  b.setup(minScreenSize[0]*2,minScreenSize[1]*2)
  afilename='circles/twoshapes/'+datetime.datetime.now().strftime('%Y-%b-%d_%H:%M:%S.%f'+'.eps')
  for start in range(len(firstpoints)):
    for firstend in range(len(secondpoints)):
      lm.pu()
      lm.goto(firstpoints[start])
      lm.pd()
      lm.goto(secondpoints[firstend])
      lm.pu()
      
    for secondend in range(start,len(firstpoints)):
      lm.pu()
      lm.goto(firstpoints[start])
      lm.pd()
      lm.goto(firstpoints[secondend])
      lm.pu()
  for secondstart in range(len(secondpoints)):
    for thirdend in range(secondstart,len(secondpoints)):
      lm.pu()
      lm.goto(secondpoints[secondstart])
      lm.pd()
      lm.goto(secondpoints[thirdend])
      lm.pu()
  savetocircles(lm, afilename=afilename, ax=-minScreenSize[0], ay=-minScreenSize[1], awidth=2*minScreenSize[0], aheight=2*minScreenSize[1], togif=True)
  
def drawaxis():
  lm=fvh.MyTurtle()
  lm.setup()
  for x in range(4):
    lm.goto(0,0)
    lm.seth(x*90)
    for x in range(100):
      lm.write(x*20)
      lm.fd(20)
      
def circlearound(point,radius,lm):
  lm.pu()
  lm.goto(point[0],point[1]-radius)
  lm.pd()
  lm.seth(0)
  lm.circle(radius)
  lm.pu()
  
  
def interlappingcircles():
  circles=[]
  circle0=((0,0),200)
  circle1=((200,0),100)
  circles.append(circle0)
  circles.append(circle1)
  lm=fvh.MyTurtle()
  lm.setup()
  circlearound(circle0[0],circle0[1],lm)
  circlearound(circle1[0],circle1[1],lm)
  newcircles=fvhmans.circleinter(circle0[0][0],circle0[0][1], circle0[1],circle1[0][0],circle1[0][1], circle1[1])
  circlearound(newcircles[0],50,lm)
  circlearound(newcircles[1],50,lm) 
  
  
def manyshapes(listofdictionariesofpoints,lm):
  ld=listofdictionariesofpoints
  lm.reset()
  lm.setup()
  minScreenSize=fvhmans.getSS(ld)
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  b=lm.getscreen()
  b.screensize(minScreenSize[0],minScreenSize[1])
  b.setup(minScreenSize[0]*2,minScreenSize[1]*2)
  afilename='circles/manyshapes/'+datetime.datetime.now().strftime('%Y-%b-%d_%H:%M:%S.%f'+'.eps')
  for shapepos in range(len(ld)-1):
    lm.tracer(False)
    first=ld[shapepos]
    second=ld[shapepos+1]
    for start in range(len(first)):
      for firstend in range(len(second)):
        lm.pu()
        lm.goto(first[start])
        lm.pd()
        lm.goto(second[firstend])
        lm.pu()
      for secondend in range(start,len(first)):
        lm.pu()
        lm.goto(first[start])
        lm.pd()
        lm.goto(second[secondend])
    for secondstart in range(len(second)):
      for thirdend in range(secondstart,len(second)):
        lm.pu()
        lm.goto(second[secondstart])
        lm.pd()
        lm.goto(second[thirdend])
        
    lm.tracer(True)
        
      
    
    
  savetocircles(lm, afilename=afilename, ax=-minScreenSize[0], ay=-minScreenSize[1], awidth=2*minScreenSize[0], aheight=2*minScreenSize[1], togif=True)


def allconnected(listofdictionariesofpoints,lm):
  ld=listofdictionariesofpoints
  lm.reset()
  lm.setup()
  lm.tracer(False)
  minScreenSize=fvhmans.getSS(ld)
  minScreenSize=(minScreenSize[0]*2, minScreenSize[1]*2)
  b=lm.getscreen()
  b.screensize(minScreenSize[0],minScreenSize[1])
  b.setup(minScreenSize[0]*2,minScreenSize[1]*2)
  afilename='circles/manyshapes/'+datetime.datetime.now().strftime('%Y-%b-%d_%H:%M:%S.%f'+'.eps')
  allpoints=[]
  for eachdic in ld:
    for eachval in eachdic.itervalues():
      allpoints.append(eachval)
  for firstpoint in range(len(allpoints)):
    for secondpoint in range(firstpoint,len(allpoints)):
      lm.pu()
      lm.goto(allpoints[firstpoint])
      lm.pd()
      lm.goto(allpoints[secondpoint])
      lm.pu()
  lm.tracer(True)
        
      
    
    
  savetocircles(lm, afilename=afilename, ax=-minScreenSize[0], ay=-minScreenSize[1], awidth=2*minScreenSize[0], aheight=2*minScreenSize[1], togif=True)

