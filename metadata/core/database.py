from flask import g, current_app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId, InvalidId

def get_db() -> PyMongo:
    if 'db' not in g:
        g.db = PyMongo(current_app)
    return g.db

def select_videos() -> list:
    videos = []
    for v in get_db().db.videos.find():
        v['_id'] = str(v['_id'])
        videos.append(v)
    return videos
    
def get_video(id: str):
    try:
        videoId = ObjectId(id)
    except InvalidId:
        return None
    video = get_db().db.videos.find_one({"_id": videoId})
    if video:
        video['_id'] = str(video['_id'])
    return video
