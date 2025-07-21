import pytest
import requests

BASE_URL = "https://catfact.ninja"

@pytest.mark.parametrize("endpoint", ["/fact", "/facts?limit=3"])
def test_valid_endpoints_should_return_200(endpoint):
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200

def test_fact_response_contains_fact_and_length():
    response = requests.get(f"{BASE_URL}/fact")
    assert response.status_code == 200
    data = response.json()
    assert "fact" in data
    assert "length" in data
    assert len(data["fact"]) == data["length"]

def test_facts_list_has_expected_structure():
    response = requests.get(f"{BASE_URL}/facts?limit=3")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) == 3
    assert "fact" in data["data"][0]

@pytest.mark.parametrize("invalid_path", ["/wrong"])
def test_invalid_requests_should_fail(invalid_path):
    response = requests.get(BASE_URL + invalid_path)
    assert response.status_code in [400, 404]
