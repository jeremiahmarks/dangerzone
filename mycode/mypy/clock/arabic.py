from fvh import MyTurtle

def one(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(8*unit)
    
def two(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit) #right 4
    lm.right(90)
    lm.fd(4.5*unit) # d 4.5
    lm.right(90)
    lm.fd(3*unit)  #in 3
    lm.left(90)
    lm.fd(2.5*unit) # d 2.5
    lm.left(90)
    lm.fd(3*unit)  # out 3
    lm.right(90)
    lm.fd(unit)  #down 1
    lm.right(90)
    lm.fd(4*unit) 
    lm.right(90)
    lm.fd(4.5*unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2.5*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(unit)
    
def three(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(unit*4)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2.5*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2.5*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(unit)
    
def four(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(4*unit)
    
def five(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2.5*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(4.5*unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(2.5*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(4.5*unit)
    
def six(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(6*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(8*unit)
    
def seven(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(7*unit)
    lm.left(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(unit)
    
def eight(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(unit)
    lm.pu()
    lm.right(90)
    lm.fd(unit)
    lm.pd()
    for x in range(2):
        lm.fd(2.5*unit)
        lm.left(90)
        lm.fd(2*unit)
        lm.left(90)
    lm.pu()
    lm.fd(3.5*unit)
    lm.pd()
    for x in range(2):
        lm.fd(2.5*unit)
        lm.left(90)
        lm.fd(2*unit)
        lm.left(90)
    lm.pu()
    lm.right(180)
    lm.fd(4.5*unit)
    lm.pd()
    lm.right(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(8*unit)
    
def nine(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.left(90)
    lm.fd(6*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.right(90)
    lm.fd(unit)
    lm.right(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(4*unit)
    
def zero(starth=0, startpos=(0,0), lm=None, height=40):
    if not lm:
        lm=MyTurtle()
    lm.pu()
    lm.goto(startpos)
    lm.seth(starth)
    lm.pd()
    unit=height/8.0
    lm.fd(4*unit)
    lm.right(90)
    lm.fd(8*unit)
    lm.right(90)
    lm.fd(unit)
    lm.pu()
    lm.right(90)
    lm.fd(unit)
    lm.pd()
    lm.fd(6*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.left(90)
    lm.fd(6*unit)
    lm.left(90)
    lm.fd(2*unit)
    lm.pu()
    lm.right(90)
    lm.fd(unit)
    lm.pd()
    lm.right(90)
    lm.fd(3*unit)
    lm.right(90)
    lm.fd(8*unit)
