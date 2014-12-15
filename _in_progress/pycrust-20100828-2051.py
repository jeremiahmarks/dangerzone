PyCrust 0.9.5 - The Flakiest Python Shell
Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import funpun
>>> point1=point()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'point' is not defined
>>> from funpun import point
>>> point1=point()
>>> point2,point3=point()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'point' object is not iterable
>>> point2=point()
>>> point1.x,point1.y=2,3
>>> point1.x
2
>>> point1.x,point1.y,point2.x,point2.y=funpun.getpoints()
Please input x of point 1
<-- 4
Please input y of point 1
<-- 5
Please input x of point 2
<-- 2
Please input y of point 2
<-- 4
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: need more than 2 values to unpack
>>> point1.x,point1.y,point2.x,point2.y=funpun.getpoints()
Please input x of point 1
<-- 7
Please input y of point 1
<-- 6
Please input x of point 2
<-- 9
Please input y of point 2
<-- 4
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: need more than 2 values to unpack
>>> reload(funpun)
<module 'funpun' from 'funpun.py'>
>>> point1.x,point1.y,point2.x,point2.y=funpun.getpoints()
Please input x of point 1
<-- 7
Please input y of point 1
<-- 5
Please input x of point 2
<-- 5
Please input y of point 2
<-- 5
>>> point2.x
'5'
>>> reload(funpun)
<module 'funpun' from 'funpun.py'>
>>> distance(point1,point2)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'distance' is not defined
>>> funpun.distance(point1,point2)
75
>>> reload(funpun)
<module 'funpun' from 'funpun.py'>
>>> funpun.distance(point1,point2)
<funpun.point object at 0xb579364c>
<funpun.point object at 0xb578e9cc>
7
75
>>> point1.x+point1.y
'75'
>>> point1.x
'7'
>>> point1.y
'5'
>>> int(point1.x)
7
>>> 