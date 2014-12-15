PyCrust 0.9.8 - The Flakiest Python Shell
Python 2.7.3 (default, Sep 26 2012, 21:51:14) 
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 9%3
0
>>> 9%7
2
>>> 9%4
1
>>> for x in range(20):
...     print ("7%",x,"=", 7%x)
...     print (x,"%7=", x%7)
...     
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> for x in range(1,20):
...     print ("7%",x,"=", 7%x)
...     print (x,"%7=", x%7)
...     
('7%', 1, '=', 0)
(1, '%7=', 1)
('7%', 2, '=', 1)
(2, '%7=', 2)
('7%', 3, '=', 1)
(3, '%7=', 3)
('7%', 4, '=', 3)
(4, '%7=', 4)
('7%', 5, '=', 2)
(5, '%7=', 5)
('7%', 6, '=', 1)
(6, '%7=', 6)
('7%', 7, '=', 0)
(7, '%7=', 0)
('7%', 8, '=', 7)
(8, '%7=', 1)
('7%', 9, '=', 7)
(9, '%7=', 2)
('7%', 10, '=', 7)
(10, '%7=', 3)
('7%', 11, '=', 7)
(11, '%7=', 4)
('7%', 12, '=', 7)
(12, '%7=', 5)
('7%', 13, '=', 7)
(13, '%7=', 6)
('7%', 14, '=', 7)
(14, '%7=', 0)
('7%', 15, '=', 7)
(15, '%7=', 1)
('7%', 16, '=', 7)
(16, '%7=', 2)
('7%', 17, '=', 7)
(17, '%7=', 3)
('7%', 18, '=', 7)
(18, '%7=', 4)
('7%', 19, '=', 7)
(19, '%7=', 5)
>>> 1/300
0
>>> 
... for x in range(1,1440):
...     t.forward( math. )
...     p.forward(x/3)
...     t.left(x%360)
...     p.right(x%180)
  File "<input>", line 3
    t.forward( math. )
                     ^
SyntaxError: invalid syntax
>>> import math
>>> import turtle
>>> p=turtle.Pen()
>>> p.forward(15)
>>> t=turtle.Pen()
>>> def rese():
...     p.setpos(0,0)
...     t.setpos(0,0)
...     p.clear()
...     t.clear()
...     
>>> rese
<function rese at 0x2d45cf8>
>>> rese()
>>> for x in range(1,1440):
...     t.fd(math.sin(x))
...     p.fd(math.sqrt(x))
...     t.left(math.sin(x))
...     p.rt(math.sqrt(x))
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1552, in forward
    self._go(distance)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1520, in _go
    self._goto(ende)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2990, in _goto
    screen._pointlist(self.currentLineItem),
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 760, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".46300408"
>>> t=turtle.Pen()
>>> p=turtle.Pen()
>>> for x in range(1,1440):
...     t.fd(4+math.sin(x))
...     p.fd(math.pow(x,1.25)
...     t.left(math.sin(x^2))
...     p.rt(math.sqrt(x))
  File "<input>", line 4
    t.left(math.sin(x^2))
    ^
SyntaxError: invalid syntax
>>> for x in range(1,1440):
...     t.fd(4+math.sin(x))
...     p.fd(math.pow(x,1.25)
...     t.left(math.sin(x**2))
...     p.rt(math.sqrt(x))
  File "<input>", line 4
    t.left(math.sin(x**2))
    ^
SyntaxError: invalid syntax
>>> for x in range(1,1440):
...     t.fd(4+math.sin(x))
...     p.fd(math.pow(x,1.25)
...     t.left(math.sin(math.pow(x,2)))
...     p.rt(math.sqrt(x))
  File "<input>", line 4
    t.left(math.sin(math.pow(x,2)))
    ^
SyntaxError: invalid syntax
>>> for x in range(1,1440):
...     t.fd(4+math.sin(x))
...     p.fd(math.pow(x,1.25))
...     t.left(360*math.sin(x))
...     p.rt(math.sqrt(x))
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1552, in forward
    self._go(distance)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1520, in _go
    self._goto(ende)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3010, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".55530920"
>>> p=turtle.Pen()
>>> t=turtle.Pen()
>>> for x in range(1,200):
...     t.fd(100*math.sin(x))
...     p.fd(x*0.66)
...     t.left(360*math.sin(x))
...     p.rt(math.sqrt(x))
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".54322384"
>>> t=turtle.Pen()
>>> p=turtle.Pen()
>>> for x in range(1,100):
...     t.fd(x%20)
...     p.fd(x%(x*0.66))
...     t.left(x%45)
...     p.rt(x%75)
...     
>>> dele()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'dele' is not defined
>>> rese()
>>> for x in range(1,360):
...     t.fd(x%20)
...     p.fd(x%75)
...     t.left(x%180)
...     p.rt(x%90)
...     
>>> rese()
>>> for x in range(1,360):
...     t.fd(x%20)
...     p.fd(x%30)
...     t.left(x%45)
...     p.rt(x%90)
...     
>>> rese()
>>> t.up()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%30)
...     #t.left(x%45)
...     p.rt(x%90)
...     
>>> rese()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%45)
...     #t.left(x%45)
...     p.rt(x%90)
...     
>>> rese()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%45)
...     
>>> rese()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%30)
...     
>>> p.up()
>>> p.heading()
165.0
>>> turtle.left(165)
>>> rese()
>>> p.fd(15)
>>> p.down
<bound method Turtle.pendown of <turtle.Turtle object at 0x34fa2d0>>
>>> p.down()
>>> p.fd(15)
>>> p.heading()
165.0
>>> p.left(165)
>>> p.heading()
330.0
>>> p.left(30)
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%30)
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1552, in forward
    self._go(distance)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1520, in _go
    self._goto(ende)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3010, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".55531496"
