

#new anagram finder

#will load the word file.

#will remove all words that contain letters not contained in the anagram string

#sort the anagram string alphabetically

#map the mutations of the anagram string to the potential word list, avoid redoing work if not needed.
import string
import random

def getWordList():
    words=set()
    wordFile=open('mypy/words.txt','r')
    for word in wordFile:
        words.add(word[:-1])
    wordFile.close()
    return words

def checkLetters(mainstring, teststring):
    #print "checkLetters is checking "+mainstring + " against "+teststring
    isThere=True
    for letter in teststring:
        if (teststring.count(letter)>mainstring.count(letter)):return False
    return isThere
    
def getwords(aString):
    stringasset=set(aString)
    allWords=getWordList()
    potentialWords=[]
    phrases=[]
    for word in allWords:
        if (set(word).issubset(stringasset)&checkLetters(aString,word)):
            potentialWords.append(word)
    """for words in potentialWords:
        tempstring=aString
        for letter in words:
            tempstring=tempstring.replace(letter,'',1)
        for theword in potentialWords:
            if (set(theword).issubset(set(tempstring))&checkLetters(tempstring,theword)):
                phrases.append(words+" "+theword)"""
    return potentialWords

def removeletters(oldstring, wordtoremove):
    for letter in wordtoremove:
        oldstring=oldstring.replace(letter,'',1)
    return oldstring

def getoneword(astring):
    return getwords(astring)[0]
    
def getlongestword(astring):
    words=getwords(astring)
    leadingword=''
    for word in words:
        if (len(word)>len(leadingword)):
            leadingword=word
    return leadingword
    
def getrandomword(astring):
    return random.choice(getwords(astring))
    
def getrandomwordlong(astring):
    words=getwords(astring)
    wordlength=len(getlongestword(astring))
    wordtoreturn=random.choice(words)
    if ((len(wordtoreturn)>1) or wordlength==1):
        return wordtoreturn
    else:
        return getrandomwordlong(astring)
    

def phrasemaker(astring):
    words=getwords(astring)
    
    phrases=[]
    for word in words:
        phrases.append([word, removeletters(astring,word)])
    newlist=[]
    for phrase in phrases:
        while (len(phrase[1])>0):

            wordtoadd=getrandomwordlong(phrase[1])
            phrase[0]=phrase[0]+' '+wordtoadd 
            phrase[1]= removeletters(phrase[1],wordtoadd)
        newlist.append(phrase)
        print phrase 
    
    return newlist
