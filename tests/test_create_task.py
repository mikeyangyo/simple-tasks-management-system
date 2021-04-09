from .test_listing_task import listing_tasks
from utils.enums import HttpStatusCode


def create_task(client, data: dict):
    rv = client.post('/tasks/', json=data)
    return rv


def test_create_task_pass(client):
    # expected: task create
    task_name = 'test_task_1'
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
    for task in tasks:
        assert set(['name', 'id', 'status']) == set(task.keys())
        if task['name'] == task_name:
            found = True
            break
    assert found


def test_create_task_with_space_name(client):
    # expected: raise 400
    task_name = '   '
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.BadRequest.value


def test_create_task_with_empty_name(client):
    # expected: raise 400
    task_name = ''
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.BadRequest.value
