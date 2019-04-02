from pymongo import MongoClient
import json
import datetime


with open("../sample.json") as f:
    users = [x for x in json.load(f)]

for user in users:
    user["date_of_birth"] = datetime.datetime.strptime(
        user["date_of_birth"], "%d/%m/%Y"
    )

client = MongoClient()

db = client.phonebook

db.records.remove()

db.records.insert_many(users)
