
import math
import supercircle

FIELD_WIDTH=400
FIELD_HEIGHT=200

class pongField(object):
  self.playball=supercircle.sCircle((0,0),15)
  self.playfield=self.playball.getscreen()
  self.playfield.screensize(FIELD_WIDTH, FIELD_HEIGHT)
  self.playfield.setup(FIELD_WIDTH+50, FIELD_HEIGHT+50)
  
  
class paddle(object):
  self.  
