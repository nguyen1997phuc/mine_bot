import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

api_key = os.environ.get('API_KEY')
secret_key = os.environ.get('SECRET_KEY')
