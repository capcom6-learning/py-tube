import requests
import pprint

from core import Configuration

def select_video() -> list[dict]:
    response = requests.get('%s/video' % (Configuration.METADATA_HOST, ))
    
    if response.status_code == 200:
        return response.json()
    return None

def get_video(id: str) -> dict:
    response = requests.get('%s/video' % (Configuration.METADATA_HOST, ), params={"id": id})
    
    if response.status_code == 200:
        return response.json()
    return None
