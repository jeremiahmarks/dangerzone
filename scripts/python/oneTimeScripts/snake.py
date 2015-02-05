import turtle
import random
import time

COLUMNS=100
ROWS=100
BLOCKWIDTH=20

class SnakeBoard(object):
  
  def __init__(self, cols, rows):
    self.cols, self.rows = cols.rows
    self.screen=turtle.Screen()
    self.screen.screensize(BLOCKWIDTH*cols-50, BLOCKWIDTH*rows-50)
    self.screen.setup(BLOCKWIDTH*cols+12, BLOCKWIDTH*rows+12)
    self.screen.title('Snake by Turtle')
    self.screen.bgcolor('black')
    self.writer= Turtle()
    self.writer.ht()
    self.label = None
    self.grid={}
    self.screen.tracer(False)
    for row in range(rows):
      for col in range(cols):
        self.grid[col,row]= SnakeField(col,row)
    self.screen.tracer(True)
    self.brick=Snake(self)
    self.result=0
    self.LEVEL=0.6
    self.keybuffer = KeyBuffer(self.screen, ['Right', 'Left', 'Up', 'Down'])
    self.reset()
    self.screen.listen()
    self.t1=time.time()
    
  def reset(self):
    self.result=0
    self.level=0.6
    self.screen.tracer(False)
    self.writer.clear()
    if self.label:
      self.writer.clearstamp(self.label)
    for x in range(COLUMNS):
      for y in range(ROWS):
        self.grid[(x,y)].fillcolor("")
    self.screen.tracer(True)
    self.state = "NEWFOOD"
    
    
class KeyBuffer(object):
  def __init__(self, board, used_keys):
    self.board = board
    for key in used_keys:
      self.board.onkey(lambda x=key: self.add(x), key)
    self.buffer = []
  def add(self, key):
    self.buffer.append(key)
  def getkey(self):
    if self.buffer:
      return self.buffer.pop(0)
    else:
      return None

class SnakeField(Turtle):
  def __init__(self, col, row):
    Turtle.__init__(self)
    self.speed(0)
    self.pu()
    self.shape("square")
    self.color("black", "")
    self.shapesize((BLOCKWIDTH-1)/20., (BLOCKWIDTH-1)/20., 1)
    self.goto(-COLUMNS*BLOCKWIDTH/2+14+col*BLOCKWIDTH, ROWS*BLOCKWIDTH/2 - 14 - row*BLOCKWIDTH)

