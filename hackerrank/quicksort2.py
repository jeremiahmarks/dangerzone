
#from https://www.hackerrank.com/challenges/quicksort2



def partition(ar):
	m=ar[0]  
	lesser=[]
	greater=[]
	for value in ar:
		if (value<m):
			lesser.append(value)
		if (value>m):
			greater.append(value)
	if (len(lesser)>1):
		lesser=partition(lesser)
	if (len(greater)>1):
		greater=partition(greater)
	partitioned=lesser+[m]+greater
	print str(partitioned).replace('[','').replace(']','').replace(',','')+"\n"
	return partitioned

	

m = int(input())
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)