import os
from flask import request, Response, stream_with_context
from core import app, Configuration
import requests

@app.route('/video')
def video():
    resp = requests.request(
        method=request.method,
        url="http://%s:%d/video?path=SampleVideo_1280x720_30mb.mp4" % (Configuration.VIDEO_STORAGE_HOST, Configuration.VIDEO_STORAGE_PORT,),
        headers={ key : value for (key, value) in request.headers if key != 'Host' },
        allow_redirects=False,
        stream=True,
    )

    excluded_headers = ['content-encoding', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(stream_with_context(resp.iter_content(64 * 1024)), resp.status_code, headers)
    return response

    