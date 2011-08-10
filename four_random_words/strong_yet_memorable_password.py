##
# Strong Yet Memorable Password Generator
#
# Fetches the New York Times home page, extracts
# link anchor text, and chooses 4 random words
# from this set of words. Operates on the assumption
# that nyt authors use only commonplace words which
# are easy to understand and remember.
#
# Does other things like lowercasing and alphanumeric
# character filtering.
#
# Based on http://xkcd.com/936/
#
# @author Dan Muriello dan@muriello.net

from urllib import urlopen
from re import findall, sub
from random import sample

url = 'http://www.nytimes.com/'
c = urlopen(url).read()
links = findall('<a.*?>([\w\s]*?)</a>', c)
lc = ' '.join(links).lower()
random_link_words = sample(sub('[^a-z\s]', '', lc).split(), 4)

print random_link_words
print ''.join(random_link_words)



