
numOfInput=int(raw_input())
retString=""
def isPerfSquare(x):
	return(int(x**(0.5))**2==x)

def isFib(x):
	return (isPerfSquare(5*x*x+4) or isPerfSquare(5*x*x-4))
for x in range(numOfInput):
	numToCheck=int(raw_input())
	if (isFib(numToCheck)):
		retString += "IsFibo"+"\n"
	else:
		retString += "IsNotFibo"+"\n"

print retString