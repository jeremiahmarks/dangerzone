# This script is intended to change the images created by a turtle script
# from postscript files to png files. 

import os
from wand.image import Image

def c2gif(inputDir, outDir):
    """
    Assumes that all files in the inputDirectory are image files. 
    Attempts to convert all of the files in the input directory to a 
    .gif representation of the file and then saves the .gif into the outDir
    
    the input/output directory is assumed to have '~/' as a given. 
    
    for instance an input directory of 'circles/' would convert all of the files
    in '~/circles/'
    
    
    """
    
    for root, dirs, files in os.walk(inputDir):
        x=0
        numberoffiles=len(files)
        for f in files:
            with Image(filename=root+f) as img:
                with img.convert('gif') as newimg:
                    newfilename=outDir+f[:-4]+'.gif'
                    newimg.save(filename=newfilename)
                    x=x+1
                    percentdone=(float(x)/numberoffiles)*100
                    print newfilename + ": Done! " + str(percentdone) + "%"

def trim(inputDir,outDir):
    """
    Since I have very nasty habit of leaving assloads of blank space around images
    that I create, this script crops the "border" as much as it can. 
    """
    letters=lambda x: chr(97+((x/(26**10))%26))+chr(97+((x/(26**9))%26))+chr(97+((x/(26**8))%26))+chr(97+((x/(26**7))%26))+chr(97+((x/(26**6))%26))+chr(97+((x/(26**5))%26))+chr(97+((x/(26**4))%26))+chr(97+((x/(26**3))%26))+chr(97+((x/(26*26))%26))+chr(97+((x/26)%26))+chr(97+(x%26))
    letter=0
    allfiles=os.listdir(inputDir)
    allfiles.sort()
    filesinoutdir=os.listdir(outDir)
    os.chdir(inputDir)
    for eachfile in allfiles:
        if eachfile[-3:]=="gif" or eachfile[-3:]=="png":
            if eachfile not in filesinoutdir:
                command='convert -trim +repage ' + eachfile + " "+outDir+eachfile
                
                os.system(command)
            else:
                while(letters(letter)+eachfile[-4:] in filesinoutdir):
                    letter+=1
                command='convert -trim +repage ' + eachfile + " "+outDir+letters(letter)+eachfile[-4:]
                letter+=1
                os.system(command)
                
def rename(inputDir, outDir, startx=0):
  allfiles=os.listdir(inputDir)
  filesinoutdir=os.listdir(outDir)
  os.chdir(inputDir)
  x=startx
  for eachfile in allfiles:
    if eachfile[-3:]=="gif" or eachfile[-3:]=="png":
      tempname='%08d' %x + eachfile[-4:]
      if tempname not in filesinoutdir:
        command = 'cp '+ eachfile + ' '+outDir+tempname
        
        os.system(command)
        x+=1
      else:
        while ('%08d' %x + eachfile[-4:]) in filesinoutdir:
          x+=1
        tempname='%08d' %x + eachfile[-4:]
        command = 'cp '+ eachfile + ' '+outDir+tempname
        
        os.system(command)
        x+=1
                
def c2png(inputDir, outDir):
    """
    Assumes that all files in the inputDirectory are image files. 
    Attempts to convert all of the files in the input directory to a 
    .gif representation of the file and then saves the .gif into the outDir
    
    the input/output directory is assumed to have '~/' as a given. 
    
    for instance an input directory of 'circles/' would convert all of the files
    in '~/circles/'
    
    
    """
    
    for root, dirs, files in os.walk(inputDir):
        x=0
        numberoffiles=len(files)
        for f in files:
            with Image(filename=root+f) as img:
                with img.convert('png') as newimg:
                    newfilename=outDir+f[:-4]+'.png'
                    newimg.save(filename=newfilename)
                    x=x+1
                    percentdone=(float(x)/numberoffiles)*100
                    print newfilename + ": Done! " + str(percentdone) + "%"

def changealltogif(topDir, somedir=None, filetypes=['jpg','png']):
  if somedir==None:somedir=''
  curDir=topDir+somedir
  allfiles=os.listdir(curDir)
  for eachfile in allfiles:
    if os.path.isdir(curDir+eachfile):
      changealltogif(topDir, somedir+eachfile+'/', filetypes)
    else:
      if eachfile[-3:] in filetypes:
        command='convert '+curDir+eachfile+" "+curDir+eachfile[:-3]+'gif'
        os.system(command)
        os.remove(curDir+eachfile)
