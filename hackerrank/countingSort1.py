
# from https://www.hackerrank.com/challenges/countingsort1



def countingsort(ar):
	results=[]
	for x in range(100):
		results.append(ar.count(x))
	return results


m = input()
ar = [int(i) for i in raw_input().strip().split()]
print str(countingsort(ar)).replace('[','').replace(']','').replace(',','')