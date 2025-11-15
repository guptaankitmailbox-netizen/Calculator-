import pytest
from calc import create, add, subtract

def test_create_default():
    assert create() == 0

def test_create_value():
    assert create(5) == 5
    assert create(2.5) == 2.5

def test_create_invalid():
    with pytest.raises(TypeError):
        create("a")

def test_add():
    assert add(1,2) == 3
    assert add(2.5, 1.5) == 4.0

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(2.5, 1.0) == 1.5
