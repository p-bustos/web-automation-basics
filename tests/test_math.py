import pytest

def test_addition():
    assert 1 + 1 == 2

def test_substraction():
    diff = 1 - 1
    assert diff == 0


def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    1 / 0