

# from https://www.hackerrank.com/challenges/quicksort4


# In practice, how much faster is Quicksort (in-place) than Insertion Sort? 
# Compare the running time of the two algorithms by counting how many swaps or shifts 
# each one takes to sort an array, and output the difference. You can modify your previous 
# sorting code to keep track of the swaps. The number of swaps required by Quicksort to 
# sort any given input have to be calculated. Keep in mind that the last element of a block 
# is chosen as the pivot, and that the array is sorted in-place as demonstrated in the explanation below.

# Any time a number is smaller than the partition, it should be "swapped", 
# even if it doesn't actually move to a different location. Also ensure that you 
# count the swap when the pivot is moved into place. The count for Insertion Sort 
# should be the same as the previous challenge, where you just count the number of "shifts".
def swapPositions(ar, pos1, pos2):
	val1=ar[pos1]
	ar[pos1]=ar[pos2]
	ar[pos2]=val1

def quicksortInPlace(ar,startLoc=0, endLoc=None):
	swaps=0
	if (endLoc==None):
		endLoc=len(ar)-1
	pivotValue=ar[endLoc]
	for location in range(startLoc,endLoc+1):
		locVal=ar[location]
		if (locVal<pivotValue):
			swaps+=1
			pass
		elif (locVal==pivotValue):
			pivoted=False
			for newLocation in range(startLoc,endLoc+1):
				if ((ar[newLocation]>=pivotValue) and not(pivoted)):
					swapPositions(ar,newLocation,endLoc)
					swaps+=1
					pivoted=True
					if ((newLocation - startLoc)>1):
						swaps+=quicksortInPlace(ar,startLoc=startLoc, endLoc=newLocation-1)
					if ((endLoc - newLocation)>1):
						swaps+=quicksortInPlace(ar,startLoc=newLocation+1, endLoc=endLoc)
		else:
			currentLocation = location + 1
			placed = False
			while ((not placed) and (currentLocation<endLoc)):
				if (ar[currentLocation]<pivotValue):
					currentLocationValue=ar[currentLocation]
					ar[currentLocation] = ar[location]
					ar[location] = currentLocationValue
					swaps+=1
					placed = True
				currentLocation+=1
	return swaps

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
		
	return shifts

m = input()
ar = [int(i) for i in raw_input().strip().split()]
br=[]
for value in ar:
	br.append(value)
a=insertionSort(ar)
b=quicksortInPlace(br)
print a-b