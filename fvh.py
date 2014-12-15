###############################################
#Author: Jeremiah Marks
#Email: jeremiah@jlmarks.org
#
# This script uses the tkinter turtle module to 
# draw various patterns. 
# 
# It also uses inheritance and modifies the original
# Turtle class to add some basic functionality such
# as jumping without leaving a trace, sending the turtle
# back to the origin without leaving a mark, and 
# returning the turtle to the origin and cleaning
# the canvas to its blank state. 

# triala() loosely draws a figure 8 shape, trialb() draws a pretty 
# series of slightly off center squares, and trialc() draws different
# shapes depending on what angle is used as a variable. (75 results in
# an interesting spiral formation, 90 results in a solid square, and
# 165 results in 24 pointed star. 


allcolors=['AliceBlue', 'AntiqueWhite', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'CadetBlue', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'CornflowerBlue', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'DarkGray', 'DarkGreen', 'DarkGrey', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepPink1', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'DeepSkyBlue', 'DeepSkyBlue1', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DimGray', 'DimGrey', 'DodgerBlue', 'DodgerBlue1', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'FloralWhite', 'ForestGreen', 'GhostWhite', 'Green', 'GreenYellow', 'HotPink', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'LavenderBlush', 'LavenderBlush1', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LawnGreen', 'LemonChiffon', 'LemonChiffon1', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCoral', 'LightCyan', 'LightCyan1', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'LightGoldenrod', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightGoldenrodYellow', 'LightGray', 'LightGreen', 'LightGrey', 'LightPink', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon', 'LightSalmon1', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSeaGreen', 'LightSkyBlue', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSlateBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow', 'LightYellow1', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'LimeGreen', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'MistyRose1', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'NavyBlue', 'OldLace', 'OliveDrab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'OliveDrab4', 'OrangeRed', 'OrangeRed1', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGoldenrod', 'PaleGreen', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PapayaWhip', 'PeachPuff', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'PowderBlue', 'Red', 'RosyBrown', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SaddleBrown', 'SandyBrown', 'SeaGreen', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SeaGreen4', 'SkyBlue', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SlateGrey', 'SpringGreen', 'SpringGreen1', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'WhiteSmoke', 'YellowGreen', 'alice blue', 'antique white', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2', 'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanched almond', 'blue', 'blue violet', 'blue1', 'blue2', 'blue3', 'blue4', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark green', 'dark grey', 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey', 'dodger blue', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray0', 'gray1', 'gray10', 'gray100', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40', 'gray41', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray96', 'gray97', 'gray98', 'gray99', 'green', 'green yellow', 'green1', 'green2', 'green3', 'green4', 'grey', 'grey0', 'grey1', 'grey10', 'grey100', 'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19', 'grey2', 'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28', 'grey29', 'grey3', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37', 'grey38', 'grey39', 'grey4', 'grey40', 'grey41', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47', 'grey48', 'grey49', 'grey5', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56', 'grey57', 'grey58', 'grey59', 'grey6', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65', 'grey66', 'grey67', 'grey68', 'grey69', 'grey7', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74', 'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey8', 'grey80', 'grey81', 'grey82', 'grey83', 'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey9', 'grey90', 'grey91', 'grey92', 'grey93', 'grey94', 'grey95', 'grey96', 'grey97', 'grey98', 'grey99', 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light gray', 'light green', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'navy blue', 'old lace', 'olive drab', 'orange', 'orange red', 'orange1', 'orange2', 'orange3', 'orange4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violet red', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'white smoke', 'yellow', 'yellow green', 'yellow1', 'yellow2', 'yellow3', 'yellow4']
somecolors=['Blue','Red','White']
from turtle import Turtle
import random
import datetime
from wand.image import Image
import fvhmans



class MyTurtle(Turtle):
    """
    This function uses Turtle as a parent function and adds a 
    jump, gohome, and clean home method to the default methods. 
    
    Jump will retract the turtles pen, move it 'distance' 
    units in the direction it is facing, and then put its 
    pen back on the ground.
    
    gohome simply jumps the turtle home
    
    clean home jumps the turtle home and then cleans up its tracks
    
    """
    #Turtle.speed(0)

    #def __init__(self):
    #    self.setup()
    #    lm=Turtle()
    #    lm.speed(0)
    #    lm.ht()
    #    return lm
        
    def setup(self):
        self.ht()
        self.speed(0)
        
    def jump(self, distance):
        self.pu()
        self.forward(distance)
        self.pd()
        
    def gohome(self):
        self.pu()
        self.goto(0,0)
        self.pd()
        
    def cleanhome(self):
        self.gohome()
        self.clear()
        
    #Turtle.speed(0)
    #Turtle.ht()

