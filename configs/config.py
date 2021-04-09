from configs import db_config
from os import path

class Config:
    DB_HOST = db_config.DB_HOST
    DB_USER = db_config.DB_USER
    DB_PASSWORD = db_config.DB_PASSWORD
    DB_NAME = db_config.DB_NAME
    DB_PORT = db_config.DB_PORT
    BASE_ROOT = path.dirname(path.dirname(path.abspath(__file__)))

class TestConfig(Config):
    DB_NAME = db_config.TEST_DB_NAME
    DB_HOST = '127.0.0.1'
