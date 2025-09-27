import requests
import json
import pytest

def test_list_all():
    r = requests.get("https://dog.ceo/api/breeds/list/all")
    assert r.status_code == 200
    assert r.json().get("status") == "success"

def test_random_breed():
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    assert r.status_code == 200
    assert r.json().get("status") == "success"

@pytest.mark.parametrize("count",
                         [9, 4])
def test_multiple_random(count):
    r = requests.get("https://dog.ceo/api/breeds/image/random/" + str(count))
    assert r.status_code == 200
    assert r.json().get("status") == "success"
    assert len(r.json().get("message")) == count, f"Wrong count of images"


@pytest.mark.parametrize("breed",
                         ["hound", "labrador"])
def test_random_image_from_breed(breed):
    r = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    assert r.status_code == 200
    assert r.json().get("status") == "success"
    assert requests.get(r.json()["message"]).status_code == 200, f"Wrong link in response"

@pytest.mark.parametrize("breed",
                         ["mastiff", "retriever"])
def test_list_subbreed_images(breed):
    r = requests.get("https://dog.ceo/api/breed/" + breed + "/images")
    assert r.status_code == 200
    assert r.json().get("status") == "success"
    list = r.json().get("message")
    assert requests.get(r.json().get("message")[0]).status_code == 200
    #если список большой, то проверим ещё парочку, но не все
    if len(list) > 3:
        assert requests.get(r.json().get("message")[1]).status_code == 200
        assert requests.get(r.json().get("message")[2]).status_code == 200