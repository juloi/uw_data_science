import MapReduce
import sys
from pprint import pprint as pp

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate((record[0], record[1]), 1)
    mr.emit_intermediate((record[1], record[0]), -1)

    # mr.emit_intermediate((record[0], record[1]), (record[1], record[0]))

def reducer(key, list_of_values):
    counter = 0
    for value in list_of_values:
        counter += value

    if counter < 0:
        mr.emit(key)
        mr.emit((key[1], key[0]))

    # friendships = {}
    # friendships[key] = list_of_values[0]
    # pp(friendships)

    # inversed_values = []
    # for key in friendships.iterkeys():
        # inversed_values.append(friendships[key][0])
        # pp(inversed_values)

    # for val in friendships.itervalues():
    #     if val not in friendships:
    #         pp(val)
        # else:
        #     mr.emit(val)

    # for key, val in friendships.iteritems():
    #     try:
    #         friendships[val]
    #     except KeyError:
    #         continue
            # mr.emit(key)
            # mr.emit(val)

data = open(sys.argv[1], 'r')

mr.execute(data, mapper, reducer)