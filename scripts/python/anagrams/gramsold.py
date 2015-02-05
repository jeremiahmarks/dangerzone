

#new anagram finder

#will load the word file.

#will remove all words that contain letters not contained in the anagram string

#sort the anagram string alphabetically

#map the mutations of the anagram string to the potential word list, avoid redoing work if not needed.
import string

def getWordList():
    words=set()
    wordFile=open('/home/jlmarks/words.txt','r')
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
    

def phraseGenerator(aString, potentialWords):
    phrases=[]
    """
    The phrase generator will accept the original anagram string,
    the list of all potential words, and the list of phrases that 
    it creates. It will check that all of the potential words are valid,
    and remove invalid ones. If there are still valid potential words, it will add one to the
    phrase list,    remove the neccessary letters from the astring, 
    and check that the astring is not     an empty string. If there are still valid letters in the astring, it will submit the 
    new astring, potentialWords, and phrase to itself. 
    
    """
        
    
        
    for word in potentialWords:
        words=potentialWords
        tempstring=aString
        phrase = phrase + " " + word
        while not(tempstring=="" or words==[]):
            for letter in word:
                tempstring=tempstring.replace(letter,'',1)
            if not checkLetters(aString, word):
                words.remove(word)        
            
        phrases.append(phrase)

        
        
        
def makePhrase(aString, potentialWords):

    wordlist=[]
    for word in potentialWords:
        wordsthatwork=[]
        tempstring=aString
        templist=potentialWords[:]
        for letter in word:
            tempstring=tempstring.replace(letter,'',1)
        for eachword in templist:
            if (checkLetters(tempstring,eachword)):
                wordsthatwork.append(eachword)
        wordlist.append([word, tempstring, wordsthatwork])
    return wordlist
        
        
        
    """
    General Algorithm that should happen. 
    
    


    """
def a():
    a=updater("asdfetnmil", getwords("asdfetnmil"))
    return a    
    
    
def updater(originalString, wordlist, tempPhrase='', phraseList=[]):
    if (originalString=='' or wordlist == []):
        phraseList.append(tempPhrase+' \n')
        print phraseList[1] + 'length of phraseList: '+len(phraseList) 
        tempPhrase=''
        return phraseList
    else:
        for word in wordlist:
            tempstring=originalString
            templist=wordlist
            tempPhrase=tempPhrase + ' ' +word
            for letter in word:
                tempstring=tempstring.replace(letter,'',1)
            if not checkLetters(tempstring, word):
                templist.remove(word)
            a=updater(tempstring, templist, tempPhrase, phraseList)
            
        return phraseList
                
def again():
    thestring='jenniferleighmarks'
    wordlist=getwords(thestring)
    phraselist=[]
    potential_firstWords=len(wordlist)
    for word in wordlist:
        tempstring=thestring
        templist=wordlist
        for letter in word:
            tempstring=tempstring.replace(letter,'',1)
        if not checkLetters(tempstring, word):
            templist.remove(word)
        phraselist.append([word,tempstring, templist])

    for phrase in phraselist:
        tempphrase=phrase[0]+' '
        for eachword in phrase[2]:
            tempstring=phrase[1]
            templist=[]
            for nextword in phrase[2]:
                templist.append(nextword)
            
            for letter in eachword:
                tempstring=tempstring.replace(letter, '', 1)
            
            if not checkLetters(tempstring, eachword):
                print "I am removing "+ eachword + " here is templist: "
                print len(templist)
                templist.remove(eachword)
            phrase.append([tempphrase+eachword, tempstring, templist])
            
    return phraselist
        
def stringmagic(lettersLeft, wordlist):
    
    for word in wordlist:
        pass
    pass
    

def again2():
    thestring='apple'
    wordlist=getwords(thestring)
    phraselist=[]

    for word in wordlist:
        tempwordlist=[]
        tempphraselist=[]
        tempstring=thestring
        templist=wordlist[:]
        for letter in word:
            tempstring=tempstring.replace(letter,'',1)
#        templist=getwords(tempstring)
        #while 
        for eachword in templist:
            if checkLetters(tempstring, eachword):
                tempwordlist.append(eachword)
        phraselist.append([word,tempstring, tempwordlist])
#    for phrase in range(len(phraselist)):
    for phrase in phraselist:
        if (phrase[2]<=0):
            continue
        
        tempstring=phraselist[phrase][1]
        print tempstring
        templist=phraselist[phrase][2][:]
        
        while (len(templist)>0):
            print "potential words before removal: " + str(len(templist))
            tempphrase = tempphrase + templist[0] + ' '
            
            for letter in templist[0]:
                tempstring=tempstring.replace(letter,'',1)
            print templist[0]+' '+tempstring+' '+tempphrase
            for eachword in templist:
                if not checkLetters(tempstring, eachword):
                    templist.remove(eachword)
            print "potential words after removal: " + str(len(templist))
        phraselist[phrase]=tempphrase
        
    return phraselist    


def words(astring):
    listofwords=getwords(astring)
    a=dothewords(astring,listofwords)


    
def dothewords(astring, listofwords, startingstring=''):

    newwordlist=[]
    for eachword in listofwords:
        thisphrase=startingstring+eachword+' '
        templist=listofwords[:]
        tempstring=astring
        for letter in eachword:
            tempstring=tempstring.replace(letter, '', 1)
        for word in templist:
            if checkLetters(tempstring, word):
                newwordlist.append(word)
                print word
        
        if (len(templist)==0):
            new.append(thisphrase)
            #return allphrases
            continue
        else:
            newwordlist.append(dothewords(tempstring, newwordlist, thisphrase))
    return newwordlist


#
#def dewthewords(astring, listofwords, startingstring=''):
    
#    for eachword
