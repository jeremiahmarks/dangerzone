#The Joy of Turtles
import turtle

t=turtle.Pen()

def drawone(loops, distance, angle):
    for loop in range(loops):
        t.fd(loop%distance)
        t.rt(loop%angle)
        
def cleanup():
    t.setpos(0,0)
    t.clear()

def cleanMove(xval, yval):
    t.up()
    t.setpos(xval, yval)
    t.down()
    
#def drawtwo(
#use lamdas/generators as the length and turn 
