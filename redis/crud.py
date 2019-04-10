import redis
from pprint import pprint


r = redis.Redis(host="localhost", port=6379, db=0)

# Create
new_user = {
    "first_name": "Alexey",
    "last_name": "Voytsekhovskiy",
    "gender": "Male",
    "email": "alex@somemail.com",
    "phone": "+5 232 434 2343",
    "workplace": "speech2doc",
    "university": "Tomsk Polytechnic University",
    "hobby": "TV shows",
    "date_of_birth": "07/05/1996",
}

r.hmset("users:30", new_user)
result = r.hgetall("users:30")
pprint(result)

# Read
user = r.hgetall("users:19")
print(f"User #19:")
pprint(user)
first_name = r.hmget("users:7", "first_name", "last_name")
print(f"Name of user #7:")
pprint(first_name)

# Update
result = r.hset("users:19", "hobby", "Dance")
hobby = r.hget("users:19", "hobby")
pprint(hobby)

# Delete
r.delete("users:18")
exists = r.exists("users:18")
print("User exists:")
print(exists)
