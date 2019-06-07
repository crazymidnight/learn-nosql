from pymongo import MongoClient, ASCENDING, TEXT, IndexModel
import json
import datetime


with open("../sample.json") as f:
    users = json.load(f)

for user in users:
    user["date_of_birth"] = datetime.datetime.strptime(
        user["date_of_birth"], "%d/%m/%Y"
    )

client = MongoClient()

db = client.phonebook

db.records.remove()
db.records.drop_indexes()

db.records.insert_many(users)

index_name = IndexModel(
    [("first_name", TEXT), ("last_name", TEXT)], name="search_by_name"
)

index_phone = IndexModel([("phone", ASCENDING)], name="by_phone", unique=True)

db.records.create_indexes([index_name, index_phone])

print(sorted(list(db.records.index_information())))
