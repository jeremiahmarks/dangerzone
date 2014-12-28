
#from https://www.hackerrank.com/challenges/tutorial-intro

# Sample Challenge 
# This is a simple challenge to get things started. Given a sorted array (ar) and a number (V), can you print the index location of V in the array?

# {The next section describes the input format. You can often skip it, if you are using included methods. }

# Input Format 
# There will be three lines of input:

# V - the value that has to be searched.
# n - the size of the array.
# ar - n numbers that make up the array.
# Output Format 
# Output the index of V in the array.

# {The next section describes the constraints and ranges of the input. You should check this section to know the range of the input. }

# Constraints 
# 1<=n<=1000 
# -1000 <=x <= 1000 , x ∈ ar

# {This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge. }


searchValue=int(raw_input())
arraySize=int(raw_input())
array=[int(i) for i in raw_input().strip().split()]

print array.index(searchValue)