import math
import time

def problemtwelve():
	range = [0,-.5,-.9,-.95,-.99,-.999,-2,-1.5,-1.1,-1.01,-1.001]
	for xvalue in range:
		numerator = (math.pow(xvalue,2))-2*x
		deno = math.pow(xvalue,2)-xvalue-2
		ffunction=numerator/deno
		print ("xvalue: %n f(x): %n" %xvalue,ffunction)
	time.sleep(100)