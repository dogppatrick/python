from pymongo import MongoClient
import pymongo
import random
from bson.objectid import ObjectId
# pymongo tutirial https://api.mongodb.com/python/current/tutorial.html
# _id need import bson.objectid
# MongoClient(host='localhost', port=27017, document_class=dict,
#             tz_aware=False, connect=True, **kwargs)
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient()
# select db create if no db
db = client["fruit"]
# select collection create in no collection
c = db.items
# _id not define >> _id auto create
# new_fruit make a data to insert
# f1 = {"fruit": ["mongo", "melon"],
#       "size": 9}
# f2 = {"fruit": ["apple", "banana"],
#       "size": 3}
# fruits = [f1, f2]
fruits =[]
fruit_list = ["apple", "melon", "banana", "orange"]
for i in range(5):
    fruit_data = {"fruit": fruit_list[random.randint(0, 3)], "size": random.randint(1, 10)}
    fruits.append(fruit_data)
# insert
# c.insert_one(f1)
# c.insert_many([{},{}]...) >> insert more than one data
result = c.insert_many(fruits)
# c = client["test0324"].c1
# c.find()  = db.c1.find in mongodb
for data in c.find():
    # fruits = data["fruit"]
    # for fruit in fruits:
    #     print(fruit, end="\t")
    print(data)
print("===")
# querying by find({})
# print(c.find_one({"_id": ObjectId('5c971e256e5cc32b50e95b02')}))
# collection data count
print(c.count_documents({"size": 3}))
# build index
# db.items.create_index([('_id', pymongo.ASCENDING)], unique=True)
# sorted(list(db.itmes.index_information()))
# drop collection
c.drop()
