import pytest 

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by Zero.")
    return a/b

def test_add():
    assert add(10, 20) == 30
    assert add(25, 10) == 35

def test_mul():
    assert mul(5, 9) == 45
    assert mul(2, 3) == 6

def test_div():
    assert div(10, 5) == 2
    with pytest.raises(ValueError):
        assert div(10, 0) == 10

@pytest.mark.skip(reason="Skipping this test due to...")
def test_all():
    assert add(10, 20) == 30
    assert mul(5, 9) == 45
    assert div(10, 5) == 2