>>> p=turtle.Pen()
>>> p.goto(100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1689, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be a sequence, not int
>>> p.goto(100,100)
>>> p.setpos(-100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1689, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be a sequence, not int
>>> p.setpos(-100,100)
>>> p.setpos(-500,100)
>>> p.circle(10)
>>> p.setpos(-800,100)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%30)
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".52112992"
>>> p=turtle.Pen()
>>> p.setpos(-800,0)
>>> p.seth(180)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%30)
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".47517992"
>>> p=turtle.Pen()
>>> p.setpos(-800,-400)
>>> p.setpos(-800,-200)
>>> p.seth(180)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%90)
...     #t.left(x%45)
...     p.rt(x%30)
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%90))
...     #t.left(x%45)
...     p.rt(x%60)
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".52111552"
>>> p=turtle.Pen()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%90))
...     #t.left(x%45)
...     p.rt(x%60)
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3110, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".58588552"
>>> p=turtle.Pen()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%90))
...     #t.left(x%45)
...     p.rt(x%90)
...     
>>> rese
<function rese at 0x2d45cf8>
>>> rese()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 3, in rese
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1691, in goto
    self._goto(Vec2D(x, y))
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2990, in _goto
    screen._pointlist(self.currentLineItem),
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 760, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".55531496"
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%60))
...     #t.left(x%45)
...     p.rt(x%120)
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x+(x%60))
...     #t.left(x%45)
...     p.rt(x+(x%120))
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".58585240"
>>> p=turtle.Pen()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%30)+(x%60))
...     #t.left(x%45)
...     p.rt((x%60)+(x%120))
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%40)+(x%17))
...     #t.left(x%45)
...     p.rt((x%42)+(x%28))
...     p.pensize(x%15)
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".66977944"
>>> p=turtle.Pen()
>>> p.pensize(10)
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%40)+(x%17))
...     #t.left(x%45)
...     p.rt((x%42)+(x%28))
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".52110112"
>>> p=turtle.Pen()
>>> p.pensize(5)
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%45)+(x%90))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1593, in right
    self._rotate(-angle)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3108, in _rotate
    self._update()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2564, in _update
    self._update_data()
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 2555, in _update_data
    self._pencolor, self._pensize)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".57736584"
>>> p=turtle.Pen()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd((x%45)+(x%90))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(5*((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1552, in forward
    self._go(distance)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 1520, in _go
    self._goto(ende)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 3010, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python2.7/lib-tk/turtle.py", line 569, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 2205, in coords
    self.tk.call((self._w, 'coords') + args)))
TclError: invalid command name ".47600056"
>>> p=turtle.Pen()
>>> p.speed(0)
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(5*((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(3*((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x+3*((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.clear()
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x+((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%((x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%(1+(x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt((x%30)+(x%90))
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     #t.fd(x%20)
...     p.fd(x%(1+(x%45)+(x%90)))
...     #t.left(x%45)
...     p.rt(x%360)
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     p.fd(x%45)
...     p.rt(x%360)
...     
>>> for x in range(1,720):
...     p.fd(x%60)
...     p.rt(x%360)
...     
>>> p.clear()
>>> p.setpos(0,0)
>>> for x in range(1,720):
...     p.fd(x%110)
...     p.rt(x%360)
...     
>>> p.clear()
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,1440):
...     p.fd(x%110)
...     p.rt(x%360)
...     
>>> p.clear()
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,1440):
...     p.fd(x%15)
...     p.rt(x%360)
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,1440):
...     p.fd(x)
...     p.rt(x%360)
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     p.fd(math.sin(x))
...     p.rt(x%360)
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,720):
...     p.fd((x%10)*math.sin(x))
...     p.rt(x%110)
...     
>>> p.setpos(0,0)
>>> p.clear()
>>> for x in range(1,1440):
...     p.fd((x%10)*math.sin(x))
...     p.rt(x%110)
...     
>>> for x in range(1,1440):
...     p.fd(2*((x%10)*math.sin(x)))
...     p.rt(x%110)
...     
>>> 
