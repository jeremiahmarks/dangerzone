#various artsy things

from TurtleWorld import *
import math
import random
world = TurtleWorld()
bob=Turtle()
bob.delay=0.01


def shape(turt,height,width):
    for i in range (4):
        turt.fd(height)
        turt.lt(20)
        turt.fd(width)
        turt.lt(20)

def offset(turt, fraction):
    fraction=float(fraction)*.1
    turn=fraction*360
    turt.rt(turn)
    


def goart(rep,turt):

    offsetdeg=random.randint(0,360)
    for i in range (rep):
        shape(turt,i,2*i)
        offset(turt,i*2)
        
def rect(turt, height,length):
    for i in range (2):
        turt.fd(length)
        turt.lt(90)
        turt.fd(height)
        turt.lt(90)
#Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360.0/n degrees.
def polygon(turt, sides,length):
    angle=360.0/sides
    for i in range (sides):
        turt.fd(length)
        turt.lt(angle)

def circle(turt,radius):
    #turt.bk(radius)
    turt.fd(2*radius) #this establishes diameter
    turt.lt(90)       #turns the turtle perpendicular to the diameter
    circ=math.pi*2*radius       #circ is circumference
    num_of_sides=math.floor(circ)  #determin number of sides. this should scale with the size of the circle
    num_of_sides=int(num_of_sides)
    length_of_side=circ/num_of_sides
    #print num_of_sides
    angle=360.0/num_of_sides  # angle needed.  
    dist_traveled=0  # track the circum the turt goes
    for i in range(num_of_sides):
        turt.fd(length_of_side)
        turt.lt(angle)
        dist_traveled=dist_traveled+length_of_side
        print dist_traveled

def bubble(turt,radius):
    circ=math.pi*2*radius       #circ is circumference
    num_of_sides=math.floor(circ)  #determin number of sides. this should scale with the size of the circle
    num_of_sides=int(num_of_sides)
    length_of_side=circ/num_of_sides
    #print num_of_sides
    angle=360.0/num_of_sides  # angle needed.  
    dist_traveled=0  # track the circum the turt goes
    for i in range(num_of_sides):
        turt.fd(length_of_side)
        turt.lt(angle)
        dist_traveled=dist_traveled+length_of_side
        print dist_traveled

def gocart(rad,turt):
    for i in range (50):
        offsetdeg=random.randint(0,360)
        bubble(turt,rad)
        turt.lt(offsetdeg)
