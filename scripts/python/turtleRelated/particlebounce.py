from supercircle import sTurtle, sCircle
import fvh2
import random
import math
import time

allcolors=['AliceBlue', 'AntiqueWhite', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'CadetBlue', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'CornflowerBlue', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'DarkGray', 'DarkGreen', 'DarkGrey', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepPink1', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'DeepSkyBlue', 'DeepSkyBlue1', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DimGray', 'DimGrey', 'DodgerBlue', 'DodgerBlue1', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'FloralWhite', 'ForestGreen', 'GhostWhite', 'Green', 'GreenYellow', 'HotPink', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'LavenderBlush', 'LavenderBlush1', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LawnGreen', 'LemonChiffon', 'LemonChiffon1', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCoral', 'LightCyan', 'LightCyan1', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'LightGoldenrod', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightGoldenrodYellow', 'LightGray', 'LightGreen', 'LightGrey', 'LightPink', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon', 'LightSalmon1', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSeaGreen', 'LightSkyBlue', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSlateBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow', 'LightYellow1', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'LimeGreen', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'MistyRose1', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'NavyBlue', 'OldLace', 'OliveDrab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'OliveDrab4', 'OrangeRed', 'OrangeRed1', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGoldenrod', 'PaleGreen', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PapayaWhip', 'PeachPuff', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'PowderBlue', 'Red', 'RosyBrown', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SaddleBrown', 'SandyBrown', 'SeaGreen', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SeaGreen4', 'SkyBlue', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SlateGrey', 'SpringGreen', 'SpringGreen1', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'WhiteSmoke', 'YellowGreen', 'alice blue', 'antique white', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2', 'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanched almond', 'blue', 'blue violet', 'blue1', 'blue2', 'blue3', 'blue4', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark green', 'dark grey', 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey', 'dodger blue', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray0', 'gray1', 'gray10', 'gray100', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40', 'gray41', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray96', 'gray97', 'gray98', 'gray99', 'green', 'green yellow', 'green1', 'green2', 'green3', 'green4', 'grey', 'grey0', 'grey1', 'grey10', 'grey100', 'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19', 'grey2', 'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28', 'grey29', 'grey3', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37', 'grey38', 'grey39', 'grey4', 'grey40', 'grey41', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47', 'grey48', 'grey49', 'grey5', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56', 'grey57', 'grey58', 'grey59', 'grey6', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65', 'grey66', 'grey67', 'grey68', 'grey69', 'grey7', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74', 'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey8', 'grey80', 'grey81', 'grey82', 'grey83', 'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey9', 'grey90', 'grey91', 'grey92', 'grey93', 'grey94', 'grey95', 'grey96', 'grey97', 'grey98', 'grey99', 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light gray', 'light green', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'navy blue', 'old lace', 'olive drab', 'orange', 'orange red', 'orange1', 'orange2', 'orange3', 'orange4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violet red', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'white smoke', 'yellow', 'yellow green', 'yellow1', 'yellow2', 'yellow3', 'yellow4']

BLOCKWIDTH=20
BLOCKHEIGHT=20
PARTICLES=0
COUNTER=0

class particle(object):
  """
  This class is to emulate a particle as it moves about a field
  """
  
  def __init__(self):
    global PARTICLES
    PARTICLES+=1
    print PARTICLES
    self.writer=sTurtle()
    self.xdirection=1
    self.ydirection=1
    #self.isin=False
    self.Boxesin=[]
    self.writer.tracer(False)
    self.writer.pensize(5)
    #self.pos=self.writer.pos()
    

  
  
  def clone(self):
    newpart=particle()
    newpart.writer.pu()
    newpart.writer.goto(self.writer.pos())
    newpart.writer.pd()
    newpart.xdirection=self.xdirection
    newpart.ydirection=self.ydirection
    for box in self.Boxesin:
      newpart.Boxesin.append(box)
    return newpart
  

  def color(self,strColor):
    self.writer.color(strColor)
    
    
class circleparticle(object):
  """
  This class is to emulate a particle as it moves about a field
  """
  
  def __init__(self):
    global PARTICLES
    PARTICLES+=1
    self.writer=sCircle((0,0),3)
    self.xdirection=5
    self.ydirection=5
    #self.isin=False
    self.Boxesin=[]
    #self.pos=self.writer.pos()
    

  
  
  def clone(self):
    newpart=circleparticle()
    newpart.writer.updatecenter(self.writer.center)
    newpart.xdirection=self.xdirection
    newpart.ydirection=self.ydirection
    for box in self.Boxesin:
      newpart.Boxesin.append(box)
    return newpart
    
  def color(self,strColor):
    self.writer.setcolor(strColor)
  
    
