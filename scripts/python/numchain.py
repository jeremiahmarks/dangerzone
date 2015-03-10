#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-08 21:40:17
# @Last Modified 2015-03-09
# @Last Modified time: 2015-03-09 21:40:22

class NumChain2(object):

    def __init__(self,targetValue, chainLength):
        self.valuegoal=targetValue
        self.linksgoal=chainLength
        self.links=[]
        self.potentialLinks=[]
        self.links.append(1)
        self.potentialLinks.append(set([1]))
        self.fulfilled=False
        self.chainsThatWork=[]

    def createNextPotentialLinks(self):
        self.potentialNextValues=set()
        self.currentValue=sum(self.links)
        self.currentLinks=len(self.links)
        for eachFirstLocation in range(len(self.links)):
            for eachSecondValue in range(eachFirstLocation,len(self.links)):
                self.potentialNextValues.add(self.links[eachFirstLocation]+self.links[eachSecondValue])

    def iterate(self):
        self.createNextPotentialLinks()
        self.potentialLinks.append(self.potentialNextValues)
        if (self.currentLinks>=self.linksgoal-1):
            if (len(self.chainsThatWork)>0):
                self.fulfilled=True
        elif (self.valuegoal in self.potentialNextValues):
            self.setNextValue(self.valuegoal)
        # elif (max(self.potentialNextValues)==self.links[-1]):
        #     """That means we have did this last time"""
        #     if (max(self.potentialNextValues)==self.valuegoal):
        #         self.fulfilled=True
        for eachPotential in self.potentialNextValues:
            self.setNextValue(eachPotential)
            self.links.pop()
    def setNextValue(self,value):
        self.links.append(value)
        if (value==self.valuegoal):
            temp=[]
            for eachV in self.links:
                temp.append(eachV)
            self.chainsThatWork.append(temp)

    def theLogicController(self):
        while not self.fulfilled:
            self.iterate()
        print self.links
