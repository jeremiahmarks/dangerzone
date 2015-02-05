
# from https://www.hackerrank.com/challenges/pangrams

stringToTest=raw_input().lower()
pangram=True
for x in range(26):
	if (stringToTest.count(chr(97+x))==0):
		pangram=False
		break
if pangram:
	print "pangram"
else:
	print "not pangram"
