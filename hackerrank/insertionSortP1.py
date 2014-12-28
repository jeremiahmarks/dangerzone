#!/bin/python
#from https://www.hackerrank.com/challenges/insertionsort1

def insertionSort(ar):
	elementToPlace=ar[-1]
	lengthOfArray=len(ar)
	placed = False
	strToReturn=""
	for place in range(2,len(ar)+1):
		if (ar[-place]>elementToPlace):
			ar[-(place-1)]=ar[-place]
		elif ((ar[-place]<elementToPlace) and not placed):
			ar[-(place-1)]=elementToPlace
			placed=True
		strToReturn+=str(ar).replace('[','').replace(']','').replace(',','')+"\n"
	return strToReturn

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)