class bounceBoard(object):
  """  
  def __init__(self):
    self.particles=[]
    self.blocks=[]
    firstparticle=particle()
    self.board=firstparticle.writer.getscreen()
    self.board.setup(500,250,0.0,0.0)
    self.board.screensize(450,200)
    for x in range(10,self.board.canvwidth,20):
      thiscol=[]
      for y in range(10,self.board.canvheight,20):
        thiscol.append(boardBlock(-(self.board.canvwidth/2.0)+x,-(self.board.canvheight/2.0)+y ))
      self.blocks.append(thiscol)
    for eachblock in self.blocks[0]:
      eachblock.writer.color('black','black')
    for eachrow in self.blocks:
      eachrow[0].writer.color('black','black')
      eachrow[len(eachrow)-1].writer.color('black','black')
    for eachblock in self.blocks[len(self.blocks)-1]:
      eachblock.writer.color('black','black')
    
  """
  def __init__(self):
    self.particles=[]
    self.blocks=[]
    firstparticle=particle()
    firstparticle.writer.pu()
    firstparticle.writer.goto(100,75)
    firstparticle.writer.pd()
    firstparticle.writer.color('red')
    self.board=firstparticle.writer.getscreen()
    self.board.setup(500,250,0.0,0.0)
    self.board.screensize(450,200)
    self.particles.append(firstparticle)
    
  def addBlock(self, centerofnewblock):
    self.blocks.append(boardBlock(centerofnewblock[0],centerofnewblock[1]))
  
  def ani(self):
    global COUNTER
    COUNTER+=1
    newparts=[]
    #self.board.update()
    self.board.screensize(self.board.window_width()-30,self.board.window_height()-30)
    for part in self.particles:
      #part.writer.clear()
      for block in self.blocks:
        blockisin=block in part.Boxesin
        if blockisin and not block.checkifin(part.writer.pos()):
          part.Boxesin.remove(block)
          
        elif not blockisin and block.checkifin(part.writer.pos()):
          part.Boxesin.append(block)
          if PARTICLES<50:
            newparts.append(block.isin(part))
          else:
            block.isin()
          
      curpos=part.writer.pos()
      
      if curpos[0]>self.board.canvwidth/2:
        part.xdirection=-random.randint(1,15)
      if curpos[0]<-self.board.canvwidth/2:
        part.xdirection=random.randint(1,15)
      if curpos[1]>self.board.canvheight/2:
        part.ydirection=-random.randint(1,15)
      if curpos[1]<-self.board.canvheight/2:
        part.ydirection=random.randint(1,15)
      nextpos=[curpos[0]+part.xdirection,curpos[1]+part.ydirection]
      part.writer.goto((nextpos[0],nextpos[1]))
      #part.writer.update()
    for newpart in newparts:
      self.particles.append(newpart)
    if COUNTER%100==0:
      for box in self.blocks:
        box.writer.color('','')
      fvh2.savetocircles(self.particles[0].writer, togif=True)
      for box in self.blocks:
        box.writer.undo()
      self.board.update()
      
