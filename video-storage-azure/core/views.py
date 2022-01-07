from datetime import datetime, timedelta
from flask import request, Response, abort, stream_with_context
from core import app, Configuration
from azure.storage.blob import generate_account_sas, ResourceTypes, AccountSasPermissions, BlobClient
from core.storage import StorageClient

@app.route('/video')
def video():
    path = request.args.get('path', '')
    bytes_range = request.range
    if not path:
        abort(400)

    client = StorageClient(
        Configuration.STORAGE_ACCOUNT_NAME, 
        Configuration.STORAGE_ACCESS_KEY, 
        path
    )

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