def coolercirclesaa():
  import math
  lm=MyTurtle()
  
  lm.ht()
  lm.speed(0)
  numofpoints=25
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(250)
    pointmap[point]=lm.position()
  for apoint in range (numofpoints):
    lm.gohome()
    lm.setheading(apoint*degperpt)
    lm.pu()
    lm.fd(500)
    pointmap[numofpoints+apoint]=lm.position()
  for start in range(0,len(pointmap)):
    for end in range(start+1,len(pointmap)):
      lm.goto(pointmap[start])
      lm.seth(lm.towards(pointmap[end]))
      lm.bk(800)
      lm.pd()
      lm.goto(pointmap[end])
      lm.fd(800)
      lm.pu()


def triala():
    fred = MyTurtle()
    herb=MyTurtle()
    for x in range (2, 180):
        fred.forward(x)
        fred.right(x)
        herb.forward(x)
        herb.left(x)

def trialb():
    a=MyTurtle()
    a.speed(0)
    for x in range (2, 3000):
        a.forward(x%100)
        a.right(91.5)
        
    turts.cleanhome()
    turts.speed(0)
    for it in range(1,6000):
        turts.fd(it/2+3)
        turts.left(angle)

def trialc2(truts, angle, revolutions):
    pass
  

        
def triald(angle):
    mover=MyTurtle()
    mover.speed(0)
    mover.setup()
    mover.tracer(False)
    printer=MyTurtle()
    printer.setup()
    ts=MyTurtle.getscreen(mover)
    ts.screensize(1600,1600)
    printer.ht()
    printer.penup()
    printer.goto(0,200)
    printer.pendown()
    for val in range(1000):
        #printer.clear()
        #printer.write(val)
        mover.fd(val)
        mover.left(angle)
    mover.tracer(True)
    fvhmans.savetocircles(printer, togif=True)
    #ts.getcanvas().postscript(file="turtle/"+str(angle)+".eps")
    #ts.bye()
    
def prettyDraw():
  leftpoints=((-75, 75), (-75, 0), (-75,-75))
  rightpoints=((75,75), (75, 60), (75,45), (75,30), (75,15), (75,0), (75,-15), (75, -30), (75, -45), (75,-60), (75, -75))
  
  mover=MyTurtle()
  mover.speed(0)
  ts=MyTurtle.getscreen(mover)
  ts.screensize(150,150)
  for leftpoint in leftpoints:
    
    for rightpoint in rightpoints:
      mover.jumpto(leftpoint)
      mover.goto(rightpoint)
  
def pdraw(numOfLPoints,numOfRPoints):
  
  mover=MyTurtle()
  mover.speed(0)
  ts=MyTurtle.getscreen(mover)
  ts.screensize(600,600)
  thesize=ts.screensize()
  vBars=thesize[0]/2
  hBars=thesize[1]/2
  leftstep=thesize[0]/numOfLPoints
  rightstep=thesize[1]/numOfRPoints
  for x in range(-vBars, vBars, leftstep):
    for y in range (-hBars, hBars, rightstep):
      #print str(-hBars)+ ","+str(y)+" TO: "+str(hBars)+","+str(x)
      mover.pu()
      mover.goto((-hBars,-x))
      mover.pd()
      mover.goto((hBars,y))
      
def triale(angle):
    mover=MyTurtle()
    mover.speed(0)
    printer=MyTurtle()
    ts=MyTurtle.getscreen(mover)
    ts.screensize(1600,1600)
    printer.ht()
    printer.penup()
    printer.goto(0,200)
    printer.pendown()
    for val in range(200):
        printer.clear()
        printer.write(val)
        mover.fd(val%100)
        mover.left(angle)
    printer.clear()
    #ts.getcanvas().postscript(file="turtle/"+str(angle)+".eps")
    ts.bye()
    
