import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# We need to raise error if any of options missed
class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PORT = os.environ.get('PORT')
    METADATA_HOST = os.environ.get('METADATA_HOST')
