"""
Consider the set of all positive integers which are n digits long.
What is the probability that a number drawn randomly from this set
contains the number 4 as one of its digits?

Dan Muriello dan@muriello.net
"""

def experimental(n = 2):
    total = 0
    fours = 0
    for i in xrange(10**(n-1), 10**n):
        total += 1
        for j in xrange(1, n+1):
            if nth_digit(i, j) == 4:
                #print i
                fours += 1
    return float(fours) / float(total)

def nth_digit(x, n):
    return (x % (10**n)) / 10**(n-1)

def theoretical(n):
    return (1.0 / 9) + (0.1 * (n-1))

if __name__ == '__main__':
    n = 7
    ex = experimental(n)
    th = theoretical(n)

    print 'experimental:', ex
    print 'theoretical:', th
