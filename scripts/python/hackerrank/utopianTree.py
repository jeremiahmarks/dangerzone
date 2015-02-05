# Problem Statement

# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. 
# Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

# Input Format 
# The first line contains an integer, T, the number of test cases. 
# T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

# Constraints 
# 1 <= T <= 10 
# 0 <= N <= 60

# Output Format 
# For each test case, print the height of the Utopian tree after N cycles.



numOfInput=int(raw_input())
retString=""
for x in range(numOfInput):
	height=1
	doubleGrowth=True
	numberOfGrowthSeasons=int(raw_input())
	for x in range(numberOfGrowthSeasons):
		if doubleGrowth:
			height=height*2
		else:
			height+=1
		doubleGrowth = not doubleGrowth
	retString += str(height) + "\n"
print retString


