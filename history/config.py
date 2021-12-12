import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: We need to raise error if any of options missed
class Configuration(object):
    PORT = int(os.environ.get('PORT'))
    DBHOST = os.environ.get('DBHOST')
    DBNAME = os.environ.get('DBNAME')
    RABBIT = os.environ.get('RABBIT')
