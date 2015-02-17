#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-02-16 22:29:02
# @Last Modified 2015-02-16
# @Last Modified time: 2015-02-16 22:45:30

import my.pw

import MySQLdb

def main():
  db = MySQLdb.connect(host=my.pw.DBPATH, user=my.pw.DBUSE, passwd=my.pw.DBPASSWORD, db=my.pw.DBTOUSE)
  cur = db.cursor()
  cur.execute("SELECT VERSION()")
  for row in cur.fetchall() :
        #data from rows
          version = str(row[0])

        #print 
          print "The MySQL version is " + version

  # close the cursor
  cur.close()

  # close the connection
  db.close ()

if __name__ == '__main__':
  main()
# if __name__ == '__main__':
#   db = MySQLdb.connect(host=my.pw.DBPATH, user=my.pw.DBUSE, passwd=my.pw.DBPASSWORD, db=my.pw.DBTOUSE)
#   cur = db.cursor()
#   cur.execute("SELECT VERSION()")
#   for row in cur.fetchall() :
#         #data from rows
#           version = str(row[0])

#         #print 
#           print "The MySQL version is " + version

#   # close the cursor
#   cur.close()

#   # close the connection
#   db.close ()
