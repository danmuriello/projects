"""
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of 
the numbers from 1 to 20?

"""

gotit = False
x = 1
while not gotit:
	if x % 100000 == 0:
		print x
	gotit = True
	for i in xrange(1,16):
		gotit = gotit and (x % i == 0)
	if gotit:
		print x
	else:
		x += 1