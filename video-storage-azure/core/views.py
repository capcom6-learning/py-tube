import os
from io import BufferedRandom, BytesIO
from datetime import datetime, timedelta
from flask import send_file, request, Response, abort, make_response, stream_with_context
from core import app, Configuration
from azure.storage.blob import generate_account_sas, ResourceTypes, AccountSasPermissions, BlobClient

async def pipe(f, t):
    await f.readinto(t)

@app.route('/video')
def video():
    path = request.args.get('path', '')
    bytes_range = request.range
    if not path:
        abort(400)

    account_url = "https://%s.blob.core.windows.net" % (Configuration.STORAGE_ACCOUNT_NAME,)
    sas_token = generate_account_sas(
        account_name=Configuration.STORAGE_ACCOUNT_NAME,
        account_key=Configuration.STORAGE_ACCESS_KEY,
        resource_types=ResourceTypes(object=True),
        permission=AccountSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )

    blob_client = BlobClient(account_url, "videos", path, credential=sas_token, max_chunk_get_size=1024*1024, max_single_get_size=1024*1024)
    properties = blob_client.get_blob_properties()
    # print(properties)

    offset = bytes_range.ranges[0][0] if bytes_range else 0
    length = ((bytes_range.ranges[0][1] or properties.size) - bytes_range.ranges[0][0] + 1) if bytes_range else properties.size

    print("Start %d length %d" % (offset, length))
    download_stream = blob_client.download_blob(
        offset = offset,
        length = length,
    )

    response = Response(stream_with_context(download_stream.chunks()))

    response.headers['Content-Type'] = properties.content_settings.content_type
    response.headers['Content-Length'] = length
    response.headers['Accept-Ranges'] = 'bytes'
    if bytes_range:
        response.headers['Content-Range'] = str(bytes_range.to_content_range_header(properties.size))
        response.status = 206
    return response
