import MapReduce
from pprint import pprint as pp
import sys
import json

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0]
    person_friend = record[1]
    mr.emit_intermediate(person, person_friend)

def reducer(key, list_of_values):
    mr.emit((key, len(list_of_values)))
    # for person in list_of_values.iterkeys():
    #     pp(person)
        # mr.emit(list((person, len(list_of_values[person]))))

input_data = open(sys.argv[1], 'r')

mr.execute(input_data, mapper, reducer)