def trialf(angle, turt):
    mover=turt
    mover.cleanhome()
    mover.setheading(0)
    for val in range(800):
        mover.fd(val)
        mover.left(angle)

def trialf(angle, turt, finallength):
    mover=turt
    mover.cleanhome()
    mover.setheading(0)
    for val in range(finallength):
        mover.fd(val)
        mover.left(angle)    
    
def dotrialf():
  frank=MyTurtle()
  frank.speed(0)
  frank.ht()
  frank.tracer(False)
  ts=MyTurtle.getscreen(frank)
  ts.screensize(300,300)
  ts.setup(350,350)
  for angle in range(0,3600):
    realangle=angle/10.0
    trialf(realangle, frank)
    ts.update()
    afilename="turtle/real/"+'%05d' % angle+".eps"
    ts.getcanvas().postscript(file=afilename)
    with Image(filename=afilename) as img:
        with img.convert('gif') as newimg:
            newfilename=afilename[:-3]+'.gif'
            newimg.save(filename=newfilename)
    print '%05d' % angle +": Done!"
  ts.bye()

def adotrialf(screensize, iterationsperangle):
  frank=MyTurtle()
  frank.speed(0)
  frank.ht()
  frank.tracer(False)
  ts=MyTurtle.getscreen(frank)
  ts.screensize(screensize, screensize)
  ts.setup(screensize+50,screensize+50)
  for angle in range(0,36000,25):
    realangle=angle/100.0
    trialf(realangle, frank, iterationsperangle)
    ts.update()
    afilename="turtle/real/"+'%05d' % angle+".eps"
    ts.getcanvas().postscript(file=afilename, height=screensize, width=screensize, x=-(screensize/2), y=-(screensize/2))
    with Image(filename=afilename) as img:
        with img.convert('gif') as newimg:
            newfilename=afilename[:-3]+'gif'
            newimg.save(filename=newfilename)
    print '%05d' % angle +": Done!"
  ts.bye()

    
def clockcharsa(colors):
  a=MyTurtle()
  a.speed(0)
  #a.ht()
  a.getscreen().colormode(255)
  numofchars=126
  degreesperchar=360.0/len(colors)
  for chars in range(len(colors)):
    print chars
    a.gohome()
    a.setheading(chars*degreesperchar)
    a.pencolor(colors.pop())
    a.fd(200)
    #a.write(chr(chars))
    
def clockchars():
  a=MyTurtle()
  a.speed(0)
  a.ht()
  a.getscreen().colormode(255)
  numofchars=126
  degreesperchar=360.0/numofchars
  for chars in range(numofchars):
    a.gohome()
    a.setheading(chars*degreesperchar)
    a.penup()
    a.fd(200)
    a.write(chr(chars))
    
def colorTuples():
    a=[]
    for x in range(255):
        for y in range(255):
            for z in range(255):
                a.append((x,y,z))
    return a
    
    
def clockcharsb():
  writer=MyTurtle()
  writer.speed(0)
  writer.ht()
  numofchars=126
  degreesperchar=360.0/numofchars
  charmap={}
  for chars in range(numofchars):
    writer.gohome()
    writer.setheading(chars*degreesperchar)
    writer.penup()
    writer.fd(300)
    charmap[chr(chars)]=writer.position()
    writer.fd(30)
    writer.write(chr(chars))
    
  return charmap
  
def doclockcharsb(astring):
  linemaker=MyTurtle()
  linemaker.speed(0)
  linemaker.ht()
  linemaker.penup()
  charmap=clockcharsb()
  for eachchar in range(len(astring)-1):
    linemaker.penup()
    linemaker.pencolor(random.choice(allcolors))
    linemaker.goto(charmap[astring[eachchar]])
    linemaker.pd()
    linemaker.goto(charmap[astring[eachchar+1]])
    
    
def coolcircles():
  import math
  lm=MyTurtle()
  
  lm.ht()
  lm.speed(0)
  numofpoints=55
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(200)
    pointmap[point]=lm.position()
  for start in range(0,numofpoints,int(math.sqrt(numofpoints))):
    for end in range(numofpoints):
      lm.goto(pointmap[start])
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      print start, end

