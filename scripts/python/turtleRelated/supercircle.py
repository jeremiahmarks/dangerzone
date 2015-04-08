##from circleint import Circle
from turtle import Turtle
import fvh2
import random
import math

allcolors=['AliceBlue', 'AntiqueWhite', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'CadetBlue', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'CornflowerBlue', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'DarkGray', 'DarkGreen', 'DarkGrey', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepPink1', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'DeepSkyBlue', 'DeepSkyBlue1', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DimGray', 'DimGrey', 'DodgerBlue', 'DodgerBlue1', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'FloralWhite', 'ForestGreen', 'GhostWhite', 'Green', 'GreenYellow', 'HotPink', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'LavenderBlush', 'LavenderBlush1', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LawnGreen', 'LemonChiffon', 'LemonChiffon1', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCoral', 'LightCyan', 'LightCyan1', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'LightGoldenrod', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightGoldenrodYellow', 'LightGray', 'LightGreen', 'LightGrey', 'LightPink', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon', 'LightSalmon1', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSeaGreen', 'LightSkyBlue', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSlateBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow', 'LightYellow1', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'LimeGreen', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'MistyRose1', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'NavyBlue', 'OldLace', 'OliveDrab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'OliveDrab4', 'OrangeRed', 'OrangeRed1', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGoldenrod', 'PaleGreen', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PapayaWhip', 'PeachPuff', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'PowderBlue', 'Red', 'RosyBrown', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SaddleBrown', 'SandyBrown', 'SeaGreen', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SeaGreen4', 'SkyBlue', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SlateGrey', 'SpringGreen', 'SpringGreen1', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'WhiteSmoke', 'YellowGreen', 'alice blue', 'antique white', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2', 'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanched almond', 'blue', 'blue violet', 'blue1', 'blue2', 'blue3', 'blue4', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark green', 'dark grey', 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey', 'dodger blue', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray0', 'gray1', 'gray10', 'gray100', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40', 'gray41', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray96', 'gray97', 'gray98', 'gray99', 'green', 'green yellow', 'green1', 'green2', 'green3', 'green4', 'grey', 'grey0', 'grey1', 'grey10', 'grey100', 'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19', 'grey2', 'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28', 'grey29', 'grey3', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37', 'grey38', 'grey39', 'grey4', 'grey40', 'grey41', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47', 'grey48', 'grey49', 'grey5', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56', 'grey57', 'grey58', 'grey59', 'grey6', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65', 'grey66', 'grey67', 'grey68', 'grey69', 'grey7', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74', 'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey8', 'grey80', 'grey81', 'grey82', 'grey83', 'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey9', 'grey90', 'grey91', 'grey92', 'grey93', 'grey94', 'grey95', 'grey96', 'grey97', 'grey98', 'grey99', 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light gray', 'light green', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'navy blue', 'old lace', 'olive drab', 'orange', 'orange red', 'orange1', 'orange2', 'orange3', 'orange4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violet red', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'white smoke', 'yellow', 'yellow green', 'yellow1', 'yellow2', 'yellow3', 'yellow4']

class sTurtle(Turtle):
  
  def __init__(self):
    
    super(self.__class__,self).__init__()
    self.ht()
    self.tracer(False)
    self.speed(0)
    self.ts=self.getscreen()
    self.ts.bgcolor('DarkGray')
    self.xmin=0
    self.xmax=0
    self.ymin=0
    self.ymax=0
    
  
  def jumpto(self, point):
    self.pu()
    self.goto(point)
    
    
  def r(self):
    self.right(90)
    
  def l(self):
    self.left(90)
  
  def cleanhome(self):
    self.pu()
    self.goto(0,0)
    self.clear()
    self.seth(0)
    
  def update(self):
    self.ts.update()
  
  def extrema(self):
    currentpos=self.pos()
    if currentpos[0]<self.xmin:
      self.xmin=currentpos[0]
    if currentpos[0]>self.xmax:
      self.xmax=currentpos[0]
    if currentpos[1]<self.ymin:
      self.ymin=currentpos[1]
    if currentpos[1]>self.ymax:
      self.ymax=currentpos[1]
  
