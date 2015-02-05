import supercircle
import fvh2

def square(size, bottomleftcorner, startangle=0, turt=None):
  if not turt:
    turt=supercircle.sTurtle()
  turt.jumpto(bottomleftcorner)
  turt.seth(startangle)
  turt.pd()
  for x in range(4):
    turt.fd(size)
    turt.l()
  turt.update()
