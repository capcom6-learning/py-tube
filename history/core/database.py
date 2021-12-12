from pymongo import MongoClient
import pymongo
from core import Configuration
from bson.objectid import ObjectId, InvalidId

dbclient = MongoClient(Configuration.DBHOST)
database = dbclient[Configuration.DBNAME]
collection = database['videos']

def addToHistory(videoId):
    record = { 'videoId': videoId }
    collection.insert_one(record)
