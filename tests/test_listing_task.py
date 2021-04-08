def test_empty_db(client):
    rv = client.get('/tasks/')
    assert rv.json == {'result': []}
