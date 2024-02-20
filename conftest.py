import pytest
import requests


@pytest.fixture(scope="session")
def postman_request():
    url = "https://api.trello.com/1/members/me/boards?key=d3d55161c01605cafa8a423ab1c8197c&token=ATTA3de8e01fe571f056208d007fb692a4511c801b7e3cb4896b2f27aff03d12427e782A1DBE"
    payload = {}
    response = requests.request("GET", url, data=payload)
    yield response