class sCircle(object):
  
  def __init__(self, point, radius, lm=None, parentCircle=None):
    self.center=point
    self.radius=radius
    if not lm:
      lm=sTurtle()
    self.lm=lm
    self.lm.pu()
    self.parent=parentCircle
    self.children=[]
    self.color='black'
    self.inittheta=0
    self.currenttheta=0
    self.deltatheta=1
    
  def turn(self):
    #self.fill()
    if not self.parent:
      self.updatecenter(self.center)
      self.lm.clear()
    for eachchild in self.children:
      self.lm.pu()
      self.lm.jumpto(self.center)
      self.lm.seth(self.currenttheta+eachchild.inittheta)
      self.lm.fd(self.radius)
      eachchild.updatecenter(self.lm.pos())
      eachchild.draw()
      eachchild.turn()
      #eachchild.tethertoparent()
    if not self.parent:
      self.draw()
      self.refresh()
      
  
  def updatecenter(self, newcenter):
    self.center=newcenter
    self.updatetheta()
  
  def setdeltatheta(self, deltatheta):
    self.deltatheta=deltatheta
  
  def updatetheta(self):
    self.currenttheta=self.currenttheta+self.deltatheta
  
  
  def setinittheta(self, startingtheta):
    self.inittheta=startingtheta
    self.currenttheta=0
    self.drawreference()
  
  def drawreference(self):
    prevsize=self.lm.pensize()
    self.lm.pensize(4)
    self.lm.jumpto(self.center)
    self.lm.pencolor(self.color)
    self.lm.seth(self.currenttheta)
    self.lm.pd()
    self.lm.fd(self.radius)
    self.lm.pu()
    self.lm.pensize(prevsize)
  
  def addchild(self, childtheta, childradius):
    self.lm.pu()
    self.lm.jumpto(self.center)
    self.lm.seth(childtheta)
    self.lm.pu()
    self.lm.fd(self.radius)
    temp=sCircle(self.lm.pos(), childradius, self.lm, self)
    temp.setinittheta(childtheta)
    temp.setdeltatheta(2*self.deltatheta)
    self.children.append(temp)
  
  def setcolor(self, color):
    self.color=color
    
  def draw(self):
    self.lm.pencolor(self.color)
    self.lm.jumpto((self.center[0],self.center[1]-self.radius))
    self.lm.pd()
    self.lm.seth(0)
    #self.lm.circle(self.radius)
    self.drawreference()
    

  def updateChildCenters(self, offset):
    for eachchild in self.children:
      self.lm.pu()
      self.lm.jumpto(self.center)
      self.lm.seth(offset+eachchild.inittheta)
      self.fd(self.center)
      eachchild.updatecenter(self.lm.pos())
  
  def drawChildren(self):
    for eachchild in self.children:
      if len(eachchild.children)>0:
        eachchild.drawChildren()
      eachchild.draw()
  
  def fill(self):
    self.lm.fillcolor(self.color)
    self.lm.pencolor(self.color)
    self.lm.jumpto((self.center[0],self.center[1]-self.radius))
    self.lm.begin_fill()
    self.lm.seth(0)
    self.lm.circle(self.radius)
    self.lm.end_fill()
    
  def refresh(self):
    self.lm.update()
  
  def tethertoparent(self):
    if self.parent:
      self.lm.jumpto(self.center)
      self.lm.pencolor(self.color)
      self.lm.pd()
      self.lm.goto(self.parent.center)
      self.lm.pu()
  
  def test(self):
    if self.radius>10:
      for x in range(0,360,180):
        self.addchild((self.inittheta)/2.0+x, self.radius/2.0)
    else:
      self.fill()
    for eachchild in self.children:
      eachchild.setcolor(random.choice(allcolors))
      eachchild.test()
      #eachchild.draw()
    self.draw()
    self.tethertoparent()
    self.refresh()
    
def colorfun():
  colors= lambda t:(t%255, (t/255)%255, (t/(255*255))%255)
  color=0
  a=sTurtle()
  b=a.getscreen()
  b.colormode(255)
  b.update()
  b.setup(300,300)
  b.screensize(260,260)

  for z in range(255):
    print z
    a.jumpto((-130,130))
    a.pd()
    a.seth(0)
    for y in range(255):
      for x in range(255):
        a.pencolor(colors(color))
        a.fd(1)
        color+=1
        
      b.update()
      a.jumpto((-130,130-y))
      a.seth(0)
      a.pd()
      if y%51==0:
        fvh2.savetocircles(a, togif=True)
        a.clear()


def bounce():
  a=sCircle((0,0),1)
  colors = lambda x : (x%255, (x/255)%255, (x/255**2)%255)
  a.draw()
  b=a.lm.getscreen()
  b.colormode(255)
  xchange=1
  ychange=1
  raw_input('waiting')
  color=0
  a.refresh()
  b.screensize(b.window_width()-30, b.window_height()-30)
  while True:
    curpos=a.center
    nextpos=[curpos[0],curpos[1]]
    if math.fabs(curpos[0])>b.canvwidth/2:
      xchange=xchange*-1
      
    if math.fabs(curpos[1])>b.canvheight/2:
      ychange=ychange*-1
      
    nextpos[0]=nextpos[0]+xchange
    nextpos[1]=nextpos[1]+ychange
    a.updatecenter((nextpos[0],nextpos[1]))
    a.setcolor(colors(color))
    color+=5
    a.draw()
    if color%100==0:
      a.refresh()
      #fvh2.savetocircles(a.lm)
      a.lm.clear()
    

def colorfuns():
  a=sTurtle()
  b=a.getscreen()
  raw_input("waiting")
  b.update()
  a.jumpto((-b.window_width()/2, b.window_height()/2))
  print a.pos()
  b.colormode(255)
  color=0
  colors = lambda x : (x%255, (x/255)%255, (x/255**2)%255)
  a.seth(0)
  a.pd()
  for x in range(b.window_height()):
    for y in range(b.window_width()):
      a.pencolor(colors(color))
      a.fd(1)
      if color%51==0:
        fvh2.savetocircles(a)
      a.clear()
      color+=1
#      print a.pos(),color
      #a.update()
    if x%2==0:
      a.r()
      a.fd(1)
      a.r()
    else:
      a.l()
      a.fd(1)
      a.l()
    a.update()

#    raw_input((a.pos(), color))
