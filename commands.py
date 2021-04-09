import click

from flask import current_app
from flask.cli import with_appcontext
from os import path, listdir
from utils.db import get_connection


def run_migrations():
    base_root = current_app.config['BASE_ROOT']
    migrations_folder = path.join(base_root, 'migrations')
    execution_order = {}
    for file_path in listdir(migrations_folder):
        file_name, extension_name = path.splitext(file_path)
        if extension_name != '.sql':
            continue
        try:
            serial_number, date, description = file_name.split('.')
        except ValueError:
            continue
        execution_order[serial_number] = '{}.{}'.format(date, description)

    for order in sorted(execution_order.keys()):
        file_path = '{}.{}.sql'.format(order, execution_order[order])
        file_content = []
        with open(path.join(migrations_folder, file_path)) as f:
            file_content = f.read().split(';')
        for row in file_content:
            sql_command = row.strip()
            if not sql_command:
                continue
            try:
                connection = get_connection()
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql_command)
                        connection.commit()
                except Exception:
                    current_app.logger.exception('Got Uncaught Error')
                finally:
                    connection.close()
            except Exception:
                current_app.logger.exception('DB Connect Fail')


@click.command('run-migrations')
@with_appcontext
def run_migrations_command():
    run_migrations()
