"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.

"""

x = 0
for i in xrange(1,101):
	x += i**2

y = 0
for i in xrange(1,101):
	y += i
y = y**2

print y-x
