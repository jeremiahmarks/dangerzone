
# from https://www.hackerrank.com/challenges/quicksort1

# You're given an array ar and a number p. Partition the array, so that, all elements greater than p are to its right, and all elements smaller than p are to its left.

# In the new sub-array, the relative positioning of elements should remain the same, i.e., if n1 was before n2 in the original array, it must remain before it in the sub-array. The only situation where this does not hold good is when p lies between n1 and n2

# i.e., n1 > p > n2.

# Guideline - In this challenge, you do not need to move around the numbers 'in-place'. This means you can create 2 lists and combine them at the end.

def partition(ar):
	m=ar[0]  
	p1=[]
	p2=[]
	for value in ar:
		if (value<m):
			p1.append(value)
		else:
			p2.append(value)
	print str(p1+p2).replace('[','').replace(']','').replace(',','')+"\n"

m = int(input())
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)