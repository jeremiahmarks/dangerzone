##from http://www.geeksforgeeks.org/check-number-fibonacci-number/

def isPerfSquare(x):
	return(int(x**(0.5))**2==x)

def isFib(x):
	return (isPerfSquare(5*x*x+4) or isPerfSquare(5*x*x-4))
	