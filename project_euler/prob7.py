"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
from math import sqrt,floor

def isprime(x):
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	
	for i in xrange(2,x):
		if x % i == 0:
			return False
	return True

def nthprime(n):
	
	c = 0
	x = 1
	while c < n:
		x += 1
		if isprime(x):
			c += 1
	return x

print nthprime(10001)