#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-08 19:24:27
# @Last Modified 2015-03-08
# @Last Modified time: 2015-03-08 21:42:13

##########################################
## from http://redd.it/2y5ziw
##########################################
## Description at bottom of file
##########################################

class numberChain(object):
    def __init__(self, goalValue, numberOfSteps):
        self.valuegoal=goalValue
        self.linksgoal=numberOfSteps
        self.links=[]
        self.links.append(1)

    def calculate(self):
        self.potentialNextValues=[]
        self.currentValue=sum(self.links)
        self.currentLinks=len(self.links)
        currentDifference=self.valuegoal-self.currentValue
        largestWithoutGoingOver={}
        if currentDifference==0:
            if (self.linksgoal-self.currentLinks == 0):
                print "YAY!  that was it!"
                print self.links
            else:
                print "At least the value is right with this: "
                print self.links
        if((self.currentValue>self.valuegoal) or (self.currentLinks>self.linksgoal)):
            self.links.pop()
            self.calculate()
        for eachlinkLocation in range(len(self.links)):
            dval=self.links[eachlinkLocation]*2
            if (dval<=self.valuegoal):
                self.potentialNextValues.append(dval)
                if largestWithoutGoingOver.has_key(dval):
                    largestWithoutGoingOver[dval].append([self.links[eachlinkLocation], self.links[eachlinkLocation]])
                else:
                    largestWithoutGoingOver[dval]=[[self.links[eachlinkLocation], self.links[eachlinkLocation]],]
            if (dval==self.valuegoal):
                self.links.append(dval)
                self.calculate()
            for eachSecondValue in range(eachlinkLocation+1, len(self.links)):
                aval=self.links[eachlinkLocation] + self.links[eachSecondValue]
                self.potentialNextValues.append(aval)
                if (aval<=self.valuegoal):
                    if largestWithoutGoingOver.has_key(aval):
                        largestWithoutGoingOver[aval].append([self.links[eachlinkLocation], self.links[eachSecondValue]])
                    else:
                        largestWithoutGoingOver[aval]=[[self.links[eachlinkLocation], self.links[eachSecondValue]],]
                if (aval==self.valuegoal):
                    self.links.append(self.links[eachlinkLocation] + self.links[eachSecondValue])
                    self.calculate()
        if True:
            "hey, you made it this far!"
            nval=max(largestWithoutGoingOver.keys())
            self.links.append(nval)
            self.calculate

class NumChain2(object):

    def __init__(self,targetValue, chainLength):
        self.valuegoal=targetValue
        self.linksgoal=chainLength
        self.links=[]
        self.potentialLinks=[]
        self.links.append(1)
        self.potentialLinks.append(set([1]))
        self.fulfilled=False

    def createNextPotentialLinks(self):
        self.potentialNextValues=set()
        self.currentValue=sum(self.links)
        self.currentLinks=len(self.links)
        for eachFirstLocation in range(len(self.links)):
            for eachSecondValue in range(eachFirstLocation,len(self.links)):
                self.potentialNextValues.add(self.links[eachFirstLocation]+self.links[eachSecondValue])
        # toremove=[]
        # for eachPotential in self.potentialNextValues:
        #     if (eachPotential>self.valuegoal):
        #         toremove.append(eachPotential)
        # for eachbad in toremove:
        #     self.potentialNextValues.remove(eachbad)

    def iterate(self):
        self.createNextPotentialLinks()
        self.potentialLinks.append(self.potentialNextValues)
        # print "potentialNextValues:"
        # for eachnum in sorted(self.potentialNextValues):
        #     print eachnum
        if (self.currentLinks>=self.linksgoal-1):
            self.fulfilled=True
        elif (self.valuegoal in self.potentialNextValues):
            self.fulfilled=True
            self.setNextValue(self.valuegoal)
        # elif (max(self.potentialNextValues)==self.links[-1]):
        #     """That means we have did this last time"""
        #     if (max(self.potentialNextValues)==self.valuegoal):
        #         self.fulfilled=True
        self.setNextValue(max(self.potentialNextValues))
    def setNextValue(self,value):
        self.links.append(value)

    def theLogicController(self):
        while not self.fulfilled:
            self.iterate()
        print self.links


