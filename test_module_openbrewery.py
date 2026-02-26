import requests
import json
import pytest

def test_metadata():
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/meta?by_country=south_korea")
    assert r.status_code == 200
    assert r.json().get("page") == 1

def test_random_brewery():
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    assert r.status_code == 200
    assert r.json()[0].get("name")

@pytest.mark.parametrize("count",
                         [9, 4])
def test_multiple_random(count):
    r = requests.get(" https://api.openbrewerydb.org/v1/breweries?per_page=" + str(count))
    assert r.status_code == 200
    assert len(r.json()) == count


@pytest.mark.parametrize(("obdbid", "name"),
                         [("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "MadTree Brewing 2.0"),
                          ("34e8c68b-6146-453f-a4b9-1f6cd99a5ada", "1 of Us Brewing Company")])
def test_single(obdbid, name):
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/" + obdbid)
    assert r.status_code == 200
    assert r.json().get("id") == obdbid
    assert r.json().get("name") == name

@pytest.mark.parametrize("type",
                         ["micro", "closed"])
def test_by_type(type):
    r = requests.get("https://api.openbrewerydb.org/v1/breweries?by_type=" + type + "&per_page=3")
    assert r.status_code == 200
    for brewery in r.json():
        assert brewery["brewery_type"] == type