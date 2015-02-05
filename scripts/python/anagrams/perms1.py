#!/usr/bin/python

#This script takes a string and returns all permutations of it. 
#if you use perms.perms("apple") you will get all permutations of Apple
#in order to get all dictionary words, you will need to use perms.getRealWords(yourString)
#Note that this is very processor intensive, so it is best to stick to 16 or fewer characters. 
#aeiousadfe

import itertools


def getPerms(somestring, length):
    return itertools.permutations(somestring, length)
    
def permsToList(allperms):
    listOfPerms=set()
    while allperms.next:
        try:
            tempstring=""
            nextHolder=allperms.next()
            for charPOS in range(len(nextHolder)):
                tempstring=tempstring+nextHolder[charPOS]
            listOfPerms.add(tempstring)
        except StopIteration:
            break
    return listOfPerms

def perms(aString):
    allperms=[]
    for length in range(len(aString)+1):
        allperms.append(permsToList(getPerms(aString, length)))
    return allperms
    
def getWordList():
    words=set()
    wordFile=open('mypy/words.txt','r')
    for word in wordFile:
        words.add(word[:-1])
    wordFile.close()
    return words
    
def getRealWords(aString):
    actualWords=set()
    words=getWordList()
    allPerms=perms(aString)
    for wordLength in range(1, len(allPerms)):
        actualWords=actualWords.union(words&allPerms[wordLength])
    return actualWords

def realWords(aString):
    actualWords=set()
    allPerms=[]
    words=getWordList()
    for length in range(len(aString)+1):
        allPerms.append(permsToList(getPerms(aString, length)))
        actualWords=actualWords.union(words&allPerms[length])
        print actualWords
        raw_input("Press Enter to continue...")
    return actualWords

def example():
    a=getRealWords("aeeiouysadtrghb")
