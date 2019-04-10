import redis
import json


with open("../sample.json") as f:
    users = [x for x in json.load(f)]

r = redis.Redis(host="localhost", port=6379, db=0)

for idx, user in enumerate(users):
    r.hmset(f"users:{idx}", user)
