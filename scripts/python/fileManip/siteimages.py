import os
from wand.image import Image
import wand

def makeindex(pictureDir, picwidth, picheight , filetypes=['jpg','gif','png']):
  blacksort(pictureDir)
  allfiles=os.listdir(pictureDir)
  allfiles.sort()
  indexname=pictureDir+'index.html'
  if not os.path.exists(indexname):
    f=open(indexname, 'w')
    f.close()
  f=open(indexname, 'rb+')
  filecontents="""<html>
  <head>
    <script type="text/javascript" src="http://jlmarks.org/javascripts/sliderman.1.3.7.js"></script>
    <link rel="stylesheet" type="text/css" href="http://jlmarks.org/css/sliderman.css" />
  </head>
  <body>
  <div id="wrapper">
  <div id="outer">
  <div id="slider_container_2">

				<div id="SliderName_2" class="SliderName_2">
				
				
  """
  
  tail="""
  
  </div>
  <div id="SliderNameNavigation_2"></div>
  </div>
  <script type="text/javascript">
    var myslider=Sliderman.slider({container: 'SliderName_2', width:"""+str(picwidth)+""", height: """+str(picheight)+""",effects: 'fade', display: {autoplay: 1500}});
  </script>
  </div>
  </body>
  </html>
  
  
  """
  x=0
  first=True
  total=len(allfiles)
  for eachfile in allfiles:
    print str(x)+" of "+str(total)
    #if first and eachfile[-3:] in filetypes:
      #newline='\n<img src="'+eachfile+'" width="'+str(picwidth)+'" height="'+str(picheight)+'" alt="sometext" title="'+eachfile+'" usemap="#img1map" />\n <map'
    if eachfile[-3:] in filetypes:
      newline='\n<img src="'+eachfile+'" width="'+str(picwidth)+'" height="'+str(picheight)+'" alt="sometext" title="'+eachfile+'" />\n'
      filecontents=filecontents+newline
    x+=1
  filecontents=filecontents+tail
  f.write(filecontents)
  f.close()
  
  

def wdivide(inputDir, filetypes=['gif','jpg','png'], sizediff=100):
  sizediff=int(sizediff)
  allfiles=os.listdir(inputDir)
  for eachfile in allfiles:
    if eachfile[-3:] in filetypes:
      with Image(filename=inputDir+eachfile) as img:
        endwidth=((int(img.size[0])/sizediff)*sizediff)+sizediff
        endheight=((int(img.size[1])/sizediff)*sizediff)+sizediff
        borderw=(endwidth-int(img.size[0]))/2
        borderh=(endheight-int(img.size[1]))/2
        #bordercommand='convert '+inputDir+eachfile+' -matte -bordercolor none -border '+borderw+'x'+borderh+' '+inputDir+size+'/'+eachfile
        size=str(endwidth)+'x'+str(endheight)
        if not os.path.exists(inputDir+size):
          os.mkdir(inputDir+size)
        command = 'convert '+inputDir+eachfile+' -matte -bordercolor none -border '+str(borderw)+'x'+str(borderh)+' '+inputDir+size+'/'+eachfile
        os.system(command)

def bringtoonedir(mainDir, someDir=None):
  """
  This is designed to bring all of the files from different subdirectories into 
  one main directory
  """
  if someDir==None:someDir=''
  curDir=mainDir+someDir
  print curDir, mainDir, someDir
  allfiles=os.listdir(curDir)
  for eachfile in allfiles:
    if os.path.isdir(curDir+eachfile):
      print 'isdir! '+someDir+eachfile+'/'
      bringtoonedir(mainDir, someDir+eachfile+'/')
    else:

      

      command='mv '+curDir+eachfile+' '+mainDir

      os.system(command)

def blacksort(dirtosort, filetypes=['gif','jpg','png']):
  allfiles=os.listdir(dirtosort)
  letters=lambda x: chr(97+((x/(26**10))%26))+chr(97+((x/(26**9))%26))+chr(97+((x/(26**8))%26))+chr(97+((x/(26**7))%26))+chr(97+((x/(26**6))%26))+chr(97+((x/(26**5))%26))+chr(97+((x/(26**4))%26))+chr(97+((x/(26**3))%26))+chr(97+((x/(26*26))%26))+chr(97+((x/26)%26))+chr(97+(x%26))
  x=0
  blacks=[]
  for eachfile in allfiles:
    if eachfile[-3:] in filetypes:
      with Image(filename=dirtosort+eachfile) as img:
        if wand.color.Color('rgb(0,0,0)') in img.histogram.keys():
          blacks.append([letters(x)+'.'+eachfile[-3:], img.histogram[wand.color.Color('rgb(0,0,0)')]])
        else:
          blacks.append([letters(x)+'.'+eachfile[-3:], 0])
        os.system('mv '+dirtosort+eachfile+' '+dirtosort+letters(x)+'.'+eachfile[-3:])
      x+=1
  x=0
  blacks.sort(key=lambda x: x[1])
  for eachfiles in blacks:
    os.system('mv '+dirtosort+eachfiles[0]+' '+dirtosort+'%08d' %x + eachfiles[0][-4:])
    x+=1
