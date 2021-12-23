from flask import Response
from bson import json_util

from . import database
from core import app

@app.route('/', methods=['GET'])
def index():
    return 'Metadata service online'

@app.route('/videos', methods=['GET'])
def videos():
    return Response(json_util.dumps(database.select_videos(), json_options=json_util.CANONICAL_JSON_OPTIONS), content_type='application/json')
