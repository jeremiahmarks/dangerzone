#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
There are several repetitious database entries that I have in my db. This script
is there to clean them up. 


"""
import os, sys
sys.path.insert(0,'/home/jlmarks/mycode/mypy') #adds the location of my password file to the path
import cgi
import pwd
import socket
import urlparse
import MySQLdb
import pw


db = MySQLdb.connect(host=pw.dbhost, user=pw.dbun, passwd=pw.dbpw, db=pw.dbname)
query="SELECT id,sourcecode,about,dateadded FROM portfolio ORDER BY sourcecode,dateadded ASC"
headers=("id","sourcecode","about","dateadded")

cur=db.cursor()

cur.execute(query)

todelete=[]
toupdate=[]
allentries={}



for row in cur.fetchall():
	thisentry={}
	for header,fieldvalue in zip(headers,row):
		thisentry[header]=fieldvalue
	if thisentry['sourcecode'] in allentries.keys():
		oldentry=allentries[thisentry['sourcecode']]
		todelete.append(thisentry['id'])
		toupdate.append(oldentry['sourcecode'])
		newabout=oldentry['about']+"\n"+str(thisentry['dateadded'])+"\t"+thisentry['about']
		allentries[thisentry['sourcecode']]['about']=newabout
	else:
		allentries[thisentry['sourcecode']]=thisentry

for eachentry in toupdate:
	thisoldentry=allentries[eachentry]
	thisquery="UPDATE portfolio SET about=\""+thisoldentry['about']+"\" WHERE id="+str(thisoldentry['id'])
	cur.execute(thisquery)

for delentry in todelete:
	thisquery="DELETE FROM portfolio WHERE id="+str(delentry)
	cur.execute(thisquery)



cur.close()
db.close()
