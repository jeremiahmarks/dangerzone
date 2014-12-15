#####################################################
##Author: Jeremiah Marks
##Contact: Jeremiah@JLMarks.org
##
##Purpose: This script is intended to help with finding potential words that
##         can be used in various games where you have letters that need to 
##         be turned into words. 

import string

def getwords(astring):
  stringasset=set(astring)
  allwords=getwordlist()
  words=[]
  for word in allwords:
    if (set(word).issubset(stringasset)&checkletters(astring,word)):
      words.append(word)
  return words
  
def getwordlist():
  words=set()
  try:
    wordfile=open('mypy/words.txt','r')
  except IOError:
    print "Could not open the word file. Please make sure that it is available"
  for word in wordfile:
    words.add(word[:-1])
  wordfile.close()
  return words

def checkletters(mainstring, teststring):
    isThere=True
    for letter in teststring:
        if (teststring.count(letter)>mainstring.count(letter)):return False
    return isThere
