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

    joined_records = []
    for key in orders_to_join.iterkeys():
        joined_records.append(orders_to_join[key] + items_joining[key])
    # pp(joined_records)

    mr.emit(joined_records)

input_data = open(sys.argv[1],'r')

mr.execute(input_data, mapper, reducer)

# pp(len(mr.result))


# for line in input_data:
#     record = json.loads(line)
#     mapper(record)
    
# pp(mr.intermediate)