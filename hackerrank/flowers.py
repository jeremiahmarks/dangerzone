

# from https://www.hackerrank.com/challenges/flowers

# Problem Statement

# You and your K-1 friends want to buy N flowers. Flower number i has cost ci. 
# Unfortunately the seller does not want just one customer to buy a lot of 
# flowers, so he tries to change the price of flowers for customers who have 
# already bought some flowers. More precisely, if a customer has already bought 
# x flowers, he should pay (x+1)*ci dollars to buy flower number i.

# You and your K-1 friends want to buy all N flowers in such a way that you spend 
# the least amount of money. You can buy the flowers in any order.

# Input:

# The first line of input contains two integers N and K (K <= N). The next line 
# contains N space separated positive integers c1,c2,...,cN.

# Output:

# Print the minimum amount of money you (and your friends) have to pay in order 
# to buy all N flowers.

# sample Input
# 3 3    ## 3 flowers want to be bought. There are three people including me
# 2 5 6  ## prices .. since we want to buy three flowers, each person would buy one.


# sample Input
# 3 2  	## 3 flowers to be purchased between two people
# 2 5 6  ## one person purchases the most expensive first, and then the cheapest next.

flowersToPurchase, numberOfCustomers = map(int, raw_input().split())
prices = sorted(map(int, raw_input().split()))

totalSpent=0

if (flowersToPurchase==numberOfCustomers):
	totalSpent=sum(prices[:numberOfCustomers])
else:
	
