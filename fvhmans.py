import math
import fvh
import datetime
from wand.image import Image
#This module is intended to supply functions that help with 
#various parts of image creation done with fvh

def getSS(listOfDictionarysOfPoints):
  currentMax=(0,0)
  for eachDictionary in listOfDictionarysOfPoints:
    for eachpoint in range(len(eachDictionary)):
      point=eachDictionary[eachpoint]
      #print point
      if (point[0]>currentMax[0]):
        currentMax=(point[0],currentMax[1])
      if (point[1]>currentMax[1]):
        currentMax=(currentMax[0],point[1])
  return currentMax
  
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
  
def getPolyPoints(numberofsides, lengthperside, numberofpointsperside):
  lm=fvh.MyTurtle()
  lm.pu()
  lm.speed(0)
  lm.ht()
  degreesperturn=360.0/numberofsides
  forwarddistance=float(lengthperside)/numberofpointsperside
  polypoints={}
  pointcounter=0
  for eachside in range(numberofsides):
    for eachpoint in range(numberofpointsperside):
      polypoints[pointcounter]=lm.position()
      pointcounter+=1
      lm.fd(forwarddistance)
    lm.left(degreesperturn)
  return polypoints
  
def center(setOfpoints):
  x=[]
  y=[]
  for point in range(len(setOfpoints)):
    x.append(setOfpoints[point][0])
    y.append(setOfpoints[point][1])
  x.sort()
  y.sort()
  xoffset=(x[0]+x[-1])/2.0
  yoffset=(y[0]+y[-1])/2.0
  newpoints={}
  for anotherpoint in range(len(setOfpoints)):
    newpoints[anotherpoint]=(setOfpoints[anotherpoint][0]-xoffset,setOfpoints[anotherpoint][1]-yoffset)
  
  return newpoints

def savetocircles(aturtle,afilename=None,aheight=None,awidth=None,ax=None,ay=None, togif=False, topng=False):
  
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

  
def circleinter(x0, y0, r0, x1, y1, r1):
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
  
def savetocircleshelp():
  lm=fvh.MyTurtle()
  lm.pu()
  lm.tracer(False)
  for x in range(0,1200,100):
    lm.pu()
    lm.goto(-x, x)
    lm.pd()

    lm.seth(270)
    for y in range(4):
      lm.write(lm.pos())
      for z in range(0,2*x,10):
        lm.fd(10)
        lm.write(lm.pos())
      lm.left(90)
  lm.tracer(True)
  return lm
    
