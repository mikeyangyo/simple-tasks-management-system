from flask import jsonify, current_app, abort, request

from . import task_bp
from utils.db import get_connection
from utils.enums import HttpStatusCode


@task_bp.route('/', methods=['GET'])
def listing_tasks():
    try:
        connection = get_connection()
        result = []
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM tasks ORDER BY id DESC')
                result = cursor.fetchall()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))
    return jsonify(result=result), HttpStatusCode.OK.value


@task_bp.route('/', methods=['POST'])
def create_task():
    body = request.json
    task_name = body.get('name')
    if not task_name:
        abort(HttpStatusCode.BadRequest.value, description="name not found")

    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO tasks (name) VALUES (%s)',
                               (task_name, ))
                connection.commit()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))
    return jsonify({"name": task_name}), HttpStatusCode.Created.value


@task_bp.route('/<_id>', methods=['GET'])
def retrieve_task(_id: int):
    result = {}
    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM tasks WHERE id=%s LIMIT 1',
                               (_id, ))
                result = cursor.fetchone()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))
    if not result:
        abort(HttpStatusCode.NotFound.value, description="task not found")
    return jsonify(result=result), HttpStatusCode.OK.value


@task_bp.route('/<_id>', methods=['PUT'])
def update_task(_id: int):
    body = request.json
    updated_part = {}
    task_name = body.get('name')
    task_status = body.get('status')
    if task_status is not None:
        try:
            task_status = int(task_status)
        except ValueError:
            abort(HttpStatusCode.BadRequest.value,
                  description="task status must be int type")
        if task_status not in (0, 1):
            abort(HttpStatusCode.BadRequest.value,
                  description="task status must be 0 or 1")
        updated_part['status'] = task_status
    if task_name is not None:
        if not task_name:
            abort(HttpStatusCode.BadRequest.value,
                  description="task name cannot be empty")
        updated_part['name'] = task_name

    if not updated_part:
        return {}, HttpStatusCode.OK.value

    result = {}
    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE tasks SET {} WHERE id=%s'.format(','.join(
                        ['{}=%s'.format(key) for key in updated_part.keys()])),
                    list(updated_part.values()) + [_id])
                connection.commit()
                cursor.execute('SELECT * FROM tasks WHERE id=%s LIMIT 1',
                               (_id, ))
                result = cursor.fetchone()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))
    if not result:
        abort(HttpStatusCode.NotFound.value, description="task not found")

    return jsonify(result), HttpStatusCode.OK.value


@task_bp.route('/<_id>', methods=['DELETE'])
def delete_task(_id: int):
    result = {}
    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM tasks WHERE id=%s LIMIT 1',
                               (_id, ))
                result = cursor.fetchone()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))

    if not result:
        abort(HttpStatusCode.NotFound.value, description='task not found')

    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM tasks WHERE id=%s', (_id, ))
                connection.commit()
        except Exception as e:
            current_app.logger.exception("Got Uncaught Error")
            abort(HttpStatusCode.InternalError.value, description=str(e))
        finally:
            connection.close()
    except Exception as e:
        current_app.logger.exception("Connect DB Fail")
        abort(HttpStatusCode.InternalError.value, description=str(e))
    return {}, HttpStatusCode.OK.value
