from pymongo import MongoClient
import pprint
import datetime

client = MongoClient()

db = client.phonebook

db.records.delete_one({"phone": "+23 111 230 4214"})

# Create
print("CREATE:")
db.records.insert_one(
    {
        "first_name": "Harry",
        "last_name": "Potter",
        "gender": "Male",
        "email": "hpotter@hw.com",
        "workplace": "Ministry of Magic",
        "university": "Hogwarts",
        "hobby": "Magic",
        "date_of_birth": datetime.datetime.strptime("23/09/1980", "%d/%m/%Y"),
        "phone": "+23 111 230 4214",
    }
)

cursor = db.records.find({"last_name": "Potter"})
for i in cursor:
    pprint.pprint(i)

# Read

cursor = db.records.find({"phone": "+55 975 220 3198"})
print("READ:")
for i in cursor:
    pprint.pprint(i)

# Update
print("UPDATE:")
db.records.update_one(
    {"last_name": "Potter"}, {"$set": {"email": "harry@ministry.com"}}
)

cursor = db.records.find({"last_name": "Potter"})
for i in cursor:
    pprint.pprint(i)

# Delete
print("DELETE:")
db.records.delete_one({"university": "+23 111 230 4214"})

cursor = db.records.find({"phone": "Hogwarts"})
for i in cursor:
    pprint.pprint(i)
