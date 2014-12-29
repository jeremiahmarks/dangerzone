
# from  https://www.hackerrank.com/challenges/quicksort3

def swapPositions(ar, pos1, pos2):
	val1=ar[pos1]
	ar[pos1]=ar[pos2]
	ar[pos2]=val1
	return ar


def quicksortInplace(ar,n):
	retString=""
	piv=ar[-1]
	for location in range(len(ar)):
		if (ar[location]<piv):
			pass
		elif (ar[location]==piv):
			for x in range(len(ar)):
				if (ar[x]>piv):
					ar=swapPositions(ar,x,-1)
					if (len(ar)==n):
						retString+= str(ar).replace('[','').replace(']','').replace(',','')+"\n"
					if (len(ar[:x])>1):
						ar=quicksortInplace(ar[:x],n)+ar[x:]
					if (len(ar)==n):
						retString+= str(ar).replace('[','').replace(']','').replace(',','')+"\n"
					if (len(ar[x:])>1):
						ar=ar[:x]+quicksortInplace(ar[x:],n)
					if (len(ar)==n):
						retString+= str(ar).replace('[','').replace(']','').replace(',','')+"\n"
					break
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
	if (len(ar)==n):
		print retString
	else:
		return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quicksortInplace(ar,m)