#!~/html/.virtualenv/pythonenv/bin/python2.7

print 'Content-type: text/plain\r\n';

import os, sys
import cgi
import pwd
import socket
import urlparse
import MySQLdb
DEBUG = 0

db = MySQLdb.connect(host="", user="", passwd="!", db="")

#create a cursor for the select
cur = db.cursor()

#execute an sql query
cur.execute("SELECT VERSION()")

##Iterate 
for row in cur.fetchall() :
      #data from rows
        version = str(row[0])

      #print 
        print "The MySQL version is " + version

# close the cursor
cur.close()

# close the connection
db.close ()
