
#from https://www.hackerrank.com/challenges/insertionsort2











def insertionSort(ar):
	returnString=""
	for x in range(1,len(ar)):
		valueToSort=ar[x]
		currentPosition=x
		while (currentPosition>0 and (ar[currentPosition-1]>valueToSort)):
			ar[currentPosition]=ar[currentPosition-1]
			currentPosition-=1
		ar[currentPosition]=valueToSort
		returnString+=str(ar).replace('[','').replace(']','').replace(',','')+"\n"
	return returnString


m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)