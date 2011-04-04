"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from commons import isprime

primes = []
for i in xrange(2,2000000+1):
	if isprime(i):
		primes.append(i)
		
total = 0
for p in primes:
	total += p

print primes
print total