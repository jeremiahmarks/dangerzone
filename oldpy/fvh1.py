import turtle
import fvh


fred=turtle.Turtle()
def a(fred):
	for x in range(360):
		fred.pu()
		fred.goto(0,0)
		fred.pd()
		for y in range(200):
			fred.fd(y)
			fred.left(x)
