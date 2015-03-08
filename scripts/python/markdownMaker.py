#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-07 23:13:32
# @Last Modified 2015-03-08
# @Last Modified time: 2015-03-08 01:15:21


############################################################
##
##  This file will start in a folder. 
##  If there is no README.md, it will create one.
##  It will open README.md
##  It will look for the line that signifies the start of the TOC
##  If there is not one, it will create on on the last line.
##  If there is one it will delete everything after that line
##  Script will crawl directories recursively
##  Script will create a TOC of all files and folders in directory
############################################################
############################################################
## TOC START LINE = "#TOC START"

import os

class Crawler(object):
    def __init__(self):
        self.mywd = os.getcwd()
        self.openreadme()
        self.findTOC()
        self.updateToc()
        self.closeUp()

    def openreadme(self):
        if not os.path.isfile('README.md'):
            open('README.md', 'a').close()
        self.readme = open('README.md', 'r+')

    def findTOC(self):
        tocStartString="""

####################################################
#TOC START
####################################################
"""
        self.fileLines=[]
        for eachLine in self.readme:
            if not(eachLine.find("#TOC START")==-1):
                if len(self.fileLines)>2:
                    precedingLine=self.fileLines.pop()
                break
            else:
                self.fileLines.append(eachLine)
        self.fileLines.append(tocStartString)
        self.readme.close()
        open ('README.md','w').close()
        self.readme = open('README.md', 'r+')

    def updateToc(self):
        self.subCrawlers=[]
        for root, dirs, files in os.walk(self.mywd):
            level = root.replace(self.mywd, '/').count(os.sep)
            indent = ' ' * 2 * (level +1)
            if level == 2:
                if not (root.replace(self.mywd,'')=='.git'):
                    os.chdir(root)
                    # print os.getcwd()
                    self.subCrawlers.append(Crawler())
                    os.chdir(self.mywd)
            self.fileLines.append('* {}'.format(root.replace(self.mywd, '.')+'\n'))
            for f in files:
                self.fileLines.append('{}* [{}]({}\{})'.format(indent, f, root.replace(self.mywd, '.'),f)+'\n')
        for eachLine in self.fileLines:
            self.readme.write(eachLine)
    def closeUp(self):
        self.readme.close()





if __name__ == '__main__':
    a=Crawler()