class circlebounceBoard(object):
  """  
  def __init__(self):
    self.particles=[]
    self.blocks=[]
    firstparticle=particle()
    self.board=firstparticle.writer.getscreen()
    self.board.setup(500,250,0.0,0.0)
    self.board.screensize(450,200)
    for x in range(10,self.board.canvwidth,20):
      thiscol=[]
      for y in range(10,self.board.canvheight,20):
        thiscol.append(boardBlock(-(self.board.canvwidth/2.0)+x,-(self.board.canvheight/2.0)+y ))
      self.blocks.append(thiscol)
    for eachblock in self.blocks[0]:
      eachblock.writer.color('black','black')
    for eachrow in self.blocks:
      eachrow[0].writer.color('black','black')
      eachrow[len(eachrow)-1].writer.color('black','black')
    for eachblock in self.blocks[len(self.blocks)-1]:
      eachblock.writer.color('black','black')
    
  """
  def __init__(self):
    
    self.particles=[]
    self.blocks=[]
    firstparticle=circleparticle()
    firstparticle.writer.draw()
    
    self.board=firstparticle.writer.lm.getscreen()
    self.board.setup(500,250,0.0,0.0)
    self.board.screensize(450,200)
    #self.board.colormode(255)
    self.particles.append(firstparticle)
    
  def addBlock(self, centerofnewblock):
    self.blocks.append(boardBlock(centerofnewblock[0],centerofnewblock[1]))
  
  def ani(self):
    newparts=[]
    self.board.update()
    self.board.screensize(self.board.window_width()-30,self.board.window_height()-30)
    for part in self.particles:
      #part.writer.lm.clear()
      for block in self.blocks:
        blockisin=block in part.Boxesin
        if blockisin and not block.checkifin(part.writer.center):
          part.Boxesin.remove(block)
          
        elif not blockisin and block.checkifin(part.writer.center):
          part.Boxesin.append(block)
          if PARTICLES<10:
            newparts.append(block.isin(part))
          else:
            block.isin()
          
          
      curpos=part.writer.center
      
      if curpos[0]>self.board.canvwidth/2:
        part.xdirection=-random.randint(1,15)
      if curpos[0]<-self.board.canvwidth/2:
        part.xdirection=random.randint(1,15)
      if curpos[1]>self.board.canvheight/2:
        part.ydirection=-random.randint(1,15)
      if curpos[1]<-self.board.canvheight/2:
        part.ydirection=random.randint(1,15)
      nextpos=[curpos[0]+part.xdirection,curpos[1]+part.ydirection]
      part.writer.updatecenter((nextpos[0],nextpos[1]))
      part.writer.draw()
    for newpart in newparts:
      self.particles.append(newpart)

class boardBlock(object):

  TYPES=['field', 'border', 'exterior']
  
  def __init__(self,centerx,centery):
    self.writer=sTurtle()
    #self.boxtype=TYPES[0]
    self.startx=centerx-(BLOCKWIDTH/2.0)
    self.starty=centery-(BLOCKHEIGHT/2.0)
    self.endx=self.startx+BLOCKWIDTH
    self.endy=self.starty+BLOCKHEIGHT
    self.writer.jumpto((centerx,centery))
    self.writer.shape('square')
    self.writer.shapesize(BLOCKWIDTH/20.0, BLOCKHEIGHT/20.0,0)
    self.writer.st()
    self.writer.color('black','')
    self.writer.tracer(True)
    
  def checkifin(self,position):
    xpos, ypos = position[0], position[1]
    if (self.startx<xpos and xpos<self.endx and self.starty<ypos and ypos<self.endy):
      return True
    else:
      return False
  
  def isin(self,aparticle=None):
    self.writer.color(random.choice(allcolors),random.choice(allcolors))
    if aparticle:
      aparticle.Boxesin.append(self)
      a=aparticle.clone()
      a.xdirection=a.xdirection*random.choice([-1,1])
      a.ydirection=a.ydirection*random.choice([-1,1])
      a.color(random.choice(allcolors))
      return a
  

class colorBoard(object):
  
  def __init__(self):
    self.particles=[]
    self.blocks=[]
    firstparticle=particle()
    self.board=firstparticle.writer.getscreen()
    raw_input('waiting for resize')
    self.board.update()
    self.board.screensize(self.board.window_width()-30,self.board.window_height()-30)
    for x in range(0,255):
      thiscol=[]
#      for y in range(10,self.board.canvheight,20):
      for y in range(0,255):
        xoffset=x*(self.board.canvwidth/255.0)
        yoffset=y*(self.board.canvheight/255.0)
        thiscol.append(boardBlock(-(self.board.canvwidth/2.0)+xoffset,-(self.board.canvheight/2.0)+yoffset ))
      self.blocks.append(thiscol)
    for eachblock in self.blocks[0]:
      eachblock.writer.color('black','black')
    for eachrow in self.blocks:
      eachrow[0].writer.color('black','black')
      eachrow[len(eachrow)-1].writer.color('black','black')
    for eachblock in self.blocks[len(self.blocks)-1]:
      eachblock.writer.color('black','black')
    self.board.colormode(255)

    
def funwithcolors():
  colors = lambda x : (x%255, (x/255)%255, (x/255**2)%255)
  a=colorBoard()
  b=0
  while b<255**3:
    for col in a.blocks:
      for block in col:
        
        c=colors(b)
        block.writer.color(c,c)
        b+=1
    fvh2.savetocircles(block.writer, togif=True, topng=True)