
#from https://www.hackerrank.com/challenges/countingsort4

def countingsort(ar):
	results=[[] for i in range(100)]
	for place,value in ar:
		results[place].append(value)
	retString= sun(results,[])
	print ''.join(retString)
	# for x in range(arrayLength):
	# 	theValue=ar[x]
	# 	if (x<firstHalf):
	# 		theValue[1]="-"
	# 	theValue[0]=int(theValue[0])
	# 	justNumbers.append(theValue[0])
	# vals=sorted(ar, key=lambda values:values[0])
	# for eachPart in vals:
	# 	print (eachPart[1]),
	# for z in range(100):
	# 	num=(justNumbers.count(z))
	# 	if (num==0):
	# 		pass
	# 	else:
	# 		for time in range(num):
	# 			thisValue=next(p for p in ar if(p[0]==z))
	# 			print (thisValue[1]),
	# 			ar.remove(thisValue)
	





m = input()
ar=[]
for x in range(m):
	t=raw_input().split()
	if x<m/2:
		ar.append([int(t[0]), "-"])
	else:
		ar.append([int(t[0]), t[1]])

countingsort(ar)