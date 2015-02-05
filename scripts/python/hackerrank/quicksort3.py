
# from  https://www.hackerrank.com/challenges/quicksort3

# Fails from test case 1
# Test Case 1 input:
# 9
# 9 8 6 7 3 5 4 1 2
# Test case 1 expected output:
# 1 2 6 7 3 5 4 9 8
# 1 2 6 7 3 5 4 8 9
# 1 2 3 4 6 5 7 8 9
# 1 2 3 4 6 5 7 8 9
# 1 2 3 4 5 6 7 8 9
# Test case 1 actual output:
# 1 2 6 7 3 5 4 9 8
# 1 2 6 7 3 5 4 9 8
# 1 2 3 4 6 5 7 8 9

def swapPositions(ar, pos1, pos2):
	val1=ar[pos1]
	ar[pos1]=ar[pos2]
	ar[pos2]=val1
	print str(ar).replace('[','').replace(']','').replace(',','')


def quicksortInPlace(ar,startLoc=0, endLoc=None):
	if (endLoc==None):
		endLoc=len(ar)-1
	#print str(ar).replace('[','').replace(']','').replace(',','') + " " + str(startLoc) + " " + str(endLoc)
	#raw_input('waiting')
	pivotValue=ar[endLoc]
	#print "pivot: " + str(pivotValue)
	for location in range(startLoc,endLoc+1):
		locVal=ar[location]
		#print "locval: " + str(locVal)
		if (locVal<pivotValue):
			#print "less than"
			pass
		elif (locVal==pivotValue):
			#print "switchingThePivots"
			pivoted=False
			for newLocation in range(startLoc,endLoc+1):
				if ((ar[newLocation]>=pivotValue) and not(pivoted)):
					swapPositions(ar,newLocation,endLoc)
					pivoted=True
					if ((newLocation - startLoc)>1):
						quicksortInPlace(ar,startLoc=startLoc, endLoc=newLocation-1)
					if ((endLoc - newLocation)>1):
						quicksortInPlace(ar,startLoc=newLocation+1, endLoc=endLoc)
		else:
			#print "else"
			currentLocation = location + 1
			placed = False
			while ((not placed) and (currentLocation<endLoc)):
				if (ar[currentLocation]<pivotValue):
					currentLocationValue=ar[currentLocation]
					ar[currentLocation] = ar[location]
					ar[location] = currentLocationValue
					placed = True
				currentLocation+=1
	return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quicksortInplace(ar,m)