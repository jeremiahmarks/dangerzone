#!/usr/bin/python
# Author:	Jeremiah Marks
# Contact:	Jeremiah@jlmarks.org

# Purpose:
#	To break a CSV file that is too large to import in one import into
#		smaller, more manageable chunks.

# Method:
#	Prompt a user for the location of a large CSV file (expected to be hosted)
#	Download the file
#	Open file and count the number of rows
# 	Advise user of number of rows, ask how to break it up
#		break up options will be into X smaller files or files of length y
#	Create appropriate number of files
#	Copy first line of CSV file to each file
#	Copy appropriate number of lines to each file
# 	Report done

import urllib2

LOCALFILENAME="localCSV.csv"
NUMBEROFLOCALFILES=0

def getRemoteFile():
	global LOCALFILENAME
	print """Please input the location of the remote file.
	Example:  http://jlmarks.org/randomname/Fielding.csv 
	"""
	floc=raw_input("Please provide location of file")
	cfile= urllib2.urlopen(str(floc))
	LOCALFILENAME = floc[floc.rindex('/')+1:]
	outputFile = open(LOCALFILENAME,'wb')
	outputFile.write(cfile.read())
	outputFile.close()

def processFile():
	global LOCALFILENAME
	global NUMBEROFLOCALFILES
	numberOfLines=sum(1 for line in open(LOCALFILENAME)) - 1
	print """
	There are %s lines in this file.  How many files would you like this file broken into? 
	""" %(str(numberOfLines))
	NUMBEROFLOCALFILES = int(raw_input())
	linesPerNormalFile=numberOfLines/NUMBEROFLOCALFILES
	linesPerFirstFile= linesPerNormalFile+numberOfLines%NUMBEROFLOCALFILES
	localFile=open(LOCALFILENAME)
	firstLine=localFile.readline()
	for x in range(NUMBEROFLOCALFILES):
		smallerFileName="%03d" % x + LOCALFILENAME
		smallerFile=open(smallerFileName,'wb')
		smallerFile.write(firstLine)
		if (x == 0):
			for y in range(linesPerFirstFile):
				smallerFile.write(localFile.readline())
		else:
			for y in range(linesPerNormalFile):
				smallerFile.write(localFile.readline())
		smallerFile.close()
	localFile.close()

def recombineAndDiff():
	global LOCALFILENAME
	global NUMBEROFLOCALFILES
	recombinedFileName="recombinedFile.csv"
	recombinedFile=open(recombinedFileName,'wb')
	for x in range(NUMBEROFLOCALFILES):
		smallerFileName="%03d" % x + LOCALFILENAME
		smallerFile=open(smallerFileName)
		if (x==0):
			recombinedFile.write(smallerFile.read())
		else:
			firstline=smallerFile.readline()
			recombinedFile.write(smallerFile.read())
	recombinedFile.close()

		
if __name__ == '__main__':
	getRemoteFile()
	processFile()
	recombineAndDiff()