import os

def test_health(client):
    """ Send notification """
    res = client.get(f"/health")
    assert res.status_code == 200
    hostname = os.environ.get('HOSTNAME')
    assert res.text == f'"{hostname} OK"'
