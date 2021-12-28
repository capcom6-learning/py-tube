import requests
import pprint

from core import Configuration

def get_video(id: str) -> dict:
    response = requests.get('%s/video' % (Configuration.METADATA_HOST, ), params={"id": id})
    
    if response.status_code == 200:
        return response.json()
    return None