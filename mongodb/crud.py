from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.phonebook

# Create

db.records.insert_one(
    {
        "first_name": "Harry",
        "last_name": "Potter",
        "gender": "Male",
        "email": "hpotter@hw.com",
        "workplace": "Ministry of Magic",
        "university": "Hogwarts",
        "hobby": "Magic",
        "date_of_birth": "31-09-1980",
    }
)

cursor = db.records.find({"last_name": "Potter"})
for i in cursor:
    pprint.pprint(i)

# Read

cursor = db.records.find({"gender": "Male"})
for i in cursor:
    pprint.pprint(i)

# Update

db.records.update_one(
    {"last_name": "Potter"}, {"$set": {"email": "harry@ministry.com"}}
)

cursor = db.records.find({"last_name": "Potter"})
for i in cursor:
    pprint.pprint(i)

# Delete

db.records.delete_one({"hobby": "JVM"})

cursor = db.records.find({"last_name": "JVM"})
for i in cursor:
    pprint.pprint(i)
