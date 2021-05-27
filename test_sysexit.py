# content of test_sysexit.py
import pytest


def f():
    raise SystemExitt(1)


def test_mytest():
    with pytest.raises(SystemExitt(i)):
        f()
