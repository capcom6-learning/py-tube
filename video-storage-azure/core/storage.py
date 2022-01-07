# Copyright 2022 Aleksandr Soloshenko
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from azure.storage.blob import generate_account_sas, ResourceTypes, AccountSasPermissions, BlobClient, BlobProperties, ContentSettings
from datetime import datetime, timedelta

class StorageClient:
    def __init__(self, account_name: str, account_key: str, path: str):
        container_name = 'videos'
        account_url = "https://%s.blob.core.windows.net" % (account_name,)
        sas_token = generate_account_sas(
            account_name=account_name,
            account_key=account_key,
            resource_types=ResourceTypes(object=True),
            permission=AccountSasPermissions(read=True, write=True),
            expiry=datetime.utcnow() + timedelta(hours=1)
        )
        self.client = BlobClient(
            account_url, 
            container_name, 
            path, 
            credential=sas_token, 
            max_chunk_get_size=1024*1024,   # important parameters for streaming
            max_single_get_size=1024*1024
        )

    def get_properties(self) -> BlobProperties:
        return self.client.get_blob_properties()

    def get_download_stream(self, offset: int = None, length: int = None):
        return self.client.download_blob(
            offset = offset,
            length = length,
        )
    
    def upload_stream(self, stream, content_type: str):
        return self.client.upload_blob(
            stream,
            content_settings=ContentSettings(content_type=content_type),
        )