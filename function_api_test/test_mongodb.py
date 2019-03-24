from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
# pymongo tutirial https://api.mongodb.com/python/current/tutorial.html
# _id need import bson.objectid
# MongoClient(host='localhost', port=27017, document_class=dict,
#             tz_aware=False, connect=True, **kwargs)
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient()
# select db create if no db
db = client["test0324"]
# select collection create in no collection
c = db.c1
# _id not define >> _id auto create
# new_fruit make a data to insert
new_fruit = {"fruit": ["mongo", "melon"],
             "size": 9}
# insert
# c.insert_one(new_fruit)
# c.insert_many([{},{}]...) >> insert more than one data

# c = client["test0324"].c1
# c.find()  = db.c1.find in mongodb
for data in c.find():
    fruits = data["fruit"]
    # for fruit in fruits:
    #     print(fruit, end="\t")
    print(data)
print("===")
# querying by find({})
print(c.find_one({"_id": ObjectId('5c971e256e5cc32b50e95b02')}))
# collection data count
print(c.count_documents({"size": 5}))
# build index
result = db.profiles.create_index([('_id', pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))
