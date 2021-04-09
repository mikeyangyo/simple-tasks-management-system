from utils.enums import HttpStatusCode


def listing_tasks(client):
    return client.get('/tasks/')


def test_listing_tasks_pass(client):
    rv = listing_tasks(client)
    result_dict = rv.json
    assert rv.status_code == HttpStatusCode.OK.value
    assert isinstance(result_dict, dict)
    assert 'result' in result_dict.keys()
    tasks = result_dict['result']
    assert isinstance(tasks, list)
