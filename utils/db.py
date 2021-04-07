from pymysql import connect
from pymysql.cursors import DictCursor
from configs import db_config


def get_connection():
    return connect(host=db_config.DB_HOST,
                   user=db_config.DB_USER,
                   password=db_config.DB_PASSWORD,
                   database=db_config.DB_NAME,
                   port=db_config.DB_PORT,
                   cursorclass=DictCursor)
