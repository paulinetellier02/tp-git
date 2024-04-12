from calculator import addition

def test_addition():
    assert addition(1, 2) == 3

from calculator import soustraction

def test_soustraction():
    assert soustraction(10,8) == 2

def test_soustraction():
    assert soustraction(18,8) == 10

from calculator import division

def test_division():
    assert division(8,2)==4