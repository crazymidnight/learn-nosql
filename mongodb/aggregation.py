from pymongo import MongoClient
from pprint import pprint
from datetime import datetime


client = MongoClient()

db = client.phonebook

"""
Calculate the number of people in your phone book who have a birthday this month
using the aggregation function and map reduce
"""

# Aggregation 
pipeline = [
    {"$project": {"month": {"$month": "$date_of_birth"}}},
    {"$match": {"month": datetime.now().month}},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}}
]
cursor = db.records.aggregate(pipeline)
for i in cursor:
    number = i
print(f"Number of people who born at {datetime.now().month}: {number['count']}")

# Map-reduce
