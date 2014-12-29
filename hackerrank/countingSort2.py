
# from https://www.hackerrank.com/challenges/countingsort2



def countingsort(ar):
	results=[]
	retString=""
	for x in range(100):
		results.append(ar.count(x))
	for y in range(len(results)):
		if (results[y]==0):
			pass
		else:
			for t in range(results[y]):
				retString +=str(y)+" "
	return retString


m = input()
ar = [int(i) for i in raw_input().strip().split()]
print str(countingsort(ar)).replace('[','').replace(']','').replace(',','')