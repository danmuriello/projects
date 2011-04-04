"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91  99. 

Find the largest palindrome made from the product of two 
3-digit numbers.
"""

def nthDigit(n,x):
	return ((x % (10**n)) - (x % (10**(n-1)))) / (10**(n-1))	

def numdigits(x):
	if x < 0:
		x = -1 * x
	
	d = 0
	while x >= (10**d):
		d += 1
	
	return d
	
def ispalindrome(x):
	d = numdigits(x)
	
	u = d
	l = 1
	palsofar = True
	while u > (d/2.0):
		if nthDigit(u,x) == nthDigit(l,x):
			palsofar = palsofar and True
		else:
			palsofar = palsofar and False
		u -= 1
		l += 1
		
	return palsofar

c = 0
pal = 0	
for i in range(10,1000):
	for j in range(10,1000):
		c += 1
		z = i*j
		#print i,j,z
		if ispalindrome(z) and z > pal:
			pal = z
			print pal,'=',i,'*',j

