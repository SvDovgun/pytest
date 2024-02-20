import requests
import time

class TestNew:
    def test_url(self):
        url = "https://api.trello.com/1/members/me/boards?key=d3d55161c01605cafa8a423ab1c8197c&token=ATTA3de8e01fe571f056208d007fb692a4511c801b7e3cb4896b2f27aff03d12427e782A1DBE"
        payload = {}
        response = requests.request("GET", url, data=payload)
        assert response.status_code == 200

    def test_5(self):
        assert True

    def test_7(self):
        assert True


def test_fail():
    assert False


def test_fail_2():
    assert False


def test_fail_3():
    assert False

def test_qa_1():
    assert True

def test_qa_4():
    time.sleep(2)
    assert True


def test_qa_5():
    time.sleep(1)
    assert True