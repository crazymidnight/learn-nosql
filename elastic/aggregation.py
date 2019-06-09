from elasticsearch import Elasticsearch
from dateutil.relativedelta import relativedelta
import datetime
import json

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
    user["age"] = relativedelta(datetime.datetime.now(), user["date_of_birth"]).years

# Write data to ElasticSearch
for idx, user in enumerate(users):
    res = es.index(index="phonebook", doc_type="contact", id=idx, body=user)

# Aggregate minimum, maximum and average age
aggregation = {
    "aggs": {
        "min_age": {"min": {"field": "age"}},
        "max_age": {"max": {"field": "age"}},
        "avg_age": {"avg": {"field": "age"}},
    }
}

res = es.search(index="phonebook", body=aggregation)["aggregations"]

print(f"Minimum age is {int(res['min_age']['value'])} years")
print(f"Maximum age is {int(res['max_age']['value'])} years")
print(f"Average age is {int(res['avg_age']['value'])} years")
