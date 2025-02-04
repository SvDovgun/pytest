import pytest
import requests

@pytest.fixture()
def database():
    print("connect....")
    data = 10
    yield data
    print("close....")

@pytest.fixture(scope="function")
def fixture_func():
    print("-> function")
    yield
    print("function <-")


@pytest.fixture(scope="class")
def fixture_class():
    print("-> class")
    yield
    print("class <-")


@pytest.fixture(scope="module")
def fixture_module():
    print("-> module")
    yield
    print("module <-")

@pytest.fixture(scope="package")
def fixture_package():
    print("-> package")
    yield
    print("package <-")

@pytest.fixture(scope="session")
def fixture_session():
    print("-> session")
    yield
    print("session <-")


# @pytest.fixture(scope="session")
# def postman_request():
#     url = "https://api.trello.com/1/members/me/boards?key=d3d55161c01605cafa8a423ab1c8197c&token=ATTA3de8e01fe571f056208d007fb692a4511c801b7e3cb4896b2f27aff03d12427e782A1DBE"
#     payload = {}
#     response = requests.request("GET", url, data=payload)
#     yield response