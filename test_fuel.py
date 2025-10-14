from fuel import convert,gauge
import pytest

def main():
    pass

def test_e():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_convert():
    assert convert("1/2")==50
    assert convert("1/4")==25
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