#Description

        # An "addition chain" is a sequence of numbers that starts with 1 and where each number is the sum of two previous numbers (or the same number taken twice), and that ends at some predetermined value. 

        # An example will make this clearer: the sequence [1, 2, 3, 5, 10, 11, 21, 42, 84] is an addition chain for the number 84. This is because it starts with 1 and ends with 84, and each number is the sum of two previous numbers. To demonstrate:

        #                     (chain starts as [1])
        #     1 + 1   = 2     (chain is now [1, 2]) 
        #     1 + 2   = 3     (chain is now [1, 2, 3]) 
        #     2 + 3   = 5     (chain is now [1, 2, 3, 5]) 
        #     5 + 5   = 10    (chain is now [1, 2, 3, 5, 10]) 
        #     1 + 10  = 11    (chain is now [1, 2, 3, 5, 10, 11]) 
        #     10 + 11 = 21    (chain is now [1, 2, 3, 5, 10, 11, 21]) 
        #     21 + 21 = 42    (chain is now [1, 2, 3, 5, 10, 11, 21, 42]) 
        #     42 + 42 = 84    (chain is now [1, 2, 3, 5, 10, 11, 21, 42, 84]) 

        # Notice that the right hand side of the equations make up the chain, and left hand side of all the equations is a sum of two numbers that occur earlier in the chain (sometimes the same number twice). 



        # We say that this chain is of length 8, because it took 8 additions to generate it (this is one less than the total amount of numbers in the chain). 

        # There are a several different addition chains of length 8 for the number 84 (another one is [1, 2, 4, 8, 16, 32, 64, 68, 84], for instance), but there are no shorter ones. This is as short as we can get. 

        # Your task today is to try and generate addition chains of a given length and last number. 

        # (by the way, you may think this looks similar to the Fibonacci sequence, but it's not, there's a crucial difference: you don't just add the last two numbers of the chain to get the next number, you can add *any* two previous numbers to get the next number. The challenge is figuring out, for each step, which two numbers to add)

        # #Formal inputs &amp; outputs

        # ##Input description

        # You will be given one line with two numbers on it. The first number will be the length of the addition chain you are to generate, and the second the final number. 

        # Just to remind you: the length of the addition chain is equal to the number of additions it took to generate it, which is the same as **one less** than the total amount of numbers in it.  

        # ##Output description

        # You will output the entire addition chain, one number per line. There will be several different addition chains of the given length, but you only need to output one of them. 

        # Note that going by the strict definition of addition chains, they don't necessarily have to be strictly increasing. However, any addition chain that is not strictly increasing can be reordered into one that is, so you can safely assume that all addition chains are increasing. In fact, making this assumption is probably a very good idea! 

        # #Examples

        # ##Input 1

        #     7 43

        # ##Output 1

        # (one of several possible outputs)

        #     1
        #     2
        #     3
        #     5
        #     10
        #     20
        #     40
        #     43

        # ##Input 2

        #     9 95

        # ##Output 2

        # (one of several possible outputs)

        #     1
        #     2
        #     3
        #     5
        #     7
        #     14
        #     19
        #     38
        #     57
        #     95

        # #Challenge inputs

        # ##Input 1

        #     10 127

        # ##Input 2

        #     13 743

        # #Bonus

        #     19 123456

        # If you want *even more* of a challenge than that input, consider this: when I, your humble moderator, was developing this challenge, my code would not be able to calculate the answer to this input in any reasonable time (even though solutions exist): 

        #     25 1234567

        # If you can solve that input, you will officially have written a much better program than me!

        # #Notes

        # I would like to note that while this challenge looks very "mathy", you don't need any higher level training in mathematics in order to solve it (at least not any more than is needed to understand the problem). There's not some secret formula that you have to figure out. It's still not super-easy though, and a good working knowledge of programming techniques will certainly be helpful!

        # In other words, in order to solve this problem (and especially the bonus), you need to be clever, but you don't need to be a mathematician. 

        # As always, if you have any suggestions for problems, hop on over to /r/dailyprogrammer_ideas and let us know!