from pymongo import MongoClient
from datetime import datetime
from core import Configuration

dbclient = MongoClient(Configuration.DBHOST)
database = dbclient[Configuration.DBNAME]
collection = database['videos']

def addToHistory(videoId):
    record = { 'videoId': videoId, 'watched': datetime.now() }
    collection.insert_one(record)

def select() -> list:
    return [ { 'videoId': x['videoId'], 'watched': x['watched'] } for x in collection.find()]
