from pymongo import MongoClient
import datetime
# MongoClient(host='localhost', port=27017, document_class=dict,
#             tz_aware=False, connect=True, **kwargs)
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient()
# select db create if no db
db = client["test0324"]
# select collection create in no collection
c = db.c1
# _id not define >> _id auto create
new_fruit = {"fruit": ["mongo", "melon"],
             "size": 5}
c.insert_one(new_fruit)
# c = client["test0324"].c1
# c.find()  = db.c1.find in mongodb
for data in c.find():
    fruits = data["fruit"]
    # for fruit in fruits:
    #     print(fruit, end="\t")
    print(data)
    print()
# insert

# new_fruit

