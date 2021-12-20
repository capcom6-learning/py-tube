import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: We need to raise error if any of options missed
class Configuration(object):
    RABBIT = os.environ.get('RABBIT')
