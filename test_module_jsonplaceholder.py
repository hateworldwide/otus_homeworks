import requests
import json
import pytest

def test_get_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert r.status_code == 200
    assert r.json()[0].get("id")

def test_delete_posts():
    r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert r.status_code == 200

@pytest.mark.parametrize("body",
                         [{"title": "foo1", "body": "bar1", "userId": 1}, {"title": "foo2", "body": "bar2", "userId": 2}])
def test_creating_posts(body):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    r = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, data=json.dumps(body))
    assert r.status_code == 201 #http 201 == created
    assert r.json().get("id")
    assert r.json().get("title") == body["title"]



@pytest.mark.parametrize("body",
                         [{"id": 1, "title": "foo1", "body": "bar1", "userId": 1}, {"id":2, "title": "foo2", "body": "bar2", "userId": 2}])
def test_single(body):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    r = requests.put("https://jsonplaceholder.typicode.com/posts/" + str(body["id"]), headers=headers, data=json.dumps(body))
    assert r.status_code == 200
    assert r.json().get("id") == body["id"]
    assert r.json().get("title") == body["title"]

@pytest.mark.parametrize("body",
                         [{"id": 1, "title": "foo1"}, {"id":2, "title": "foo2"}])
def test_by_type(body):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    r = requests.patch("https://jsonplaceholder.typicode.com/posts/" + str(body["id"]), headers=headers, data=json.dumps(body))
    assert r.status_code == 200
    assert r.json().get("id") == body["id"]
    assert r.json().get("title") == body["title"]