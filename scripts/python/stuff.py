import circleint
import supercircle
import fvh2


def every():
  a()
  b()
  c()

def a():
  for x in range(100,1700,100):
    for y in range(1,50):
      circleint.masterCircleSet=set()
      circleint.yetanotherdrawing(x,y)
      circleint.fvh.MyTurtle().getscreen().bye()
      
def b():
  lm=circleint.fvh.MyTurtle()
  for x in range(100,1200,100):
    for y in range(1,8):
      print x,y
      circleint.masterCircleSet=set()
      circleint.yetanotherdrawingagain(x,y,lm=lm)
      lm.tracer(False)
      lm.clear()
      circleint.masterCircleSet=set()
      circleint.yetanotherdrawingagain(x,y,True,lm)
      lm.tracer(False)
      lm.clear()
      
def c():
  lm=circleint.fvh.MyTurtle()
  for x in range(100,1700,100):
    for y in range(1,30):
      circleint.masterCircleSet=set()
      circleint.yetanotherdrawingagainwithcontinue(x,y,lm=lm)
      #raw_input()
      lm.tracer(False)
      lm.clear()
      #circleint.masterCircleSet=set()
      #circleint.yetanotherdrawingagainwithcontinue(x,y,True,lm=lm)
      #raw_input()
      #lm.clear()
      
def d():
  allcircles=[]
  a=supercircle.sTurtle()
  a.tracer(False)
  for x in range(400):
    a.tracer(False)
    allcircles.append(supercircle.sCircle((-200+x, 0), 30))
    for each in allcircles:
      each.turn()
  for x in range(720):
    filen='circles/%03d.eps' %x
    for each in allcircles:
        each.turn()
    a.tracer(True)
    a.tracer(False)
    fvh2.savetocircles(a, filen)
    #print x, filen    
