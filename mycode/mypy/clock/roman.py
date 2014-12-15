from fvh import MyTurtle
import math

def one(starth=270, startpos=(0,0), lm=None, cube=[60,60]):
    if not lm:
        lm=MyTurtle()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    lm.ht()
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(30)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(30)
    lm.tracer(True)
    
def two(starth=270, startpos=(0,0), lm=None):
    if not lm:
        lm=MyTurtle()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    lm.ht()
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.pu()
    lm.rt(180)
    lm.fd(20)
    lm.left(90)
    lm.fd(5)
    lm.pd()
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.right(90)
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.tracer(True)
    
def three(starth=270, startpos=(0,0), lm=None):
    if not lm:
        lm=MyTurtle()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    lm.ht()
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(90)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.left(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(90)
    lm.pu()
    lm.rt(180)
    lm.fd(20)
    lm.left(90)
    lm.fd(5)
    
    lm.pd()
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.right(90)
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.pu()
    lm.rt(180)
    lm.fd(30)
    lm.left(90)
    lm.pd()
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.right(90)
    lm.fd(40)
    lm.right(90)
    lm.fd(20)
    lm.tracer(True)
    
def five(starth=270, startpos=(0,0), lm=None):
    if not lm:
        lm=MyTurtle()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    lm.ht()
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    top0=lm.pos()
    topheading=lm.heading()
    theta=math.degrees(math.asin(40.0/((15.0**2+40.0**2)**0.5)))
    lm.seth(topheading+theta)
    lm.fd((15.0**2+40.0**2)**0.5)
    lm.seth(topheading-180)
    lm.fd(25)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(25)
    lm.seth(topheading-theta)
    lm.fd((15.0**2+40.0**2)**0.5)
    lm.seth(topheading)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.pu()
    lm.right(180)
    lm.fd(20)
    lm.left(90)
    lm.fd(5)
    lm.pd()
    innertheta=math.degrees(math.asin(30/((10.0**2+30.0**2)**0.5)))
    lm.seth(topheading+innertheta)
    lm.fd((10.0**2+30.0**2)**0.5)
    lm.seth(topheading-innertheta)
    lm.fd((10.0**2+30.0**2)**0.5)
    lm.seth(topheading-180.0)
    lm.fd(20)
    lm.tracer(True)
    
def ten(starth=270, startpos=(0,0), lm=None):
    if not lm:
        lm=MyTurtle()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    lm.ht()
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    topheading=lm.heading()
    outtertheta=math.degrees(math.asin(25.0/((15.0**2+25.0**2)**0.5)))
    lm.seth(topheading+outtertheta)  #top right
    lm.fd((15.0**2+25.0**2)**0.5)
    lm.seth(topheading-(180+outtertheta)) # middle right

    lm.fd((15.0**2+25.0**2)**0.5)
    lm.seth(topheading-180)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(10)
    lm.seth(topheading+(180+outtertheta)) # bottom left
    lm.fd((15.0**2+25.0**2)**0.5)
    lm.seth(topheading-outtertheta) # middle left
    lm.fd((15.0**2+25.0**2)**0.5)
    lm.seth(topheading)
    lm.fd(10)
    lm.right(90)
    lm.fd(5)
    lm.right(90)
    lm.fd(60)
    lm.pu()
    lm.right(180)
    lm.fd(20)
    lm.left(90)
    lm.fd(5)
    lm.right(90)
    lm.pd()
    lm.fd(20)
    lm.seth(180+(topheading-outtertheta))
    lm.fd((2.0/3.0)*((15.0**2+25.0**2)**0.5))
    lm.seth(topheading+(180+outtertheta))
    lm.fd((2.0/3.0)*((15.0**2+25.0**2)**0.5))    
    lm.pu()
    lm.seth(90+topheading)
    lm.fd(50)
    lm.pd()
    lm.seth(topheading)
    lm.fd(20)
    lm.seth(topheading+(180+outtertheta))
    lm.fd((2.0/3.0)*((15.0**2+25.0**2)**0.5))
    lm.seth(180+(topheading-outtertheta))
    lm.fd((2.0/3.0)*((15.0**2+25.0**2)**0.5))
    lm.tracer(True)
    
    
def fifty(starth=270, startpos=(0,0), lm=None):
    if not lm:
        lm=MyTurtle()
    lm.ht()
    lm.tracer(False)
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.fd(35)
    lm.pd()
    lm.fd(15)
    lm.right(90)
    lm.fd(30)
    lm.right(90)
    lm.fd(50)
    lm.right(90)
    lm.fd(10)
    lm.right(90)
    lm.fd(40)
    lm.left(90)
    lm.fd(15)
    lm.left(45)
    lm.fd(50**0.5)
    lm.tracer(True)