# install python interpreter -  pytest-order
import pytest

@pytest.mark.order(3)
def test_DB_disconnection():
    print("DB disconnected")
    assert True

@pytest.mark.order(1)
def test_DB_connection():
    print("DB connected")
    assert True

@pytest.mark.order(2)
def test_data_check():
    print("Data checked")
    assert True
