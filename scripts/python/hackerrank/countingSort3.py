
#from https://www.hackerrank.com/challenges/countingsort3

def countingsort(ar):
	results=[]
	retString=""
	runningTotal=0
	for x in range(100):
		results.append(ar.count(x))
	for y in range(len(results)):
		runningTotal+=results[y]
		retString +=str(runningTotal)+" "
	return retString


m = input()
ar=[]
for x in range(m):
	ar.append(int(raw_input().split()[0]))

print str(countingsort(ar)).replace('[','').replace(']','').replace(',','')