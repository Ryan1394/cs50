from bankk import value

def main():
    test_value_hello()
    test_value_h()
    test_value_0theR()

def test_value_hello():
    """
    checks if starting with hello or not
    """
    assert value("Hello Human") == 0
    assert value("Hello") == 0
    assert value("hello") == 0

def test_value_h():
    """
    checks if starting with h or not
    """
    assert value("how ur doin'") == 25
    assert value("hi :D") == 25
    assert value("hll0") == 25

def test_value_0theR():
    assert value("What's happening? :| ") == 100
    assert value("Karkerkar kurkur") == 100
    assert value("50") == 100