from pymysql import connect
from pymysql.cursors import DictCursor
from flask import current_app


def get_connection(with_db=True):
    return connect(host=current_app.config['DB_HOST'],
                   user=current_app.config['DB_USER'],
                   password=current_app.config['DB_PASSWORD'],
                   database=current_app.config['DB_NAME'] if with_db else '',
                   port=current_app.config['DB_PORT'],
                   cursorclass=DictCursor)
