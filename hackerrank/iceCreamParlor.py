
#from https://www.hackerrank.com/challenges/icecream-parlor

t = int(input()) # m= number of test cases

for eachCase in range(t):
	m=int(raw_input()) # m = amount of money to spend
	n=int(raw_input()) # n = number of flavors
	ar=map(int, raw_input().strip().split(" "))
	for f1 in range(len(ar)):
		for f2 in range(f1+1,len(ar)):
			if (ar[f1]+ar[f2]==m):
				print str(f1+1) + " " + str(f2+1)


