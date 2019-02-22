from pymongo import MongoClient
import json


with open("sample.json") as f:
    users = [x for x in json.load(f)]

client = MongoClient()

db = client.phonebook

db.records.insert_many(users)
