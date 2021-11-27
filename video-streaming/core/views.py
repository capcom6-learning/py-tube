import os
from datetime import datetime
from flask import send_file, request, Response
from flask_rangerequest import RangeRequest
from core import app
from config import basedir

@app.route('/video')
def video():
    filename = os.path.join(basedir, 'videos', 'SampleVideo_1280x720_30mb.mp4')
    stats = os.stat(filename)
    size = stats.st_size
    last_modified = datetime.fromtimestamp(stats.st_mtime)
    with open(filename, 'rb') as f:
        etag = RangeRequest.make_etag(f)
    return RangeRequest(
        open(filename, 'rb'), 
        size=size, 
        etag=etag, 
        last_modified=last_modified
    ).make_response()
    