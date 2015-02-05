
#This file is intended to accept an input folder and an outfolder. It will
#then recursively move through the input folder and move all files into 
#the single output folder. 


import os, shutil


def movefiles():
    x=0
    inputDir=raw_input("please enter the folder where the files are: ")
    outputDir=raw_input("please enter the destination folder")
    for root, dirs, files in os.walk(inputDir topdown=False):
        for name in files:
            newname="%09d"%x+name
            x+=1
            shutil.move(os.path.join(root, name), os.path.join(outputDir,newname))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
            
def consolodateby():
    inputDir=raw_input("please enter the folder where the files are: ")
    filesperdir=int(raw_input("How many files per dir?"))
    

    for x in range(10):
        os.system("mkdir "+inputDir+"/"+str(x))

    for root, dirs, files in os.walk(inputDir):
        for f in files:
            shutil.move(os.path.join(root, f),os.path.join(root+"/"+str(f[8]),f))