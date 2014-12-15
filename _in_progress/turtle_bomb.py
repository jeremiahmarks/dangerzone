import turtle
t=turtle.Pen()
z=turtle.Pen()
z.left(180)
t.speed(0)
z.speed(0)
t.hideturtle
z.hideturtle
for x in range (0, 3600):
    t.forward(15)
    t.left(3.25*x)
    z.forward(15)
    z.right(3.25*x)
