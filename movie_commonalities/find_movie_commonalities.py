#!/usr/bin/python
"""
  find_movie_commonalities.py

  Finds common properties from an arbitrary set of movies.

  Example Usage:
    python find_movie_commonalities.py "happy gilmore" "billy madison"
      Rated: PG-13
      Writer: Adam Sandler,Tim Herlihy
      Actors: Adam Sandler
      Genre: Romance,Comedy

  @author Dan Muriello dan@muriello.net
"""

from json import loads
from sys import argv
from urllib import urlencode
from urllib2 import urlopen, Request

api_url = 'http://www.imdbapi.com/'

def main() :
    if len(argv) == 1:
        print 'usage: blah.py "movie0" "movie1" "movie2"  ...'
        exit()

    queries = argv[1:]
    query_info = {}
    for query in queries:
        query_info[query] = getInfoForQuery(query)

    commonalities = findCommonalities(query_info)
    printCommonalities(commonalities)

def getInfoForQuery(query, apiversion=1):
    params = {'i' : '', 't' : query}
    data = urlencode(params)
    uri = api_url + '?' + data
    req = Request(uri)
    content = urlopen(req).read()

    info = loads(content)

    # remove meaningless key(s)
    if 'Response' in info:
        del info['Response']

    return info
    
def findCommonalities(query_info):
    """
    Query info here will be a map from query to fetched info
info:  {u'Plot': u'A look at a few chapters in the life of Poppy, a cheery, colorful, North London schoolteacher whose optimism tends to exasperate those around her.', u'Votes': u'15954', u'Rated': u'R', u'Response': u'True', u'Title': u'Happy-Go-Lucky', u'Poster': u'http://ia.media-imdb.com/images/M/MV5BMTI4ODY1MjIyNV5BMl5BanBnXkFtZTcwMTExMTM5MQ@@._V1._SX320.jpg', u'Writer': u'Mike Leigh', u'ID': u'tt1045670', u'Director': u'Mike Leigh', u'Released': u'18 Apr 2008', u'Actors': u'Sally Hawkins, Alexis Zegerman, Samuel Roukin, Elliot Cowan', u'Year': u'2008', u'Genre': u'Comedy, Drama', u'Runtime': u'1 hr 58 mins', u'Rating': u'7.0'}

    """
    if len(query_info) == 0:
        return {}

    properties = query_info.values()[0].keys()

    """
    {
      actors : [[], []],
      directors : [[''], ['']]
    }
    """
    property_lists = {}

    for query,info in query_info.iteritems():
        for property, propvalue in info.iteritems():
            if property not in property_lists:
                property_lists[property] = []
            if property != 'Plot':
                prop_value_parts = map(lambda x : x.strip(), propvalue.split(','))
            else:
                prop_value_parts = [propvalue]
            property_lists[property].append(prop_value_parts)

    commonalities = {}

    for property, propvalue_sets in property_lists.iteritems():
        accumulator_propset = set()
        new = True
        for propvalue_set in propvalue_sets:
            if new:
                """
                This is the first of the queries, populate the accumulator
                """
                accumulator_propset = set(propvalue_set)
                new = False
            else:
                """
                Not the first, do an intersection
                """
                accumulator_propset = accumulator_propset.intersection(set(propvalue_set))

        if len(accumulator_propset) > 0:
            commonalities[property] = accumulator_propset

    return commonalities
        
def printCommonalities(commonalities):
    if len(commonalities) == 0:
        print 'These things have nothing in common.'
        return
        
    for property, propset in commonalities.iteritems():
        print '  %s: %s' % (property, ','.join(list(propset)))

    return

if __name__ == '__main__':
    main()
