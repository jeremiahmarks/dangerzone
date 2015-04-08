#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-14 22:08:02
# @Last Modified 2015-04-03
# @Last Modified time: 2015-04-03 21:31:08


import MySQLdb
import pw

class statementOrganizer(object):

    def __init__(self):
        self.running=True
        ##self.db=MySQLdb. connect(host=pw.DBPATH, user=pw.DBUSER, passwd=pw.DBPASSWORD, db=pw.DBTOUSE)

    def startServer(self):
        self.db=MySQLdb. connect(host=pw.DBPATH, user=pw.DBUSER, passwd=pw.DBPASSWORD, db=pw.DBTOUSE)
    def endServer(self):
        self.db.close()

    def addStmt(self, stmtToAdd):
        self.startServer()
        cur = self.db.cursor()
        stmt = 'INSERT INTO resStmts (statement) VALUES ("%s")'
        cur.execute(stmt, (stmtToAdd))
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            rownum = row[0]
        cur.close()
        return rownum
        self.endServer()

    def addTag(self, tagToAdd):
        self.startServer()
        cur = self.db.cursor()
        stmt = 'INSERT INTO restags (tagname) VALUES (%s)'
        cur.execute(stmt, (tagToAdd))
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            rownum = row[0]
        cur.close()
        self.endServer()
        return rownum

    def applyTagToStatement(self, statementid, tagid):
        self.startServer()
        cur = self.db.cursor()
        ## check if that tag is already applied
        checkStmt='SELECT COUNT(1) FROM restagsapplied WHERE resstatementid="%s" AND restagid="%s"'
        cur.execute(checkStmt, (int(statementid), int(tagid)))
        for row in cur.fetchall():
            if row[0]==0:
                stmt = 'INSERT INTO restagsapplied (resstatementid, restagid) VALUES ("%s", "%s")'
                cur.execute(stmt, (int(statementid), int(tagid)))
                cur.execute("SELECT LAST_INSERT_ID()")
                for row in cur.fetchall():
                    rownum = row[0]
            else:
                rownum = 0
        cur.close()
        self.endServer()
        self.getAllTagApplication()
        return rownum

    def getAllTags(self, ):
        cur = self.db.cursor()
        self.tags={}
        stmt="SELECT id, tagname FROM restags"
        cur.execute(stmt)
        for row in cur.fetchall():
            self.tags[int(row[0])] = row[1]
        cur.close()

    def getAllStmts(self, ):
        cur = self.db.cursor()
        self.stmts={}
        stmt = "SELECT id, `statement` FROM resStmts"
        cur.execute(stmt)
        for row in cur.fetchall():
            self.stmts[int(row[0])] = row[1]
        cur.close()

    def getAllTagApplication(self, ):
        self.startServer()
        self.getAllTags()
        self.getAllStmts()
        self.tagsToStmts={}
        self.stmtsTotags={}
        for eacht in self.tags.iterkeys():
            self.tagsToStmts[eacht] = []
        for eachs in self.stmts.iterkeys():
            self.stmtsTotags[eachs] = []
        cur = self.db.cursor()
        self.tagApps={}
        stmt = "SELECT applicationid, resstatementid, restagid  FROM restagsapplied"
        cur.execute(stmt)
        for row in cur.fetchall():
            self.tagApps[int(row[0])] = {'statement':int(row[1]), 'tag':int(row[2])}
            print row[2]
            self.tagsToStmts[int(row[2])].append(int(row[1]))
            self.stmtsTotags[int(row[1])].append(int(row[2]))
        cur.close()
        self.endServer()

    def statementMenu(self,statementid):
        self.getAllTagApplication()
        menu = """
        Options:  
        \t(c)reate new tag
        \t(a)pply Existing tag
        \t(n)ext
        \t(p)revious

        Available Tags: 
        """
        for eachTag in self.tags.iterkeys():
            menu+="%s-%s\t"%(str(eachTag), self.tags[eachTag])
        menu+="\n\nSTATEMENT:\n"+self.stmts[statementid]
        menu+="\n\nApplied Tags:\n"
        for eachTag in self.stmtsTotags[statementid]:
            menu+="%s-%s\t"%(str(eachTag), self.tags[eachTag])
        print menu
        choice=raw_input("Choice: ")
        self.inputParser(choice, statementid)

    def inputParser(self, choice, statementid):
        choiceVals=choice.replace(' ','').split("-")
        if choiceVals[0]=='c':
            newTagName=raw_input("New Tag Name: ")
            newTagId=self.addTag(newTagName)
            self.applyTagToStatement(statementid,newTagId)
            self.statementMenu(statementid)
        elif choiceVals[0]=='a':
            choiceVals = [choiceVals[0], int(choiceVals[1])]
            self.applyTagToStatement(statementid,choiceVals[1])
            print choiceVals
            self.statementMenu(statementid)
        elif choiceVals[0]=='n':
            stmtKeys=self.stmts.keys()
            stmtKeys.sort()
            self.statementMenu(stmtKeys[stmtKeys.index(statementid)+1])
        elif choiceVals[0]=='p':
            stmtKeys=self.stmts.keys()
            stmtKeys.sort()
            self.statementMenu(stmtKeys.index(statementid)-1)
        else:
            print "I do now know how to do that."
            self.statementMenu(statementid)

def __init__():
    pass


if __name__ == '__main__':
    a=statementOrganizer()
    a.getAllTagApplication()