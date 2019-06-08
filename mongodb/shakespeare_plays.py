from pymongo import MongoClient
from pprint import pprint
import json


shakespeare = []
for line in open("../shakespeare_plays.json", "r"):
    shakespeare.append(json.loads(line))

client = MongoClient()

db = client.shakespeare

db.plays.remove()

db.plays.insert_many(shakespeare)

"""
Find the scene with the largest number of
replicas. (the name of the play, act and scene).
"""

pipeline = [
    {"$unwind": "$acts"},
    {"$unwind": "$acts.scenes"},
    {"$unwind": "$acts.scenes.action"},
    {
        "$project": {
            "lines": {"$size": "$acts.scenes.action.says"},
            "play": "$_id",
            "act": "$acts.title",
            "scene": "$acts.scenes.title",
        }
    },
    {
        "$group": {
            "_id": {"play": "$play", "act": "$act", "scene": "$scene"},
            "lines": {"$sum": "$lines"},
        }
    },
    {"$sort": {"lines": -1}},
    {"$limit": 1},
]
cursor = list(db.plays.aggregate(pipeline))

pprint(cursor)

"""
Number of acts and scenes in each play.
"""

pipeline = [
    {"$unwind": "$acts"},
    {
        "$project": {
            "play": "$_id",
            "acts": {"$add": 1},
            "scenes": {"$size": "$acts.scenes"},
        }
    },
    {
        "$group": {
            "_id": "$play",
            "acts": {"$sum": "$acts"},
            "scenes": {"$sum": "$scenes"},
        }
    },
]
cursor = list(db.plays.aggregate(pipeline))

pprint(cursor)

"""
A list of characters for each play, sorted
alphabetically.
"""

pipeline = [
    {"$unwind": "$acts"},
    {"$unwind": "$acts.scenes"},
    {"$unwind": "$acts.scenes.action"},
    {
        "$group": {
            "_id": "$_id",
            "characters": {"$addToSet": "$acts.scenes.action.character"},
        }
    },
    {"$unwind": "$characters"},
    {"$sort": {"characters": 1}},
    {"$group": {"_id": "$_id", "characters": {"$push": "$characters"}}},
]
cursor = list(db.plays.aggregate(pipeline))
pprint(cursor)

"""
How many replicas does Juliette have?
"""

pipeline = [
    {"$unwind": "$acts"},
    {"$unwind": "$acts.scenes"},
    {"$unwind": "$acts.scenes.action"},
    {
        "$project": {
            "lines": {"$add": [1]},
            "character": "$acts.scenes.action.character",
        }
    },
    {"$group": {"_id": "$character", "lines": {"$sum": "$lines"}}},
    {"$match": {"_id": "JULIET"}},
]
cursor = list(db.plays.aggregate(pipeline))
pprint(cursor)

"""
What characters occur in more than one play?
"""

pipeline = [
    {"$unwind": "$acts"},
    {"$unwind": "$acts.scenes"},
    {"$unwind": "$acts.scenes.action"},
    {"$project": {"play": "$_id", "character": "$acts.scenes.action.character"}},
    {"$unwind": "$character"},
    {"$group": {"_id": "$character", "plays": {"$addToSet": "$play"}}},
    {
        "$project": {
            "character": "$_id",
            "plays": "$plays",
            "count": {"$size": "$plays"},
        }
    },
    {"$match": {"count": {"$gt": 1}}},
]
cursor = list(db.plays.aggregate(pipeline))
pprint(cursor)

"""
For each play, find a character who has the
largest number of replicas.
"""

pipeline = [
    {"$unwind": "$acts"},
    {"$unwind": "$acts.scenes"},
    {"$unwind": "$acts.scenes.action"},
    {
        "$project": {
            "play": "$_id",
            "character": "$acts.scenes.action.character",
            "lines": {"$add": [1]},
        }
    },
    {
        "$group": {
            "_id": {"play": "$play", "character": "$character"},
            "lines": {"$sum": "$lines"},
        }
    },
    {"$sort": {"lines": -1}},
    {
        "$group": {
            "_id": "$_id.play",
            "character": {"$first": "$_id.character"},
            "lines": {"$first": "$lines"},
        }
    },
    {
        "$project": {
            "play": "$_id",
            "character": "$character",
            "number of lines": "$lines",
        }
    },
]

cursor = list(db.plays.aggregate(pipeline))
pprint(cursor)
