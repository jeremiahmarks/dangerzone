
#from https://www.hackerrank.com/challenges/runningtime











def insertionSort(ar):
	shifts=0
	for x in range(1,len(ar)):
		valueToSort=ar[x]
		currentPosition=x
		while (currentPosition>0 and (ar[currentPosition-1]>valueToSort)):
			ar[currentPosition]=ar[currentPosition-1]
			shifts+=1
			currentPosition-=1
		ar[currentPosition]=valueToSort
		
	return str(shifts)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)