from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import Code


client = MongoClient()

db = client.phonebook

"""
Calculate the number of people in your phone book who have a birthday this month
using the aggregation function and map reduce
"""

current_month = datetime.now().month

# Aggregation
pipeline = [
    {"$project": {"month": {"$month": "$date_of_birth"}}},
    {"$match": {"month": current_month}},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
]
cursor = db.records.aggregate(pipeline)
for i in cursor:
    number = i
print(f"Number of people who born at {current_month}: {number['count']}")

# Map-reduce

mapper = Code(
    """
    function map() {
        for(i in this.date_of_birth) {
		    emit(this.date_of_birth.getMonth(), 1);
	    }
    }
    """
)

reducer = Code(
    """
    function reduce(key, values) {
        var sum = 0;
	    for(var i in values) {
            sum += values[i];
	    }
	    return sum;
    }
    """
)

result = int(
    db.records.map_reduce(mapper, reducer, "myresult").find()[current_month - 1][
        "value"
    ]
)

print(f"Number of people who born at {current_month}: {result}")
