import pytest 

@pytest.fixture(scope="module")
def calculator():
    from simple_example import Calculator
    return Calculator()