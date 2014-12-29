
# from https://www.hackerrank.com/challenges/closest-numbers

def swapPositions(ar, pos1, pos2):
	val1=ar[pos1]
	ar[pos1]=ar[pos2]
	ar[pos2]=val1


def quicksortInPlace(ar,startLoc=0, endLoc=None):
	if (endLoc==None):
		endLoc=len(ar)-1
	pivotValue=ar[endLoc]
	for location in range(startLoc,endLoc+1):
		locVal=ar[location]
		if (locVal<pivotValue):
			pass
		elif (locVal==pivotValue):
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
			currentLocation = location + 1
			placed = False
			while ((not placed) and (currentLocation<endLoc)):
				if (ar[currentLocation]<pivotValue):
					currentLocationValue=ar[currentLocation]
					ar[currentLocation] = ar[location]
					ar[location] = currentLocationValue
					placed = True
				currentLocation+=1

n=int(raw_input())

ar=map(int,raw_input().strip().split(" "))
quicksortInPlace(ar)

answer=[[ar[0],ar[1],abs(ar[0]-ar[1])],]

for v1 in range(len(ar)-1):
	if (abs(ar[v1]-ar[v1+1])<answer[0][2]):
		answer = []
		answer.append([ar[v1],ar[v1+1],abs(ar[v1]-ar[v1+1])])
	elif(abs(ar[v1]-ar[v1+1])==answer[0][2]):
		answer.append([ar[v1],ar[v1+1],abs(ar[v1]-ar[v1+1])])

for eachsolution in answer:
	print (str(eachsolution[0]) + " " + str(eachsolution[1])),
