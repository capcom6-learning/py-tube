from flask import g, current_app
from flask_pymongo import PyMongo

def get_db():
    if 'db' not in g:
        g.db = PyMongo(current_app)
    return g.db

def select_videos() -> list:
    return get_db().db.videos.find()
    # dbclient = MongoClient(Configuration.DBHOST)
    # database = dbclient[Configuration.DBNAME]
    # collection = database['videos']
    # return list(collection.find())
