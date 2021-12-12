import os
import pprint

from flask import Response, abort, request, stream_with_context

from core import Configuration, app

from . import database

@app.route('/')
def index():
    return 'History service online'

@app.route('/viewed', methods=['POST'])
def viewed():
    payload = request.get_json()
    if not payload:
        abort(400)

    videoPath = payload['videoPath']
    if not videoPath:
        abort(400)

    database.addToHistory(videoPath)
    
    return Response(None, 200)

    