

# from https://www.hackerrank.com/challenges/circle-city


t = int(raw_input()) # number of test cases

for x in range(t):
	placesNeeded=0
	radiusSquared,numberOfStations = map(int,raw_input().split())
	radius = int(radiusSquared**0.5)
	for x in range(radius):
		if ((int((radiusSquared-(x**2))**0.5))**2==(radiusSquared-(x**2))):
			placesNeeded+=4
	if (placesNeeded<=numberOfStations):
		print "possible"
	else:
		print "impossible"
