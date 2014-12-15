"""
This module is designed to provide the various scripts neccessary to solve the 
problems from "Chapter 2 Motion in One Dimension" from Serway/Jewett Physics for
Scientists and Engineers 8e book.
"""

accelDueToGravity=9.8

def q2(initialSpeed, targetDownwardSpeed):
  """
  An arrow is shot straight up in the air at an initial speed of 15.0 m/s. After
  how much time is the arrow movind downard at a speed of 8.00 m/s?
  """
  positioneq = lambda x : initialSpeed*x-9.8*x
