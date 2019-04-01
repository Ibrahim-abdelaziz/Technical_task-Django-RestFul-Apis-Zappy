from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db=client['test-database']
task = db.Task

