import requests

def test_status_code(url, status_code):
    r = requests.get(url)
    assert r.status_code == int(status_code)

