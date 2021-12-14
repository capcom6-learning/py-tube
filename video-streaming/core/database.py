from pymongo import MongoClient
from core import Configuration
from bson.objectid import ObjectId, InvalidId

dbclient = MongoClient(Configuration.DBHOST)
database = dbclient[Configuration.DBNAME]
collection = database['videos']

def getVideoById(videoId):
    try:
        objectId = ObjectId(videoId)
    except InvalidId:
        return None
    return collection.find_one({"_id": objectId})
