
from math import sqrt

def isprime(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	
	for i in xrange(2,int(sqrt(x))+1):
		if x % i == 0:
			return False
	return True

def factors(x):
	fs = []
	for i in xrange(1,int(x/2)+1):
		if x % i == 0:
			fs.append(i)
	fs.append(x)
	return fs
	