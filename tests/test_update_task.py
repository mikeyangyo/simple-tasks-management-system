from .test_create_task import create_task
from .test_listing_task import listing_tasks
from .test_retrieve_task import retrieve_task
from utils.enums import HttpStatusCode


def update_task(client, _id: int, data: dict):
    rv = client.put(f'/tasks/{_id}', json=data)
    return rv


def test_update_task_pass(client):
    # expected: update task with given status, name property
    task_name = 'test_task_3'
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.Created.value
    rv = listing_tasks(client)
    result_dict = rv.json
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    tasks = result_dict['result']
    assert isinstance(tasks, list)
    found = False
    task_created = {}
    for task in tasks:
        assert set(['name', 'id', 'status']) == set(task.keys())
        if task['name'] == task_name:
            found = True
            task_created = task.copy()
            break
    assert found
    rv = retrieve_task(client, task_created['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == task_name
    assert task['id'] == task_created['id']
    assert task['status'] == task_created['status']

    status_updated = 1
    name_updated = 'test_task_4'
    rv = update_task(client, task['id'], {
        'status': status_updated,
        'name': name_updated
    })
    assert rv.status_code == HttpStatusCode.OK.value
    rv = retrieve_task(client, task['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == name_updated
    assert task['id'] == task['id']
    assert task['status'] == status_updated


def test_update_task_with_try_to_update_id(client):
    # expected: id not changed, another property was changed
    task_name = 'test_task_5'
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.Created.value
    rv = listing_tasks(client)
    result_dict = rv.json
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    tasks = result_dict['result']
    assert isinstance(tasks, list)
    found = False
    task_created = {}
    for task in tasks:
        assert set(['name', 'id', 'status']) == set(task.keys())
        if task['name'] == task_name:
            found = True
            task_created = task.copy()
            break
    assert found
    rv = retrieve_task(client, task_created['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == task_name
    assert task['id'] == task_created['id']
    assert task['status'] == task_created['status']

    id_updated = 0
    status_updated = 1
    name_updated = 'test_task_6'
    rv = update_task(client, task['id'], {
        'id': id_updated,
        'status': status_updated,
        'name': name_updated
    })
    assert rv.status_code == HttpStatusCode.BadRequest.value
    rv = retrieve_task(client, task['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == name_updated
    assert task['id'] != id_updated
    assert task['status'] == status_updated


def test_update_task_with_undefined_status(client):
    # expected: raise 400
    task_name = 'test_task_6'
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.Created.value
    rv = listing_tasks(client)
    result_dict = rv.json
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    tasks = result_dict['result']
    assert isinstance(tasks, list)
    found = False
    task_created = {}
    for task in tasks:
        assert set(['name', 'id', 'status']) == set(task.keys())
        if task['name'] == task_name:
            found = True
            task_created = task.copy()
            break
    assert found
    rv = retrieve_task(client, task_created['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == task_name
    assert task['id'] == task_created['id']
    assert task['status'] == task_created['status']

    status_updated = 2
    name_updated = 'test_task_7'
    rv = update_task(client, task['id'], {
        'status': status_updated,
        'name': name_updated
    })
    assert rv.status_code == HttpStatusCode.BadRequest.value


def test_update_task_with_space_name(client):
    # expected: raise 400
    task_name = 'test_task_8'
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.Created.value
    rv = listing_tasks(client)
    result_dict = rv.json
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    tasks = result_dict['result']
    assert isinstance(tasks, list)
    found = False
    task_created = {}
    for task in tasks:
        assert set(['name', 'id', 'status']) == set(task.keys())
        if task['name'] == task_name:
            found = True
            task_created = task.copy()
            break
    assert found
    rv = retrieve_task(client, task_created['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    task = result_dict['result']
    assert isinstance(task, dict)
    assert task['name'] == task_name
    assert task['id'] == task_created['id']
    assert task['status'] == task_created['status']

    status_updated = 2
    name_updated = '   '
    rv = update_task(client, task['id'], {
        'status': status_updated,
        'name': name_updated
    })
    assert rv.status_code == HttpStatusCode.BadRequest.value