def coolercircles():
  import math
  lm=MyTurtle()
  
  lm.ht()
  lm.speed(0)
  numofpoints=55
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(800)
    pointmap[point]=lm.position()
  for start in range(0,numofpoints):
    for end in range(start,numofpoints):
      lm.goto(pointmap[start])
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      print start, end


def coolercircles():
  import math
  lm=MyTurtle()
  
  lm.ht()
  lm.speed(0)
  numofpoints=55
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(800)
    pointmap[point]=lm.position()
  for start in range(0,numofpoints):
    for end in range(start,numofpoints):
      lm.goto(pointmap[start])
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      print start, end

def coolestcircles(numofpoints, circlewidth, firststep=1, secondstep=1):
  lm=MyTurtle()
  lm.ht()
  lm.speed(0)
  ts=lm.getscreen()
  ts.screensize(1000,1000)
  ts.setup(1050,1050)
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(circlewidth)
    pointmap[point]=lm.position()
  for start in range(0,numofpoints,firststep):
    for end in range(start,numofpoints,secondstep):
      lm.goto(pointmap[start])
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      print 
  ts.getcanvas().postscript(file="circles/"+datetime.datetime.now().strftime('%b-%d-%I%M%S%p-%G')+".eps")
  lm.reset()

def coolcirclesa(numofpoints,circlesize,stepsize):
  import math
  lm=MyTurtle()
  ts=lm.getscreen()
  ts.bgcolor('gray50')
  lm.ht()
  lm.speed(0)
  degperpt=360.0/numofpoints
  pointmap={}
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt)
    lm.pu()
    lm.fd(circlesize)
    pointmap[point]=lm.position()
  for start in range(0,numofpoints,stepsize):
    lm.pencolor(random.choice(allcolors))
    for end in range(numofpoints):
      lm.goto(pointmap[start])
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      print start, end
      
def coolcirclesb(numofpoints,stepsize):
  import math
  lm=MyTurtle()
  ts=lm.getscreen()
  ts.bgcolor('gray50')
  lm.ht()
  lm.speed(0)
  degperpt=360.0/numofpoints
  pointmap={}
  origdist=10
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(point*degperpt+1)
    lm.pu()
    lm.fd(origdist)
    lm.dot()
    origdist+=3
    pointmap[point]=lm.position()
  for start in range(0,numofpoints):
    lm.pencolor(random.choice(somecolors))
    for end in range(start,numofpoints,stepsize):
      
      lm.goto(pointmap[start])
      x=lm.towards(pointmap[end])
      
      print x
      if(x<45 or x>200):
        lm.pd()
        lm.goto(pointmap[end])
        lm.pu()
        

        
def coolcirclesc(numofpoints,stepsize):
  import math
  lm=MyTurtle()
  ts=lm.getscreen()
  ts.bgcolor('gray50')
  lm.ht()
  lm.speed(0)
  degperpt=360.0/numofpoints
  pointmap={}
  origdist=10
  for point in range(numofpoints):
    lm.gohome()
    lm.setheading(12.5*point*degperpt+origdist)
    lm.pu()
    lm.fd(origdist)
    lm.dot()
    origdist+=1
    pointmap[point]=lm.position()
  for start in range(0,numofpoints):
    lm.pencolor(random.choice(somecolors))
    for end in range(start,numofpoints,stepsize):
      
      lm.goto(pointmap[start])
      x=lm.towards(pointmap[end])
      
      lm.pd()
      lm.goto(pointmap[end])
      lm.pu()
      
def attr():
    partlist=[]
    
    for x in range(50):
        a=MyTurtle()
        a.tracer(False)
        a.pu()
        a.goto(random.randint(-1200,1200), random.randint(-1200,1200))
        a.tracer(True)
        partlist.append(a)
    return partlist

def mag(partlist):
    for part in partlist:
        part.ht()
        furthest=[0,0]
        for anotherpart in partlist:
            if (((part.xcor()-anotherpart.xcor())**2)+(part.ycor()-anotherpart.ycor())**2)>furthest[0]:
                furthest[0]=((part.xcor()-anotherpart.xcor())**2)+(part.ycor()-anotherpart.ycor())**2
                furthest[1]=part.towards(anotherpart.pos())
        part.seth(furthest[1])
        part.pd()
        part.fd(10)
    

