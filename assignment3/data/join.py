import MapReduce
from pprint import pprint as pp
import sys
import json

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    len_values = len(list_of_values)    
    orders_to_join = {}
    items_joining = {}

    for i in range(1,len_values):
        orders_to_join[i - 1] = list_of_values[0]
        items_joining[i - 1] = list_of_values[i]

    for key in orders_to_join.iterkeys():
        mr.emit(orders_to_join[key] + items_joining[key])

input_data = open(sys.argv[1],'r')

mr.execute(input_data, mapper, reducer)

# pp(len(mr.result[0]))


# for line in input_data:
#     record = json.loads(line)
#     mapper(record)
    
# pp(mr.intermediate)