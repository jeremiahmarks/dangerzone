#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-09 19:25:25
# @Last Modified 2015-05-10
# @Last Modified time: 2015-05-10 01:07:11

import fractions
import math
primesAndNums={}
primesAndNums["primes"]=[]
primesAndNums["powerful"]=[]
primesAndNums["perfectPowers"]=set()
primesAndNums["achillesNums"]=[]
primesAndNums['strongAchillesNums']=[]
primesAndNums["totients"]={}
primesAndNums['factors']={}

def newDD():
    primesAndNums={}
    primesAndNums["primes"]=[]
    primesAndNums["powerful"]=[]
    primesAndNums["perfectPowers"]=[]
    primesAndNums["achillesNums"]=[]
    primesAndNums['strongAchillesNums']=[]
    primesAndNums["totients"]={}
    primesAndNums['factors']={}



def isPrime(number):
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

def test(anum):
    newDD()
    x = 0
    findAllPerfectRoots(anum)
    # primesAndNums = newDD()
    while(x<anum-1):
        x+=1
        if isPrime(x):
            primesAndNums['primes'].append(x)
        else:
            primesAndNums['factors'][x]= breakUpToPrimes(x)
            # Determine if is powerful
            powers=primesAndNums['factors'][x].values()
            isPowerful = not(1 in powers)
            if isPowerful:
                primesAndNums['powerful'].append(x)
            # Determin if is perfect
            isPerfect= x in primesAndNums['perfectPowers']
            isAchilles = (isPowerful and not(isPerfect))
            if isAchilles:
                if len(primesAndNums['factors'][x].keys())>1:
                    print str(x) + " has been found to be an Achilles number"
                    primesAndNums['achillesNums'].append(x)
                    primesAndNums['totients'][x]=countTotient(x)
                    if (primesAndNums['totients'][x] in primesAndNums['achillesNums']):
                        print str(x) + " has been found to be a strongAchilles number"
                        primesAndNums['strongAchillesNums'].append(x)
    return primesAndNums


if __name__ == '__main__':
    results = test(10**8)
    print len(results['strongAchillesNums'])