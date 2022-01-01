from pymongo import MongoClient
from datetime import datetime
from core import Configuration
from bson.objectid import ObjectId, InvalidId

dbclient = MongoClient(Configuration.DBHOST)
database = dbclient[Configuration.DBNAME]
collection = database['videos']

def addToHistory(videoId):
    record = { 'videoId': videoId, 'watched': datetime.now() }
    collection.insert_one(record)
