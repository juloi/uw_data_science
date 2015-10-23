import MapReduce
import sys
from pprint import pprint as pp

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate((record[0], record[1]), (record[1], record[0]))

def reducer(key, list_of_values):
    friendships = {}
    friendships[key] = list_of_values[0]

    for key, val in friendships.iteritems():
        try:
            friendships[val]
        except KeyError:
            mr.emit(key)
            mr.emit(val)

data = open(sys.argv[1], 'r')

mr.execute(data, mapper, reducer)