from elasticsearch import Elasticsearch, NotFoundError
import datetime

# Create instanse of elastic client
es = Elasticsearch()

# Create
new_record = {
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

count = es.count(index="phonebook", doc_type="contact")["count"]
print(f"Number of records: {count}")

res = es.index(index="phonebook", id=count, doc_type="contact", body=new_record)
print(f"Result of creating: {res['result']}")

# Read
res = es.get(index="phonebook", doc_type="contact", id=10)
print(f"Result of reading: {res}")

# Update
updated_record = {
    "first_name": "Harry",
    "last_name": "Potter",
    "gender": "Male",
    "email": "harry_potter@ministry.uk",
    "workplace": "Ministry of Magic",
    "university": "Hogwarts",
    "hobby": "Quidditch",
    "date_of_birth": datetime.datetime.strptime("23/09/1980", "%d/%m/%Y"),
    "phone": "+23 111 230 4214",
}
res = es.update(
    index="phonebook", id=count, doc_type="contact", body={"doc": updated_record}
)
print(f"Result of updating: {res['result']}")
res = es.get(index="phonebook", doc_type="contact", id=30)
print(f"Result of updating: {res}")

# Delete
res = es.delete(index="phonebook", id=count, doc_type="contact")
print(f"Result of deleting: {res['result']}")
try:
    res = es.get(index="phonebook", doc_type="contact", id=30)
except NotFoundError:
    print("Record not found")

# Search
search = {"query": {"match": {"university": "Yaroslavl"}}}
res = es.search(index="phonebook", body=search)

print("Result of searching:")
print(res)
