from src.math_operations import add, subtract

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_add():
    assert subtract(2,3) == -1
    assert subtract(-1,1) == -2
    assert subtract(5,3) == 2