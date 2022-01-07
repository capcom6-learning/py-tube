from flask import Response, abort, request, jsonify

from core import app

from . import database

@app.route('/')
def index():
    return 'History service online'

@app.post('/viewed')
def viewed():
    payload = request.get_json()
    if not payload:
        abort(400)

    videoPath = payload['videoId']
    if not videoPath:
        abort(400)

    database.addToHistory(videoPath)
    
    return Response(None, 200)

@app.get('/viewed')
def get_viewed():
    return jsonify(database.select())
