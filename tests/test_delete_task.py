from .test_create_task import create_task
from .test_listing_task import listing_tasks
from .test_retrieve_task import retrieve_task
from utils.enums import HttpStatusCode


def delete_task(client, _id: int):
    rv = client.delete(f'/tasks/{_id}')
    return rv


def test_delete_task_pass(client):
    # expected: deleting task success
    task_name = 'test_task_9'
    rv = create_task(client, {'name': task_name})
    assert rv.status_code == HttpStatusCode.Created.value
    rv = listing_tasks()
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

    rv = delete_task(client, task['id'])
    assert rv.status_code == HttpStatusCode.OK.value
    rv = retrieve_task(client, task['id'])
    assert rv.status_code == HttpStatusCode.NotFound.value


def test_delete_task_with_not_found_resource(client):
    # expect: raise 404
    rv = delete_task(client, 1000000)
    assert rv.status_code == HttpStatusCode.NotFound.value
