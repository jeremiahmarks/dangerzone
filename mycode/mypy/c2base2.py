#!/usr/bin/python

import _mysql

def sqlconnect():
    global conn
    conn = _mysql.connect("jeremiahmarks.db.6816406.hostedresource.com", 'jeremiahmarks','B0ttles0fb33r!','jeremiahmarks')


class bookshelf:
    global conn
    def __init__(self):
        self.shelf=[]
        sqlconnect()
        conn.query("""SELECT * FROM books""")
        results=conn.store_result()

        self.bookdatalayout={}
        pos=0
        desc = results.describe()
        for each in desc:
            self.bookdatalayout[each[0]] = pos
            pos+=1
        for eachresult in range(results.num_rows()):
            tbookdata=results.fetch_row()[0]
            self.addbook(tbookdata[self.bookdatalayout['origstring']], title=tbookdata[self.bookdatalayout['title']], author=tbookdata[self.bookdatalayout['author']], bookid=tbookdata[self.bookdatalayout['bookid']], isfinished=tbookdata[self.bookdatalayout['finished']])
        conn.close()
    def addbook(self, origstring, title=None,author=None, bookid=None, isfinished=None):
        if not origstring in self.shelf:
            tempbook = book(origstring, title, author, bookid, isfinished)
            self.shelf.append(tempbook)
            return tempbook
        else:
            return self.getbook(origstring)
    
    def getbook(self, origstring=None, title=None, author=None, bookid=None):
        if(bookid):
            for eachbook in self.shelf:
                if eachbook.bookid==bookid:
                    return eachbook
            return False
        elif(origstring):
            for eachbook in self.shelf:
                if eachbook==origstring:
                    return eachbook
            return False
        else:
            tempbook=book(title, author)
            for eachbook in self.shelf:
                if eachbook==tempbook:
                    return eachbook
            return False
    def cleanbooks(self):
        charsIhate=['(', ')', '-', '_',',']
        for eachbook in self.shelf:
            for eachchar in charsIhate:
                eachbook.author = eachbook.author.replace(eachchar,'')
                eachbook.title = eachbook.title.replace(eachchar,'')

class book:
    global conn
    def __init__(self, origstring, title=None,author=None, bookid=None, isfinished=None):
        self.origstring=origstring
        self.title=title
        self.author=author
        self.bookid=bookid
        self.isfinished=isfinished
        self.quotelibrary=[]
        self.newwords=[]
        if (origstring and not (title or author or bookid)):
            self.fillinfo()
    def settitle(self, title):
        self.title=title
    def addauthor(self, author):
        self.author=author
    def setbookid(self,bookid):
        self.bookid=bookid
    def isfinished(self, isfinished):
        self.isfinished=isfinished
    def addquote(self, quote):
        if not quote in quotelibrary:
            self.quotelibrary.append(Quote(highlight=quote))
    def addnewword(self, quoteid=None, frombook=None, highlight=None, note=None, definition=None):
        self.newwords.append(booknote(quoteid, frombook, highlight, note, definition))
    def __eq__(self, other):
        return ((self.title==other.title and self.author==other.author) or (self.origstring==other))
    def __str__(self):
        return self.title + " by " + self.author
    def fillinfo(self):
        self.title, self.author = self.origstring.rsplit('(',1)
    def cleanfields(self):
        charsIhate=['(', ')', '-', '_',',']
        for eachchar in charsIhate:
            self.author = self.author.replace(eachchar,'')
            self.title = self.title.replace(eachchar,'')
            
class Quote:
    def __init__(self, quoteid=None, highlight=None, frombook=None, note=None, definition=None, rawhighlight=None):
        self.quoteid=quoteid
        self.highlight=highlight
        self.frombook=frombook
        self.note=note
        self.definition=definition
        self.rawhighlight=rawhighlight
        
    def __eq__(self,other):
        return ((self.highlight==other.highlight) or (self.highlight==other))