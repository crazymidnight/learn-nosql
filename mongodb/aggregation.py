from pymongo import MongoClient


client = MongoClient()

db = client.phonebook

"""
Calculate the number of people in your phone book who have a birthday this month
using the aggregation function and map reduce
"""
# Aggregation 
# It should be like that: db.records.aggregate({$project: {month: {$month: "$date_of_birth"}}})
pipeline = [
    {"$match": {"$month: $date_of_birth": 4}},
]
cursor = db.records.aggregate([]).count()
# Map-reduce

