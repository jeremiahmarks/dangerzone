#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-10 02:16:00
# @Last Modified 2015-05-10>
# @Last Modified time: 2015-05-10 03:56:55

import math
import fractions

primesAndNums={}
primesAndNums["primes"]=[]
primesAndNums["powerful"]=set()
primesAndNums["perfectPowers"]=set()
primesAndNums["achillesNums"]=set()
primesAndNums['strongAchillesNums']=set()
primesAndNums["totients"]={}
primesAndNums['factors']={}

def newDD():
    primesAndNums={}
    primesAndNums["primes"]=[]
    primesAndNums["powerful"]=set()
    primesAndNums["perfectPowers"]=set()
    primesAndNums["achillesNums"]=set()
    primesAndNums['strongAchillesNums']=set()
    primesAndNums["totients"]={}
    primesAndNums['factors']={}

def isitprime(number):
    isprime = False
    if number==1:
        return True
    elif number==2:
        return True
        
    elif number%2==0:
        return False
    for x in range(3, int(number**0.5) + 1, 2):
        if number%x==0:
            return False
    return True

def breakUpToPrimes(number):
    primes={}
    counter=0
    myPrimes=iter(primesAndNums["primes"])
    thisPrime=myPrimes.next()
    while (number>1):
        if (thisPrime<2):
            thisPrime=myPrimes.next()
            continue
        if (number%thisPrime == 0 ):
            counter+=1
            primes[thisPrime] = counter
            number = number/thisPrime
        else:
            if not(counter==0):
                primes[thisPrime] = counter
            counter = 0
            thisPrime=myPrimes.next()
    return primes

def countTotient(number):
    totients = 0
    for potentialTotient in range(1, number + 1):
        if fractions.gcd(number, potentialTotient) == 1:
            totients += 1
    return totients

def findAllPerfectRoots(maxVal):
    maxRoot = int(maxVal**(0.5))+1
    for x in range(2,maxRoot):
        thisRoot=2
        while(x**thisRoot<maxVal):
            thisVal = x**thisRoot
            primesAndNums['perfectPowers'].add(thisVal)
            thisRoot+=1

def isitpowerful(number):

    pass

def isitperfect(number):
    pass

def isitachilles(number):
    pass

def isitstrongachilles(number):
    pass

def main(maxVal):
    print "Starting by finding all perfect values, this is because it may help speed up primes"
    findAllPerfectRoots(maxVal)
    # print "starting with primes"
    # for x in range(2,maxVal):
    #     if isitprime(x):
    #         primesAndNums["primes"].append(x)
    print "finding all roots"
    for ro in range(2,maxV):
        if isitprime(ro):
            primesAndNums["primes"].append(ro)
        primesAndNums['factors'][ro] = breakUpToPrimes(ro)
    print "I just got all factors and primes, now Finding all perfect Roots"
    # findAllPerfectRoots(maxVal)
    print "all perfection found, moving to prime"
    # for x in range(2,maxVal):
    #     if isitprime(x):
    #         primesAndNums["primes"].append(x)
    print "Primes done Starting Power"
    for t in range(2,maxVal):
        if isitpowerful(t):
            primesAndNums['powerful'].add(t)
    print "Power checked, checking perfection"
    # for per in range(2,maxVal):
    #     if (per in primesAndNums['perfectPowers']):
    #         primesAndNums
    print "Seems Redundant, onto checking for Achilles and Strength"
    for ach in range(2,maxVal):
        if isitachilles(ach):
            primesAndNums['achillesNums'].add(ach)
            tots=countTotient(ach)
            if tots in primesAndNums['achillesNums']:
                primesAndNums['strongAchillesNums']
