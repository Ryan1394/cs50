from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("testing") == "tstng"
    assert shorten("This is my twitter account") == "Ths s my twttr ccnt"