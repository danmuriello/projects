"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

triples = []
for i in xrange(1001):
	for j in xrange(1001):
		for k in xrange(1001):
			if i<j and j<k and i+j+k == 1000 and (i**2 + j**2) == k**2:
				triples.append((i,j,k))
t =  triples[0]
print t[0]*t[1]*t[2]