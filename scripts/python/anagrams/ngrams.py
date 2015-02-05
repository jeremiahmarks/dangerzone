import string
import random
import grams

class anagramfinder(object):

    
    
    def checkLetters(self,mainstring, teststring):
        #print "checkLetters is checking "+mainstring + " against "+teststring
        isThere=True
        for letter in teststring:
            if (teststring.count(letter)>mainstring.count(letter)):return False
        return isThere
    
    def getWordList(self):
        words=set()
        wordFile=open('/home/jlmarks/words.txt','r')
        for word in wordFile:
            words.add(word[:-1])
        wordFile.close()
        self.entiredictionary=words
        stringasset=set(self.astring)
        for word in words:
            if (set(word).issubset(stringasset)&self.checkLetters(self.astring,word)):
                self.allwords.append(word)
        
        
    def __init__ (self, astring):
        self.allwords=[]
        self.points=[]
        self.wordpoints=[]
        self.astring=astring
        self.getWordList()
        self.auditwordlist()
        self.computeWordScore()
    
    def auditwordlist(self):
        
        for letter in set(self.astring):
            wordsusedin=0
            for word in self.allwords:
                if letter in set(word):
                    wordsusedin+=1
            self.points.append([wordsusedin,letter])
        self.points.sort()
        tempdict={}
        for position in range(len(self.points)):
            #print [self.points[len(self.points)-position][0], self.points[position][1]]
            tempdict[self.points[position][1]]= self.points[len(self.points)-1-position][0]
        self.points=tempdict
        
    def computeWordScore(self):
        maxscore=0
        for letter in self.astring:
            maxscore=maxscore+self.points[letter]
        for word in self.allwords:
            score=0
            for letter in word:
                score=score+self.points[letter]
            self.wordpoints.append([score,word])
            if score>=maxscore:
                print word
    
            
