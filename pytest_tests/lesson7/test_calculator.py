import pytest
from calculator import addition

#decorator
@pytest.mark.parametrize('number1, number2, result', (
        pytest.param(3, 2, 5, id='positive test with positive numbers'),
        pytest.param(-1, 4, 3, id='positive test with negative number'),
        pytest.param(4.3, 2.6, 6.9, id='positive test with float numbers')
))
def test_calculator(number1, number2, result):
    assert addition(number1,number2) == result