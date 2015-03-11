#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-09 22:51:07
# @Last Modified 2015-03-10
# @Last Modified time: 2015-03-10 00:53:55


##########################################
## from http://redd.it/2y5ziw
##########################################
## Description at bottom of file
##########################################
import random
import timeit
class secondSolution(object):

    def __init__(self, numberOfLinks, desiredValue):
        self.numberOfLinks = numberOfLinks
        self.desiredValue = desiredValue
        self.links=[]
        self.links.append(1)
        solution = self.calculateNextLinks()
        if solution:
            print solution
        else:
            print "no solution found."
        

    def calculateNextLinks(self):
        potentialNextValues = set()
        currentNumberOfLinks=len(self.links)
        if (self.links[-1]==self.desiredValue):
            return self.links
        elif (self.links[-1]>self.desiredValue):
            return False
        elif (self.links[-1]*2**(self.desiredValue+1 - currentNumberOfLinks) < self.desiredValue):
            return False
        elif (currentNumberOfLinks>self.numberOfLinks):
            return False
        else:
            for outterLinkLocation in range(currentNumberOfLinks):
                for innerLinkLocation in range(outterLinkLocation, currentNumberOfLinks):
                    potentialNextValues.add(self.links[outterLinkLocation]+self.links[innerLinkLocation])
            while (len(potentialNextValues)>0):
                eachLink = max(list(potentialNextValues))
                potentialNextValues.discard(eachLink)
                self.links.append(eachLink)
                done=self.calculateNextLinks()
                if (done):
                    return done
                else:
                    self.links.pop()
            return False

class firstSolution(object):

    def __init__(self, numberOfLinks, desiredValue):
        self.numberOfLinks = numberOfLinks
        self.desiredValue = desiredValue
        self.links=[]
        self.links.append(1)
        a = self.calculateNextLinks()
        

    def calculateNextLinks(self):
        potentialNextValues = set()
        currentNumberOfLinks=len(self.links)
        if (self.links[-1]==self.desiredValue):
            return self.links
        elif (currentNumberOfLinks>self.numberOfLinks):
            return False
        else:
            for outterLinkLocation in range(currentNumberOfLinks):
                for innerLinkLocation in range(outterLinkLocation, currentNumberOfLinks):
                    potentialNextValues.add(self.links[outterLinkLocation]+self.links[innerLinkLocation])
            while (len(potentialNextValues)>0):
                eachLink = random.choice(list(potentialNextValues))
                potentialNextValues.discard(eachLink)
                self.links.append(eachLink)
                done=self.calculateNextLinks()
                if (done):
                    return done
                else:
                    self.links.pop()
            return False

def testBoth():
    times=[]
    s1=0
    s2=0
    for x in range(5):
        a=random.randint(3,12)
        b=random.randint(1,2**(a-1))
        varspassed="( %i, %i)"%(a,b)
        firsttime= timeit.timeit("firstSolution" + varspassed, "from __main__ import firstSolution",number=1)
        secondtime= timeit.timeit("secondSolution" + varspassed, setup="from __main__ import secondSolution",number=1)
        times.append([(a,b),firsttime, secondtime])
    print "links\tvalue\t time1\t time2\t\t\tFastest\tby"
    for eachTime in times:
        t1, t2 = [eachTime[1],eachTime[2]]
        if t1<t2:
            faster= "firstSolution "
            s1+=1
        else:
            faster= "secondSolution"
            s2+=1
        print "   %i\t\t%i\t\t%f\t%f\t\t%s\t%f"%(eachTime[0][0],eachTime[0][1],eachTime[1],eachTime[2], faster, abs(t1-t2))

if __name__ == '__main__':
    testBoth()