
# from  https://www.hackerrank.com/challenges/quicksort3

def swapPositions(ar, pos1, pos2):
	val1=ar[pos1]
	ar[pos1]=ar[pos2]
	ar[pos2]=val1
	return ar


def quicksortInplace(ar):
	piv=ar[-1]
	for location in range(len(ar)):
		if (ar[location]<piv):
			break
		elif (ar[location]==piv):
			for x in range(len(ar)):
				if (ar[x]>piv):
					ar=swapPositions(ar,x,-1)
					if (len(ar[:x])>1):
						ar=quicksortInplace(ar[:x])+ar[x:]
					if (len(ar[x:])>1):
						ar=ar[:x]+quicksortInplace(ar[x:])
			print ar
		else:
			curloc=location+1
			placed=False
			while ((not placed) and (curloc<len(ar))):
				if (ar[curloc]<piv):
					curlocval=ar[curloc]
					ar[curloc]=ar[location]
					ar[location]=curlocval
					placed=True
				curloc+=1
	return ar

