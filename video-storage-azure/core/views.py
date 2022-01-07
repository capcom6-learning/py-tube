from flask import request, Response, abort, stream_with_context, request
from core import app, Configuration
from core.storage import StorageClient

def make_client(path: str) -> StorageClient:
    return StorageClient(
        Configuration.STORAGE_ACCOUNT_NAME, 
        Configuration.STORAGE_ACCESS_KEY, 
        path
    )

@app.get('/video')
def video():
    path = request.args.get('path', '')
    bytes_range = request.range
    if not path:
        abort(400)

    client = make_client(path)

    properties = client.get_properties()
    
    offset = bytes_range.ranges[0][0] if bytes_range else 0
    length = ((bytes_range.ranges[0][1] or properties.size) - bytes_range.ranges[0][0] + 1) if bytes_range else properties.size
    print("Start %d length %d" % (offset, length))

    download_stream = client.get_download_stream(offset, length)

    response = Response(stream_with_context(download_stream.chunks()))

    response.headers['Content-Type'] = properties.content_settings.content_type
    response.headers['Content-Length'] = length
    response.headers['Accept-Ranges'] = 'bytes'
    if bytes_range:
        response.headers['Content-Range'] = str(bytes_range.to_content_range_header(properties.size))
        response.status = 206
    return response

@app.put('/video')
def put_video():
    path = request.args.get('path', '')
    if not path:
        abort(400)

    client = make_client(path)

    try:
        client.upload_stream(request.stream, request.content_type)
    except Exception as e:
        print(e)
        abort(500)

    return Response(status = 201)
