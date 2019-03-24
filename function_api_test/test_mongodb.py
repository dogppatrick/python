from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient("localhost", 27017)
# select db
db = client["iii-2019-03"]
# select collection
c = db.food
# c = client["iii-2019-03"].food
# c.find()  = db.c.find in mongodb
for data in c.find():
    fruits = data["fruit"]
    for fruit in fruits:
        print(fruit, end="\t")
    print()
