#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
There are several repetitious database entries that I have in my db. This script
is there to clean them up. 


"""
import os, sys
import cgi
import pwd
import socket
import urlparse
import MySQLdb
import pw

sys.path.insert(0,'/home/jlmarks/mycode/mypy')

db = MySQLdb.connect(host=pw.dbhost, user=pw.dbun, passwd=pw.dbpw, db=pw.dbname)
##########################################
## this code is from a different project
##########################################
# import os, sys
# import cgi
# import pwd
# import socket
# import urlparse
# import MySQLdb
# DEBUG = 0

# db = MySQLdb.connect(host="grid50mysql2451.secureserver.net", user="jlm1232505575334", passwd="B0ttles0fb33r!", db="jlm1232505575334")

# #create a cursor for the select
# cur = db.cursor()

# #execute an sql query
# cur.execute("SELECT VERSION()")

# ##Iterate 
# for row in cur.fetchall() :
#       #data from rows
#         version = str(row[0])

#       #print 
#         print "The MySQL version is " + version

# # close the cursor
# cur.close()

# # close the connection
# db.close ()
