import pytest
from calc import add,sub,mul,div
def test_add():
    assert add(10,20) == 30

def test_sub():
    assert add(20, 10) == 10

def test_mul():
    assert add(5,2) == 10

def test_div():
    assert add(10,2) == 5