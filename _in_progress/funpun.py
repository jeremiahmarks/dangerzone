#Exercise 15.1 Write a function called distance 
#that it takes two Points as arguments and returns
#the distance between them
# point1.x,point1.y,point2.x,point2.y=funpun.getpoints()


import math
class point(object):
    """this is a point"""

def getpoints():
#input is better fro getting integer input than raw_input anyday    
    print ('Please input x of point 1')
    x=input()
    print ('Please input y of point 1')
    y=input()
    print ('Please input x of point 2')
    a=input()
    print ('Please input y of point 2')
    b=input()
    return(x,y,a,b)


def distance(point1,point2):
    tdist=math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
    return (tdist)

def calcdistance():
    point1=point()
    point2=point()


    point1.x,point1.y,point2.x,point2.y=getpoints()

    totaldist=distance(point1,point2)

    print("The distance from ( %s,%s ) to ( %s,%s ) is %s units") % (point1.x,point1.y,point2.x,point2.y,totaldist)
