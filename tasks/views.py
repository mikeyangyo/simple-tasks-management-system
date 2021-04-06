from flask import jsonify

from . import task_bp


@task_bp.route('/', methods=['GET'])
def listing_tasks():
    return jsonify({"result": [{"id": 1, "name": "name", "status": 0}]})


@task_bp.route('/', methods=['POST'])
def create_task():
    return jsonify({"name": "買晚餐"}), 201


@task_bp.route('/<_id>', methods=['GET'])
def retrieve_task(_id: int):
    return jsonify({"result": {"name": "買晚餐", "status": 0, "id": 1}})


@task_bp.route('/<_id>', methods=['PUT'])
def update_task(_id: int):
    return jsonify({"name": "買早餐", "status": 1, "id": 1})


@task_bp.route('/<_id>', methods=['DELETE'])
def delete_task(_id: int):
    return {}
