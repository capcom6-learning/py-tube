import pprint
import requests
import json
from flask import Response, abort, request, stream_with_context

from . import metadata
from core import Configuration, app
from . import rabbit

@app.route('/video')
def video():
    videoId = request.args.get('id', '')
    if not videoId:
        abort(400)

    video = metadata.get_video(videoId)
    pprint.pprint(video)
    if not video:
        abort(404)

    if not request.range:
        msg = json.dumps({'videoId': video['_id']})
        channel = rabbit.makeChannel()
        channel.basic_publish(exchange='viewed', routing_key='', body=msg)
        rabbit.closeChannel()

    resp = requests.request(
        method=request.method,
        url="http://%s:%d/video?path=%s" % (Configuration.VIDEO_STORAGE_HOST, Configuration.VIDEO_STORAGE_PORT, video['videoPath'], ),
        headers={ key : value for (key, value) in request.headers if key != 'Host' },
        allow_redirects=False,
        stream=True,
    )

    excluded_headers = ['content-encoding', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(stream_with_context(resp.iter_content(64 * 1024)), resp.status_code, headers)
    return response

    