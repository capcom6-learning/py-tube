import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PORT = os.environ.get('PORT')
    STORAGE_ACCOUNT_NAME = os.environ.get('STORAGE_ACCOUNT_NAME')
    STORAGE_ACCESS_KEY = os.environ.get('STORAGE_ACCESS_KEY')
