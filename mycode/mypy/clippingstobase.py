#!/usr/bin/python

import _mysql

conn = _mysql.connect("jeremiahmarks.db.6816406.hostedresource.com", 'jeremiahmarks','B0ttles0fb33r!','jeremiahmarks')


class bookshelf:
    global conn
    def __init__(self):
        self.shelf=[]
    def addbook(self, title=None,author=None, bookid=None, isfinished=None):
        newbook = book(title, author, bookid, isfinished)
        if (not newbook in self.shelf):
            self.shelf.append(newbook)
            return True
        else:
            return False
    def getbook(self, title=None, author=None, bookid=None):
        if(bookid):
            for eachbook in self.shelf:
                if eachbook.bookid==bookid:
                    return eachbook
            return False
        else:
            tempbook=book(title, author)
            for eachbook in self.shelf:
                if eachbook==tempbook:
                    return eachbook
            return False
        

class book:
    global conn
    def __init__(self, title=None,author=None, bookid=None, isfinished=None):
        self.title=title
        self.author=author
        self.bookid=bookid
        self.isfinished=isfinished
        self.quotelibrary=[]
        self.newwords=[]
    def settitle(self, title):
        self.title=title
    def addauthor(self, author):
        self.author=author
    def setbookid(self,bookid):
        self.bookid=bookid
    def isfinished(self, isfinished):
        self.isfinished=isfinished
    def addquote(self,quoteid=None, frombook=None, highlight=None, note=None):
        self.quotelibrary.append(booknote(quoteid, frombook, highlight, note))
    def addnewword(self, quoteid=None, frombook=None, highlight=None, note=None, definition=None):
        self.newwords.append(booknote(quoteid, frombook, highlight, note, definition))
    def __eq__(self, other):
        return (self.title==other.title and self.author==other.author)
    def __str__(self):
        return self.title + " by " + self.author
    

class booknote:
    global conn
    def __init__(self, quoteid=None, frombook=None, highlight=None, note=None, definition=None):
        self.quoteid=quoteid
        self.frombook=frombook
        self.highlight=highlight
        self.note=note
        self.definition=definition
    def addquoteid(self, quoteid):
        self.quoteid=quoteid
    def addbook(self,frombook):
        self.frombook=frombook
    def addhighlight(self,highlight):
        self.highlight=highlight
    def addnote(self,note):
        self.note=note
    def adddefinition(self, definition):
        self.definition=definition


def getclips():

    f=open("clippings.txt", "r")
    #opening the file that contains the clips
    clip=[]
    t=[]
    for line in f:
        line=unicode(line, 'utf-8-sig').strip()
        #this converts from utf-8 to unicode and strips unnecessary chars
        if (not line==''):
            #drops empty lines
            t.append(line)
        if line=="==========":
            #the kindle uses that line to signify the end of an entry
            #when we find it we append the current entry to the list of entries and
            #then clear out the templist for the next entry
            clip.append(t)
            t=[]
    for selection in clip:
        if (not selection[1][0]=='-'):
            #for some reason the kindle occasionally splits the author up onto a 
            #a different line. This simply rectifies that problem.
            selection[0] = selection[0] +" "+ selection[1]
            del selection[1]
    return clip

def doit():
    clips=getclips()
    for clip in clips:
        split= clip[0].rfind('(')
        author=clip[0][split:]
        title=clip[0][:split]
        print author + " " + title
        
        