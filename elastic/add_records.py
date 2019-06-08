from elasticsearch import Elasticsearch
import json
import datetime

# Create instanse of elastic client
es = Elasticsearch()

# Load phonebook data from json
with open("../sample.json") as f:
    users = json.load(f)

# Format date of birth to datetime
for user in users:
    user["date_of_birth"] = datetime.datetime.strptime(
        user["date_of_birth"], "%d/%m/%Y"
    )

# Write data to ElasticSearch
for idx, user in enumerate(users):
    res = es.index(index="phonebook", doc_type="contact", id=idx, body=user)
    print(res["result"])
    
# Test record
res = es.get(index="phonebook", doc_type="contact", id=1)
print(res["_source"])
